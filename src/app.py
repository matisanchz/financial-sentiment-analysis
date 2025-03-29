import threading
from customtkinter import *

from config import Settings
from model import FinbertModel
from utils import generate_date_list
from PIL import Image
import os

def get_sentiment_analysis(app, frame, date_from, date_to, keyword):
    if keyword != "" and date_from <= date_to:

        frame.destroy()

        app.geometry("300x200")

        preloader = CTkFrame(master=app)
        preloader.pack(pady=20, padx=60, fill="both", expand=True)
        
        loading_label = CTkLabel(preloader, text="Analyzing sentiment...", font=("Arial", 16, "bold"))
        loading_label.pack(pady=20)

        img = Image.open("images/wait.png")

        image = CTkImage(light_image=img, 
                        dark_image=img, 
                        size=(60,60))

        wait = CTkLabel(preloader, image=image, text="") 
        wait.pack(padx=10, pady=10)

        # Inicia el análisis en un hilo separado
        thread = threading.Thread(target=lambda: analyze_sentiment(app, preloader, date_from, date_to, keyword))
        thread.start()

    else:
        open_popup(keyword, date_from, date_to)

def analyze_sentiment(app, preloader, date_from, date_to, keyword):

    model = FinbertModel()

    num_positive_articles, num_negative_articles, num_neutral_articles, result, final_score = model.get_sentiment(keyword, date_from, date_to)

    preloader.destroy()

    app.geometry("400x450")

    label1 = CTkLabel(app, text=f'Total positive articles: {num_positive_articles}')
    label1.pack(pady=12,padx=10)

    label2 = CTkLabel(app, text=f'Total negative articles: {num_negative_articles}')
    label2.pack(pady=12,padx=10)

    label3 = CTkLabel(app, text=f'Total neutral articles: {num_neutral_articles}')
    label3.pack(pady=12,padx=10)

    frame = CTkFrame(master=app)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    title = CTkLabel(frame, 
                     text="Sentiment Analysis:", 
                     font=("Arial", 20, "bold"))
    
    title.pack(padx=10, pady=10)

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

    label6 = CTkLabel(frame, text=f"Final Score: {final_score}") 
    label6.pack(pady=10)

    return_app = CTkButton(master=app, text="Return", command=lambda: return_main(app))
    return_app.pack()

def open_popup(keyword, date_from, date_to):
    popup = CTkToplevel()
    popup.title("Validator")

    if keyword == "":

        label1 = CTkLabel(popup, text="You must enter a valid keyword", font=("Arial", 14))
        label1.pack(pady=20, padx=20)

    if date_from > date_to:
        label2 = CTkLabel(popup, text="Date 'To' must be after Date 'From'.", font=("Arial", 14))
        label2.pack(pady=20, padx=20)

    close_button = CTkButton(popup, text="Cerrar", command=popup.destroy)
    close_button.pack(pady=10)

    popup.transient()
    popup.grab_set()

def return_main(app):
    app.destroy()
    main()
    
def main():

    set_appearance_mode("dark")
    set_default_color_theme("themes/GhostTrain.json")

    app = CTk()
    app.geometry("600x500")
    app.title("Financial Sentiment Analysis")

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

    from_frame = CTkFrame(body, fg_color="transparent")
    from_frame.pack(pady=5, padx=10)
    
    from_label = CTkLabel(from_frame, text="From:")
    from_label.pack(side="left", padx=5)

    from_box = CTkComboBox(from_frame, 
                           values=dates, 
                           corner_radius=10)
    
    from_box.pack(pady=12,padx=10)

    to_frame = CTkFrame(body, fg_color="transparent")
    to_frame.pack(pady=5, padx=10)
    
    to_label = CTkLabel(to_frame, text="To:")
    to_label.pack(side="left", padx=5)

    to_box = CTkComboBox(to_frame, 
                        values=dates, 
                        corner_radius=10)
    
    to_box.pack(pady=12,padx=10)

    input = CTkEntry(master=body, placeholder_text="Enter the keyword here.")
    input.pack(pady=12,padx=10)

    btn = CTkButton(master=body, 
                    text="Submit", 
                    command=lambda: get_sentiment_analysis(app, body, from_box.get(), to_box.get(), input.get()))
    btn.pack()

    app.mainloop()

if __name__ == "__main__":
    main()
