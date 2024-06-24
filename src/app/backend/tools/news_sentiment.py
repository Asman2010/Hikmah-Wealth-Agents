from gnews import GNews
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
from crewai_tools import tool


def sentiment_analyzer(titles):
    """
    Performs sentiment analysis on a list of titles using the FinBERT model.

    Args:
        titles (list): A list of news article titles.

    Returns:
        list: A list of tuples containing the sentiment label and confidence score for each title.
    """
    finbert = BertForSequenceClassification.from_pretrained(
        'yiyanghkust/finbert-tone', num_labels=3
    )
    tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
    nlp = pipeline("sentiment-analysis", model=finbert, tokenizer=tokenizer)
    results = nlp(titles)
    return [(result['label'], result['score']) for result in results]


@tool("Fetch Company News And Perfrom Sentiment Analysis")
def news_analysis(company: str):
    """
    Fetches the latest news articles for a given company and performs sentiment analysis on their titles.

    Args:
        company (str): The name of the company to fetch news for.

    Returns:
        list: A list of lists containing the title, date, URL, sentiment label, and
        confidence score for each news article.
    """
    google_news = GNews(language='en', country='IN', period='7d', max_results=20)
    news = google_news.get_news(company)
    titles = [article['title'] for article in news]
    labels_scores = sentiment_analyzer(titles)
    news_data = [[article['title'], article['published date'], label, score] for article,
                 (label, score) in zip(news, labels_scores)]
    
    return news_data
