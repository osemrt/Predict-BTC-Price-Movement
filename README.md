# The Influence of News on Bitcoin Price

### Project Description
It is obvious that media news, becoming the most important everyday source of life information, is a decision-making tool for traders, investors and markets. Cryptocurrencies have received lots of media attention, which is due to their low transaction costs, peer-to-peer system and governmental free design. That has contributed to a rise in trading volume, volatility and price of cryptocurrencies, with cryptocurrencies regularly in the mainstream news. In terms of trading volume among cryptocurrencies, Bitcoin is the most popular cryptocurrency and is a peer-to-peer electronic cash system which allows online payments to be sent directly from one party to another without going through a financial institution. Therefore unlike the vast majority of other financial assets, Bitcoin have no association with any higher authority, such as a government, firm, country or commodity. The relation between the price movement of Bitcoin and knowledge in the form of news is clear but complicated. The arrival of news at every moment changes the perception or sentiment towards Bitcoin. Now, thanks to the bliss of the internet, the traders, and investors have constant access to the updated news, and the news constantly molds their sentiments and influences their decision to invest in Bitcoin. In this project, we will build a system to show whether bitcoin-related news articles will cause an apparent Bitcoin price increase or decrease to help Bitcoin players to make a more reasonable decision on selling or buying Bitcoin

In this project, we investigate the influence of the news articles on bitcoin prices to reveal the relation between the news articles and the price changes. We scrape the relevant news headlines and bitcoin historical data. We apply sentiment analysis to each collected headline to get the polarity and subjectivity scores. We then combine the polarity and subjectivity scores with the historical price data and further train a prediction model based on LSTM with this combined data to predict the price movement.

### Problem Statement
A cryptocurrency exchange allows customers to trade cryptocurrencies or digital currencies for other assets such as conventional fiat money or other digital currencies. The change in the prices has some predictive relationships with the publicly available news of present and historical stock market prices. 

The investors or traders decide the better time to sell/buy/hold a cryptocurrency in the market based on the past relationship. In this project, we will learn the possibility of devising a model, which will predict the next BTC price movements with a lower percentage of error, using novel machine learning techniques to help BTC players. 

Accuracy plays a vital role in stock price movement prediction. Although many algorithms are available for this purpose, selecting the most accurate one continues to be the fundamental task in getting the best results. This involves training the model several times, and executing it, getting the model results, then comparing multiple performance parameters of the model, and finally obtaining the most accurate one.

### Dataset
There are two datasets that we utilized in this project: historical bitcoin price and bitcoin-related news headline. For the news headlines, we utilize a WebDriver to collect bitcoin-related news metadata from various news aggregators. We chose only bitcoin-related news because we hypothesized that articles from this section would be most related to BTC price change. We then wrote a Python web scraper to harvest 17,047 news headlines.

<img src="https://github.com/image-assets/png/blob/master/prediction-btc-movements-dataset_news_headlines.png" width="700" />

Our job was easy for the historical price data; we downloaded the daily price data from around 2013 to 2020 for Dollar-BTC on coinmarketcap.com.

<img src="https://github.com/image-assets/png/blob/master/prediction-btc-movements-dataset_historical_price.png" width="700" />

### Preprocessing
Data preprocessing is a part of data mining, which involves transforming raw data into a more consistent format. Raw data is usually inconsistent or incomplete and often contains many errors. In this section, we explain the applied preprocessing steps to the historical prices and news headlines. 

News preprocessing steps are respectively: 
- converting all letters to lowercase. (e.g. News becomes news) 
- replacing contractions with their longer forms (e.g. wasn’t becomes was not) 
- removing stop words in English 

Historical data preprocessing step is: 
- max-min scaling


### System Architecture
In the system, we have proposed a model to predict BTC price movement using news sentiment and historical prices. We assumed the positive stream of stock information is to simulate buying and increase the stock prices, and the negative stream of stock information is assumed to result in selling and decrease the stock prices. The general schema of the system is illustrated in the following figure.

<img src="https://github.com/image-assets/png/blob/master/prediction-btc-movements-sentiment-lstm-schema.png" width="650" />

