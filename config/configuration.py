from configparser import ConfigParser

config = ConfigParser()

config["NEWS_PARAMETERS"] = {
    "API_KEY": "xyx2fDIhdOhUob7uu40W018GVstAOiTB3f-iGZRAXt0",
    "QUERY": "adani",
    "FROM": "2023/7/6",
    "TO": "2023/7/7",
    "LANGUAGE": "en",
    "COUNTRIES": "IN"
}
config["PATH"] = {
    "ARTICLE_PATH": "./output/article.csv",
    "SENTIMENT_ARTICLE_PATH": "./output/sentiment_article_path.csv",
    "PIE_CHART_PATH": "./output/pie_chart.jpg"
}

with open("config.yaml", "w") as f:
    config.write(f)
