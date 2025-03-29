# Financial Sentiment Analysis 💰📈💵

## 📝 Description

This project is a financial sentiment analysis tool that uses a pretrained model called FinBERT to analyze the sentiment of financial news. FinBERT is a pre-trained NLP model to analyze sentiment of financial text. It is built by further training the BERT language model in the finance domain, using a large financial corpus and thereby fine-tuning it for financial sentiment classification.

## 📂 Project Structure

```bash
financial-sentiment-analysis/
│-- images/                 # Images for the Interface
│-- src/
│   ├── app.py              # Entry point, UI rendering (Customtkinter)
│   ├── config.py           # Configuration settings (keys, properties, paths)
│   ├── model.py            # FinBERT model, with functions to extract news information and predict the TARGET
│   ├── utils.py            # Utility functions to serve different components
│-- themes/                 # UI theme
│-- example.pdf             # Use case of the app
│-- README.md               # Project documentation
│-- requirements.txt        # Project needed requirements
```

## ⚙️ Installation

### Clone the repository:
```bash
git clone https://github.com/matisanchz/financial-sentiment-analysis.git
```
#### Go to the folder:
```bash
cd financial-sentiment-analysis
```
### Install dependencies:
```bash
pip install -r requirements.txt
```

**IMPORTANT:** Set up environment variables in a .env file.

The .env file contains important information about the API KEYS. To run the project, you must define:

* NEWS_API_KEY='' -> To connect with the API to extract news base on parameters.

### Run the application:
```bash
python .\src\app.py
```

## 📚 Usage

The user must provide three inputs:

- "Date From"
- "Date To"
- "Keyword": This keyword will be sent to the News API to retrieve the most relevant news related to the context.

If the user does not provide a keyword, or if the "Date To" is earlier than "Date From," they will receive a validation message.

## ✅ Example:

In the example.pdf you will see a simple use case of the sentiment analysis.