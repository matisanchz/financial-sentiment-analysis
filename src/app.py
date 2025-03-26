from customtkinter import *

from config import Settings
from model import FinbertModel
from utils import generate_date_list
from PIL import Image
import os


def get_sentiment_analysis(app, frame, date_from, date_to, keyword):
    if keyword != "":
        print(keyword)

        model = FinbertModel()

        num_positive_articles, num_negative_articles, num_neutral_articles, result, final_score = model.get_sentiment(keyword, date_from, date_to)

        frame.destroy()

        label1 = CTkLabel(app, text=f'Total positive articles: {num_positive_articles}')
        label1.pack(pady=12,padx=10)

        label2 = CTkLabel(app, text=f'Total negative articles: {num_negative_articles}')
        label2.pack(pady=12,padx=10)

        label3 = CTkLabel(app, text=f'Total neutral articles: {num_neutral_articles}')
        label3.pack(pady=12,padx=10)

        frame = CTkFrame(master=app)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        if result == 'Positive':
            img_path = Settings.POSITIVE_IMAGE
        elif result == 'Negative':
            img_path = Settings.NEGATIVE_IMAGE
        else:
            img_path = Settings.NEUTRAL_IMAGE

        img = Image.open(img_path)

        image = CTkImage(light_image=img, dark_image=img, size=(40,40))
        
        label5 = CTkLabel(frame, image=image, text="") 
        label5.pack(pady=10)

        label6 = CTkLabel(frame, text=result) 
        label6.pack(pady=10)

        return_app = CTkButton(master=app, text="Return", command=lambda: return_main(app))
        return_app.pack()

def return_main(app):
    app.destroy()
    main()
    
def main():

    set_appearance_mode("dark")
    set_default_color_theme("themes/MoonlitSky.json")

    app = CTk()
    app.geometry("600x500")

    body = CTkFrame(app)
    body.pack(pady=20, padx=60, fill="both", expand=True)

    header = CTkFrame(body)
    header.pack(pady=10)

    img = Image.open("images/logo.png")

    image = CTkImage(light_image=img, 
                     dark_image=img, 
                     size=(120,120))

    logo = CTkLabel(header, image=image, text="") 
    logo.pack(padx=10, pady=10, side="left")

    title = CTkLabel(header, 
                     text="Financial Sentiment Analysis", 
                     font=("Arial", 20, "bold"))
    
    title.pack(padx=10, pady=10, side="left")

    description = CTkLabel(body, 
                           text="Analyze the sentiment of financial news based on a specific keyword and date range. "
                           "Enter a start date, end date, and keyword to gain insights into market sentiment.",
                           wraplength=400, 
                           justify="center",
                           font=("Arial", 15))
    
    description.pack(pady=10)

    dates=generate_date_list()

    from_box = CTkComboBox(master=body, 
                           values=dates, 
                           corner_radius=10)
    
    from_box.pack(pady=12,padx=10)

    to_box = CTkComboBox(master=body, values=dates, corner_radius=10)
    to_box.pack(pady=12,padx=10)

    input = CTkEntry(master=body)
    input.pack(pady=12,padx=10)

    btn = CTkButton(master=body, 
                    text="Submit", 
                    command=lambda: get_sentiment_analysis(app, body, from_box.get(), to_box.get(), input.get()))
    btn.pack()

    app.mainloop()

if __name__ == "__main__":
    main()
