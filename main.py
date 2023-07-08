from src.FinancialNewsAnalysis import FinancialNewsAnalysis, save_articles_to_csv
from src.FinancialNewsAnalysis import perform_sentiment_analysis, save_sentiment_pie_chart
from configparser import ConfigParser

config = ConfigParser()
config.read("./config/config.yaml")

config_param = config["NEWS_PARAMETERS"]
config_path = config["PATH"]
api = config_param["api_key"]
q = config_param["query"]
news_from = config_param["from"]
news_to = config_param["to"]
lang = config_param["language"]
countries = config_param["countries"]

news_article_path = config_path["article_path"]
sentiment_article_path = config_path["sentiment_article_path"]
pie_chart_path = config_path["pie_chart_path"]

if __name__ == '__main__':
    news = FinancialNewsAnalysis(api_key=api)
    article = save_articles_to_csv(news.fetch_articles(q, news_from, news_to, lang, countries), news_article_path)
    negative_score, neutral_score, positive_score = perform_sentiment_analysis(article, sentiment_article_path)
    save_sentiment_pie_chart(negative_score, neutral_score, positive_score, pie_chart_path, q)
