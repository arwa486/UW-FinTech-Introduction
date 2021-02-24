# Homework 12

## Sentiment Analysis of Bitcoin, Ethereum News 

The sentiment for both Bitcoin and Ethereum is mostly positive (0.909, 0.943 respectively.) The standard deviation for the Bitcoin and Ethereum from the dataset is 8% and 6% respectively. While Ethereum has slightly more positive news (3% higher mean) and less variance (6% standard deviation), the means and standard deviation overlap, which suggest that the news for both cryptocurrencies are positively correlated. 

Two caveats to my conclusion are that the datasets are small (18 articles for Bitcoin and 20 articles for Ethereum) and the articles are relatively recent (within the last month.) This is a limitation of the "free tier" API service from NewsAPI. The small size of the datasets indicates that the sentiment statistics are not  representative of the news articles written on cryptocurrencies. The bias of recent articles in the "free tier" also skews the results as Bitcoin and Ethereum have had a phenomenal rally over the last three months. 

Future work could be done to create a sentiment tool that is "weighted"(e.g. "clustering" news articles by date and frequency and weighting on the cluster size.) This could "balance" or "skew" the statistical analysis and create a "weighted moving average" of sentiment for news.