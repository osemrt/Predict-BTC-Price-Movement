import numpy as np
import pandas as pd
from keras.layers import Dense, Dropout, LSTM, BatchNormalization
from keras.models import Sequential
from sklearn import preprocessing


def preprocess(dataframe, isTraining, predict_length, series_length):
    df = dataframe.copy()
    df["future_price"] = df['close'].shift(-predict_length)

    # Drop any NaN values
    df.dropna(inplace=True)

    # Compare future BTC price with today's price and labeling it as 1 if price increases and zero otherwise
    df["label"] = np.where(df["future_price"] >= df["close"], 1, 0)

    # Drop 'future_price' column as it is no longer required
    df.drop('future_price', 1, inplace=True)

    temp = df.loc[:, df.columns != 'label']

    cols = temp.columns
    scaler = preprocessing.StandardScaler()
    scaled_df = scaler.fit_transform(temp)
    temp = pd.DataFrame(scaled_df, columns=cols)

    sequence = []

    for i in range(len(temp) - series_length):
        sequence.append([np.array(temp[i:i + series_length]), df.iloc[i + series_length, -1]])

    X = []
    y = []

    increases = []
    decreases = []

    for seq, label in sequence:
        if label == 0:
            decreases.append([seq, label])
        else:
            increases.append([seq, label])

    len_increases = len(increases)
    len_decreases = len(decreases)

    if isTraining:
        if (len_increases < len_decreases):
            increases = increases[:len_increases]
            decreases = decreases[:len_increases]
        else:
            increases = increases[:len_decreases]
            decreases = decreases[:len_decreases]

    sequence = increases + decreases

    if isTraining:
        np.random.shuffle(sequence)

    for seq, label in sequence:
        X.append(seq)
        y.append(label)

    return np.array(X), np.array(y)


def create_model(shape):
    model = Sequential()
    model.add(LSTM(256, input_shape=(shape), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(LSTM(256, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(LSTM(256, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(2, activation='softmax'))

    return model


def update_balance(balance, change):
    price_change = (balance * change) / 100
    balance += price_change
    return balance