Gathering the datasets and their preprocessing steps have already been described in the previous sections. For all news headlines for a specific day are concatenated and applied sentiment analysis for each of them to compute the polarity and subjectivity scores. Then, polarity and subjectivity scores combined with preprocessed historical data. In this stage, the dataset will looks like in the following figure.

<img src="https://github.com/image-assets/png/blob/master/prediction-btc-movements-dataset_combined.png" width="700" />

After getting combined data, we have applied feature selection using WEKA to find the best subset of features, which will give the best accuracy. 

Before starting the training, we need to define:
- a ***prediction length*** to get the price movements. If the prediction length is 3, the close prices are shifted three times above, and shifted close prices are added as ’future price’ column to the dataset, and NaN rows removed from it. Then, for each day, feature close prices are substracted from close prices. If the result is greater than zero, the price movement for that day will be one; otherwise, it becomes zero.
- a ***sequence length*** for LSTM inputs. We always have to give a three-dimensional array as an input to your LSTM networks. Where the first dimension represents the batch size, the second dimension represents the time-steps and the third dimension represents the number of units in one input sequence. If we choose the sequence length as 30, each LSTM input samples contains the current features plus the past 29 sample features.

### Prediction Model
The applied model in the above system consists of a stacked LSTM of three layers. We have applied a stacked LSTM over selected features, in stacked LSTMs, each LSTM layer outputs a sequence of vectors which will be used as an input to a subsequent LSTM layer. This hierarchy of hidden layers enables more complex representation of our time-series data, capturing information at different scales. The model can also be seen in the following figure.

<img src="https://github.com/image-assets/png/blob/master/sentiment-lstm-model.png" width="700" />

### Market Simulation
To show how the model we have proposed are delivering results in practice, we have developed a Windows application. This program simulates bitcoin trading according to the model predictions. If the prediction indicates that the price will increase for the next day, the program buy bitcoin with all its money and applies the price change to the balance, otherwise it holds its current state.

<img src="https://github.com/image-assets/png/blob/master/prediction-btc-movements-application.png" width="600" />

The user first starting uploading the datasets and then deposits some money. For experience purposes, we have deposited $1000 and then uploaded the datasets of the model which is tuned and trained according to the experiment results in the previous section.

<img src="https://github.com/image-assets/png/blob/master/prediction-btc-movements-results.png" width="600" />

In the price range we examined for the test, even though the price of bitcoin lost huge value, our model saved more than 50% of the price loss that could occur without using the model, knowing 64% of all possible movements. 

### Conclusion

Many traders rely on news services as their major information source when they make a more reasonable decision on selling or buying bitcoin. However, the increasing amount of up-to-date textual information leads to a substantial information overload, making it harder for market participants to select the information relevant to them. Therefore, in this project we implemented a system that predicts bitcoin price movements using the subjectivity and polarity of the bitcoin-related news headlines and historical price data. 

First the relevant news headlines and bitcoin historical data have been scraped from cointelegraph and coinmarketcap respectively, and then we applied sentiment analysis to each collected headline to get the polarity and subjectivity scores. In order to find correlation between the bitcoin news and price movements and to test efficient market hypothesis, we trained our model. We acquired 66% accuracy from our best model. This accuracy rate is greater than random prediction, which has 50% accuracy. These results argue that there is a relationship between financial news and stock price movements. 

Although the accuracy level of the model is satisfactory, it can further be developed by incorporating more complex classifiers. In this project, we only considered the impact of the news articles to the bitcoin price movement. To increase prediction accuracy, other public information sources like social media, users comments in the forums can be included. Then, the optimization step for this project is based on experiments, grid search and re-factory. A more advanced optimization approach can be researched in the future. 

Also, the future scope of the project can be varied. Using the proposed system, we can do several financial modeling like portfolio management, risk estimation models, and several other strategic modeling etc. where perception plays an important role.

### Acknowledgments
I would like to thank my supervisor Assoc. Prof. Mine Elif KARSLIGIL YAVUZ for her support and advice throughout this project. Thanks also to the lecturers and staff of YTU. And finally to my family and friends for their ongoing support.
