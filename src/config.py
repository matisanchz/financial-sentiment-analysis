from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

root = Path(__file__).parent.parent

class Settings():

    IMAGE_FOLDER: Optional[str] = f"{root}\\images\\"

    POSITIVE_IMAGE: Optional[str] = IMAGE_FOLDER+"positive.png"
    NEGATIVE_IMAGE: Optional[str] = IMAGE_FOLDER+"negative.png"
    NEUTRAL_IMAGE: Optional[str] = IMAGE_FOLDER+"neutral.png"
    
    def get_news_api_url(keyword, date_from, date_to):
        return ('https://newsapi.org/v2/everything?'
               f'q={keyword}&'
               f'from={date_from}&'
               f'to={date_to}&'
               'sortBy=popularity&'
               f'apiKey={os.getenv("NEWS_API_KEY")}'
        )
    

    