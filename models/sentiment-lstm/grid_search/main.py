import csv
from datetime import datetime

import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta

from model_functions import create_model
from model_functions import preprocess
from model_functions import update_balance

#######################################
csvfile = open('results.csv', 'w', newline='')
writer = csv.writer(csvfile)
header = [
    'training_period',
    'test_period',
    'series_length',
    'predict_length',
    'training_start',
    'training_end',
    'test_start',
    'test_end',
    'test_score',
    'test_accuracy',
    'initial_BTC_price',
    'last_BTC_price',
    'total_balance_with_model',
    'total_balance_without_model',
    'average_daily_profit_with_model',
    'average_daily_profit_without_model'
]

writer.writerow(header)

#######################################


batch_size = 32
epochs = 100

start_date = '2018-05-01'
end_date = '2019-12-31'
dataset_period = 20

selected_features = ['filtered_polarity', 'subjectivity', 'open', 'close', 'high', 'low', 'volume', 'market_cap']

dt_start_date = datetime.strptime(start_date, '%Y-%m-%d')

df_data = pd.read_csv('./../combined_data.csv')
df_data = df_data[(df_data.date >= start_date) & (df_data.date <= end_date)]

training_periods = [6, 12, 18]
series_lengths = [7, 15, 30]
predict_lengths = [1, 3, 7]
test_period = 1

for training_period in training_periods:
    for series_length in series_lengths:
        for predict_length in predict_lengths:
            for k in range(dataset_period - (training_period + test_period) + 1):
                dt_training_start = dt_start_date + relativedelta(months=k)
                dt_test_start = dt_training_start + relativedelta(months=training_period)

                dt_training_end = dt_test_start + relativedelta(days=-1)
                dt_test_end = dt_training_end + relativedelta(months=test_period)

                str_training_start = "{:%Y-%m-%d}".format(dt_training_start)
                str_training_end = "{:%Y-%m-%d}".format(dt_training_end)

                str_test_start = "{:%Y-%m-%d}".format(dt_test_start)
                str_test_end = "{:%Y-%m-%d}".format(dt_test_end)

                df_train = df_data[(df_data.date >= str_training_start) & (df_data.date <= str_training_end)]
                df_test = df_data[(df_data.date >= str_test_start) & (df_data.date <= str_test_end)]
                df_train_test = pd.concat([df_train, df_test])

                df_test_for_sequence = df_train_test[len(df_train_test) - len(df_test) - series_length:]

                X_train, y_train = preprocess(df_train[selected_features], True, predict_length, series_length)
                X_test, y_test = preprocess(df_test_for_sequence[selected_features], False, predict_length,
                                            series_length)

                model = create_model(X_train.shape[1:])

                model.compile(loss='sparse_categorical_crossentropy', optimizer="adam", metrics=['accuracy'])

                history = model.fit(X_train,
                                    y_train,
                                    batch_size=batch_size,
                                    epochs=epochs,
                                    verbose=False,
                                    validation_split=0.1)

                test_score, test_accuracy = model.evaluate(X_test, y_test, batch_size=batch_size)
                test_score = round(test_score, 2)
                test_accuracy = round(test_accuracy, 2)

                predictions = model.predict(X_test, verbose=1)
                predictions = np.argmax(predictions, axis=-1)

                ############

                DATE_COLUMN = 0
                CHANGE_COLUMN = 9
                OPEN_COLUMN = 5
                CLOSE_COLUMN = 6

                DECREASE = 0
                INCREASE = 1

                trueCount = 0

                initial_balance = 1000
                current_balance = initial_balance

                initial_BTC_price = df_test.iloc[0, OPEN_COLUMN]
                last_BTC_price = df_test.iloc[len(predictions), CLOSE_COLUMN]

                for i in range(len(predictions)):
                    # Date and Percent change
                    DATE = df_test.iloc[i, DATE_COLUMN]
                    CHANGE = df_test.iloc[i, CHANGE_COLUMN]

                    # Price movement
                    if CHANGE > 0:
                        ACUTAL_MOVEMENT = INCREASE
                    else:
                        ACUTAL_MOVEMENT = DECREASE

                    before_balance = current_balance

                    # Movement prediction
                    if predictions[i] == 1:
                        CURRENT_MOVEMENT_PREDICTION = INCREASE
                        current_balance = update_balance(current_balance, CHANGE)
                    else:
                        CURRENT_MOVEMENT_PREDICTION = DECREASE

                    after_balance = current_balance

                    if CURRENT_MOVEMENT_PREDICTION == ACUTAL_MOVEMENT:
                        trueCount += 1

                btc_amount = initial_balance / initial_BTC_price
                current_money = btc_amount * last_BTC_price

                total_balance_with_model = round(current_balance - initial_balance, 2)
                total_balance_without_model = round(current_money - initial_balance, 2)

                average_daily_profit_with_model = round((current_balance - initial_balance) / len(predictions), 2)
                average_daily_profit_without_model = round((current_money - initial_balance) / len(predictions), 2)

                row = [
                    training_period,
                    test_period,
                    series_length,
                    predict_length,
                    str_training_start,
                    str_training_end,
                    str_test_start,
                    str_test_end,
                    test_score,
                    test_accuracy,
                    initial_BTC_price,
                    last_BTC_price,
                    total_balance_with_model,
                    total_balance_without_model,
                    average_daily_profit_with_model,
                    average_daily_profit_without_model
                ]

                writer.writerow(row)
                print(row)

csvfile.close()
