# Financial News Analysis

Perform sentiment analysis on financial news articles using NewsCatcher API and VADER sentiment analysis.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Obtaining the API Key](#obtaining-the-api-key)
- [Acknowledgements](#acknowledgements)
## Introduction

The Financial News Analysis project fetches financial news articles using the NewsCatcher API based on specified parameters such as query, date range, language, and countries. It performs sentiment analysis on the articles using VADER (Valence Aware Dictionary and Sentiment Reasoner) sentiment analysis tool. The sentiment analysis results are saved to a CSV file, and a pie chart visualization of the sentiment distribution is generated and saved as an image.

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/prabhattiwari16/Financial_News_Sentiment.git
  ```
2. Change to the project directory:
```bash
      cd financial-news-analysis
  ```
3. Install the required dependencies:
```bash
    pip install -r requirements.txt
```
4. Set up the configuration:
   Open the config/configuration.py file and update the API key and other parameters as needed.

## Usage
1. Run the config/configuration.py and main.py script:
```bash
  python config/configuration.py 
  python main.py
```
This will fetch the financial news articles based on the specified parameters, perform sentiment analysis, and save the results to CSV.

2. Check the output:
- The news articles will be saved to a CSV file specified in the configuration.
- The sentiment analysis results will be saved to a separate CSV file specified in the configuration.
- A pie chart visualization of the sentiment distribution will be saved as an image file specified in the configuration.

## Configuration
The configuration for the Financial News Analysis project is stored in the config/config.yaml file. It includes the following parameters:

- `api_key`: The API key for the NewsCatcher API.
- `query`: The query used to fetch the financial news articles.
- `from`: The start date for the news articles in the format YYYY/MM/DD.
- `to`: The end date for the news articles in the format YYYY/MM/DD.
- `language`: The language of the news articles.
- `countries`: The countries to filter the news articles.

## Obtaining the API Key

To use the NewsCatcher API, you need to obtain an API key. Visit the [NewsCatcher API website](https://newscatcherapi.com) to sign up and get your API key.

## Acknowledgements

We would like to acknowledge the following resources and projects that have contributed to this project:

- NewsCatcher API: The API service used to fetch financial news articles.
- VADER Sentiment Analysis: The Python library used for sentiment analysis.