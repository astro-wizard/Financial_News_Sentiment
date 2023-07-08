from newscatcherapi import NewsCatcherApiClient
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


def save_articles_to_csv(articles, file_path):
    df = pd.DataFrame(articles)
    df.to_csv(file_path, index=False)
    print(f"Saved articles to {file_path}")
    return df


def perform_sentiment_analysis(data, file_path):
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
        articles = self.api.get_search(
            q=query,
            from_=from_date,
            to_=to_date,
            lang=language,
            countries=countries,
            page_size=page_size
        )
        return articles['articles']
