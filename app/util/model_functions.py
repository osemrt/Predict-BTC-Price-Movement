import pandas as pd
import numpy as np

from keras.models import load_model

CNN_LSTM = 3
SENTIMENT_LSTM = 4

CNN_LSTM_MODEL_PATH = "../models/cnn-lstm/cnn-lstm.h5"
SENTIMENT_LSTM_MODEL_PATH = "../models/sentiment-lstm/sentiment-lstm.h5"
HISTORICAL_DATASET_PATH = "../models/sentiment-lstm/combined_data.csv"

TEST_SIZE = 0.3


def get_model(model_id):
    if model_id == CNN_LSTM:
        return load_model(CNN_LSTM_MODEL_PATH)
    else:
        return load_model(SENTIMENT_LSTM_MODEL_PATH)


def get_predictions(model, x_test_path, model_id):
    if model_id == CNN_LSTM:
        X_test = np.loadtxt(x_test_path, delimiter=',')

        predictions = model.predict(X_test)
        return predictions.round()
    else:
        X_test = np.loadtxt(x_test_path, delimiter=',')
        X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

        predictions = model.predict(X_test, verbose=1)
        return predictions.round()

def get_actual_y(y_test_path):

    return 0

def get_price_data():
    df_histoical = pd.read_csv(HISTORICAL_DATASET_PATH)
    row_count = df_histoical.shape[0]
    start = round(row_count * (1 - TEST_SIZE))
    total = len(df_histoical.values[start - 1:row_count])
    return df_histoical.values[start:row_count], total
