import pandas as pd
import numpy as np

from keras.models import load_model

from config.variables import CNN_LSTM, SENTIMENT_LSTM
from config.variables import CNN_LSTM_MODEL_PATH, SENTIMENT_LSTM_MODEL_PATH
from config.variables import SENTIMENT_LSTM
from config.variables import HISTORICAL_DATASET_PATH


def get_model(model_id):
    if model_id == CNN_LSTM:
        return load_model(CNN_LSTM_MODEL_PATH)
    else:
        return load_model(SENTIMENT_LSTM_MODEL_PATH)


def get_predictions(model, x_test_path, model_id):
    if model_id == CNN_LSTM:
        X_test = np.loadtxt(x_test_path, delimiter=',')
        predictions = model.predict(X_test, verbose=1)
        #
        abc = np.loadtxt(
            "D:/CS/workspace/Projects/predict-btc-price-movement/models/cnn-lstm/train_and_test/y_test.txt",
            delimiter=',')
        score, acc = model.evaluate(X_test, abc, batch_size=2048)
        print('Test score:', score)
        print('Test accuracy:', acc)
        #

        return predictions.round()
    else:
        X_test = np.loadtxt(x_test_path, delimiter=',')
        X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))
        predictions = model.predict(X_test, verbose=1)

        #
        abc = np.loadtxt(
            "D:/CS/workspace/Projects/predict-btc-price-movement/models/sentiment-lstm/train_and_test/y_test.txt",
            delimiter=',')
        score, acc = model.evaluate(X_test, abc, batch_size=2048)
        print('Test score:', score)
        print('Test accuracy:', acc)

        np.savetxt('./predictions.txt', predictions, delimiter=',')
        #
        return predictions.round()


def get_price_data(model_id):
    df_histoical = pd.read_csv(HISTORICAL_DATASET_PATH)
    if model_id == SENTIMENT_LSTM:
        TEST_SIZE = 0.3
        row_count = df_histoical.shape[0]
        start = round(row_count * (1 - TEST_SIZE))
        total = len(df_histoical.values[start - 1:row_count])
        print("start:" + str(start) + " end:" + str(row_count))
        return df_histoical.values[start - 1:row_count], total
    else:
        print(df_histoical.shape)
        df_histoical.sort_values('date', ascending=False, inplace=True)
        TEST_SIZE = 0.2
    row_count = df_histoical.shape[0]
    start = round(row_count * (1 - TEST_SIZE))
    total = len(df_histoical.values[start - 1:row_count])
    print("start:" + str(start) + " end:" + str(row_count))
    return df_histoical.values[start - 1:row_count], total


def init_model(self):
    if self.radioButton_CNNLSTM.isChecked():
        model = get_model(self.CNN_LSTM)
        self.predictions = get_predictions(model, self.x_test_path, self.CNN_LSTM)
        # self.actual_movements = pd.read_csv(self.y_test_path).values
        self.actual_movements = np.loadtxt(self.y_test_path, delimiter=',')
        self.price_data, self.total = get_price_data(self.CNN_LSTM)
        self.last = self.price_data.shape[0] -1
    else:
        model = get_model(self.SENTIMENT_LSTM)
        self.predictions = get_predictions(model, self.x_test_path, self.SENTIMENT_LSTM)
        # self.actual_movements = pd.read_csv(self.y_test_path).values
        self.actual_movements = np.loadtxt(self.y_test_path, delimiter=',')
        self.price_data, self.total = get_price_data(self.SENTIMENT_LSTM)
        self.last = self.price_data.shape[0]
