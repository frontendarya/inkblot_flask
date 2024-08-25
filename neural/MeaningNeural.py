"""нейронная сеть, многоклассовая классификация содержания ответа"""

import pandas as pd
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from keras.src.datasets import reuters
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import pathlib
from pathlib import Path

class Meaning():
    # answers;H;(H);(Hd);A;(A);Ad;At;Sex;Obj;Aobj;Aat;Food;N;Geo;Pi;Arch;Art;Abs;Bi;Ti;Ci
    # answers;1;(h);1;a;(a);ad;at;sex;obj;aobj;aat;food;n;geo;pi;arch;art;abs;bi;ti;ci;

    # Загрузка датасета
    dataframe = pd.read_csv("C:/Users/ASUS-DARYA/PycharmProjects/inkblot_flask/data/datasets/dataset.csv",
                            names=['answers','H','(H)','(Hd)','A','(A)','Ad','At','Sex','Obj','Aat','Food','N','Geo','Pi','Arch','Art','Abs','Bi','Ti','Ci'],
                            sep=';',
                            header=None,
                            nrows=1659,
                            encoding='utf-8')
    # dataframe.drop(dataframe.columns[0], axis=1, inplace=True)
    dataframe = dataframe.fillna('0').astype(int, errors='ignore')

    print(dataframe)
    dataframe = shuffle(dataframe)
    # y_dataframe = dataframe.drop('answers')

    # Инициализация векторизатора
    vectorizer = CountVectorizer(binary=True)

    # Преобразование данных в бинарную матрицу
    x_train = vectorizer.fit_transform(dataframe['answers']).toarray().astype('string')
    y_train = np.asarray(y_dataframe).astype('float32')
    # Разделение данных на тренинровочные и проверочные
    x_val = x_train[-800:]
    y_val = y_train[-800:]
    x_train = x_train[:-800]
    y_train = y_train[:-800]

    # Создание модели
    model = Sequential()
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(20, activation='sigmoid'))
    # Компиляция модели
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['acc'])

    # Обучение модели
    result = model.fit(x_train, y_train, epochs=24, batch_size=64, validation_data=(x_val, y_val))

    @staticmethod
    def isAnimal(inputTxt):
        new_data = pd.Series([str(inputTxt)])
        new_binary_matrix = vectorizer.transform(new_data).toarray()
        prediction = model.predict(new_binary_matrix)
        result_label = np.where(prediction > 0.5, 1, 0)
        if result_label == [[0]]:
            return 0
        elif result_label == [[1]]:
            return 1

# class Category():
#     from preprocessing.text import Tokenizer
#     from preprocessing.sequence import pad_sequences
#     from tensorflow.python.keras.models import Sequential
#     from tensorflow.python.keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
#     from sklearn.model_selection import train_test_split
#
#     # Подготовка данных
#     max_fatures = 2000
#     tokenizer = Tokenizer(num_words=max_fatures, split=' ')
#     tokenizer.fit_on_texts(df['Text'].values)
#     X = tokenizer.texts_to_sequences(df['Text'].values)
#     X = pad_sequences(X)
#
#     # Создание модели
#     embed_dim = 128
#     lstm_out = 196
#
#     model = Sequential()
#     model.add(Embedding(max_fatures, embed_dim, input_length=X.shape[1]))
#     model.add(SpatialDropout1D(0.4))
#     model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
#     model.add(Dense(2, activation='softmax'))
#     model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#
#     # Деление данных на обучающую и тестовую выборки
#     Y = pd.get_dummies(df['Category']).values
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
#
#     # Обучение модели
#     batch_size = 32
#     model.fit(X_train, Y_train, epochs=7, batch_size=batch_size, verbose=2)
#
#     (train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=1000)
#     # кодирование
#     model = Sequential()
#     model.add(Dense(64, activation='relu', input_shape=(10000,)))   #настроить входные нейроны на количество категорий
#     model.add(Dense(64, activation='relu'))
#     model.add(Dense(64, activation='softmax'))  #вероятность пренадлежности к классу
#
#     model.compile(
#         optimizer='rmsprop',
#         loss='categorial_crossentropy',
#         metrics=['accuracy']
#     )



    # result_dict = result.history
    # loss = result_dict['loss']
    # val_loss = result_dict['val_loss']
    # epochs = range(1, len(result_dict['acc']) + 1)
    #
    # plt.plot(epochs, loss, 'bo', label='Потери при обучении')
    # plt.plot(epochs, val_loss, 'b', label='Потери при проверке')
    # plt.xlabel('Эпохи')
    # plt.ylabel('Потери')
    # plt.legend()
    # plt.show()
    #
    # plt.clf()
    # acc = result_dict['acc']
    # val_acc = result_dict['val_acc']
    #
    # plt.plot(epochs, acc, 'bo', label='Точность при обучении')
    # plt.plot(epochs, val_acc, 'b', label='Точность при проверке')
    # plt.xlabel('Эпохи')
    # plt.ylabel('Потери')
    # plt.legend()
    # plt.show()