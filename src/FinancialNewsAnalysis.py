from newscatcherapi import NewsCatcherApiClient
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


def save_articles_to_csv(articles, file_path):

    """
    Save the fetched news articles to a CSV file.

    Args:
        articles (list): List of news articles.
        file_path (str): File path to save the CSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the news articles.
    """
    df = pd.DataFrame(articles)
    df.to_csv(file_path, index=False)
    print(f"Saved articles to {file_path}")
    return df


def perform_sentiment_analysis(data, file_path):

    """
    Perform sentiment analysis on the news articles.

    Args:
        data (pandas.DataFrame): DataFrame containing the news articles.
        file_path (str): File path to save the DataFrame with sentiment scores.

    Returns:
        float: Mean negative sentiment score.
        float: Mean neutral sentiment score.
        float: Mean positive sentiment score.
    """
    analyzer = SentimentIntensityAnalyzer()
    negative = []
    neutral = []
    positive = []
    for i in range(data.shape[0]):
        title = data.iloc[i, 0]
        excerpt = data.iloc[i, 5]
        title_analyzed = analyzer.polarity_scores(title)
        desc_excerpt = analyzer.polarity_scores(excerpt)
        negative.append((title_analyzed['neg'] + desc_excerpt['neg']) / 2)
        neutral.append((title_analyzed['neu'] + desc_excerpt['neu']) / 2)
        positive.append((title_analyzed['pos'] + desc_excerpt['pos']) / 2)

    data['negative'] = negative
    data['neutral'] = neutral
    data['positive'] = positive

    data.to_csv(file_path)
    print(f"Saved articles with sentiment to {file_path}")
    return data['negative'].mean(), data['neutral'].mean(), data['positive'].mean()


def save_sentiment_pie_chart(negative_score, neutral_score, positive_score, file_path, q):
    """
    Save a pie chart visualizing the sentiment distribution.

    Args:
        negative_score (float): Mean negative sentiment score.
        neutral_score (float): Mean neutral sentiment score.
        positive_score (float): Mean positive sentiment score.
        file_path (str): File path to save the pie chart.
        query (str): Query used to fetch the news articles.
    """
    # Create a pie chart
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [positive_score, negative_score, neutral_score]
    colors = ['#55c0a7', '#f95d6a', '#f9d56a']
    explode = (0.1, 0, 0)  # Explode the positive slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title(f'Sentiment Distribution for {q}')

    # Save the pie chart
    plt.savefig(file_path)
    print(f"Saved pie chart to {file_path}")


class FinancialNewsAnalysis:
    def __init__(self, api_key):
        self.api = NewsCatcherApiClient(x_api_key=api_key)

    def fetch_articles(self, query, from_date, to_date, language='en', countries=None,
                       page_size=1000):
        """
                Fetch news articles based on the specified parameters.

                Args:
                    query (str): Query to search for news articles.
                    from_date (str): Start date for the news articles (format: YYYY/MM/DD).
                    to_date (str): End date for the news articles (format: YYYY/MM/DD).
                    language (str, optional): Language of the news articles (default: 'en').
                    countries (str or list, optional): Countries to filter the news articles (default: None).
                    page_size (int, optional): Number of articles to fetch per page (default: 1000).

                Returns:
                    dict: Dictionary containing the fetched news articles.
                """
        articles = self.api.get_search(
            q=query,
            from_=from_date,
            to_=to_date,
            lang=language,
            countries=countries,
            page_size=page_size
        )
        return articles['articles']
