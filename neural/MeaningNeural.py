"""нейронная сеть, многоклассовая классификация содержания ответа"""

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.src.datasets import reuters
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

class Animal():

    global model, x_train, y_train, x_val, y_val, vectorizer
    # Загрузка датасета
    dataframe = pd.read_csv("data/datasets/meaning.csv", names=['text', 'label'], sep=',', header=None, nrows=2000)
    dataframe = shuffle(dataframe)

    # Инициализация векторизатора
    vectorizer = CountVectorizer(binary=True)

    # Преобразование данных в бинарную матрицу
    x_train = vectorizer.fit_transform(dataframe['text']).toarray().astype('float32')
    y_train = np.asarray(dataframe['label']).astype('float32')
    # Разделение данных на тренинровочные и проверочные
    x_val = x_train[-1000:]
    y_val = y_train[-1000:]
    x_train = x_train[:-1000]
    y_train = y_train[:-1000]

    # Создание модели
    model = Sequential()
    model.add(Dense(16, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
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

class Category():
    (train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=1000)
    # кодирование
    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(10000,)))   #настроить входные нейроны на количество категорий
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='softmax'))  #вероятность пренадлежности к классу

    model.compile(
        optimizer='rmsprop',
        loss='categorial_crossentropy',
        metrics=['accuracy']
    )

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