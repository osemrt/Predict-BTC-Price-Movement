import json

import matplotlib.pyplot as plt
import pandas as pd


def load_pet(filename):
    with open(filename) as f:
        pet = json.loads(f.read())
    return pet


def plot_movements(df_data):
    movements = load_pet('LSTM-Sentiment_movements.json')

    date = df_data['date'].values
    close = df_data['close'].values
    plt.figure(figsize=(15, 11))
    for x1, x2, y1, y2 in zip(date, date[1:], close, close[1:]):
        if movements[x1]:
            plt.plot([x1, x2], [y1, y2], 'g')
        else:
            plt.plot([x1, x2], [y1, y2], 'r')

    plt.plot(x1, y1, "-g", label="True Predicted Movement")
    plt.plot(x2, y2, "-r", label="False Predicted Movement")
    plt.legend(loc="upper right")
    plt.title('Sentiment-LSTM Movements')
    plt.xlabel('date')
    plt.xticks(rotation='vertical')
    plt.ylabel('Bitcoin Price in Dollars')
    plt.savefig('img/movements.png')
