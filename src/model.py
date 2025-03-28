from transformers import pipeline
from config import Settings
import requests

class FinbertModel():

    def __init__(self):
        self.pipe = pipeline("text-classification", model="ProsusAI/finbert")

    def get_sentiment(self, keyword, date_from, date_to):
        news_api_url = Settings.get_news_api_url(keyword, date_from, date_to)

        response = requests.get(news_api_url)

        articles = response.json()['articles']
        articles = [article for article in articles if keyword.lower() in article['title'].lower() or keyword.lower() in article['description'].lower()]

        total_score = 0
        num_positive_articles = 0
        num_negative_articles = 0
        num_neutral_articles = 0

        for i, article in enumerate(articles):
            print(f'Title: {article["title"]}')
            print(f'Link: {article["url"]}')
            print(f'Description: {article["description"]}')

            sentiment = self.pipe(article["content"])[0]

            print(f'Sentiment {sentiment["label"]}, Score: {sentiment["score"]}')
            print('-'*40)

            sentiment_label = sentiment['label']
            sentiment_score = sentiment['score']

            if sentiment_label == 'positive':
                total_score += sentiment_score
                num_positive_articles += 1
            elif sentiment_label == 'negative':
                total_score -= sentiment_score
                num_negative_articles += 1
            else:
                num_neutral_articles += 1
        
        final_score = total_score / (num_positive_articles+num_negative_articles)

        result = "Neutral"

        if final_score >= 0.15:
            result = "Positive"
        elif final_score <= -0.15:
            result = "Negative"
    
        return num_positive_articles, num_negative_articles, num_neutral_articles, result, final_score

