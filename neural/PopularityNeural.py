"""наивный байес, категоризация популярного ответа"""

import pandas as pd
from sklearn.naive_bayes import MultinomialNB, ComplementNB
from sklearn.feature_extraction.text import CountVectorizer

class PopularityNeural():
    global data, labels, texts, vectorizer, clf, x_train
    global train_data
    data= pd.read_csv('data/datasets/popularity.csv', sep=';', names=['label', 'text'], encoding='cp1251')    # Dataset по категориям
    train_data = pd.read_csv('data/datasets/test-popular.csv', sep=';', names=['label', 'text'],
                             encoding='cp1251')  # Dataset по категориям

    labels = data['label']
    texts = data['text']
    # Инициализация векторизатора
    vectorizer = CountVectorizer()
    # Преобразование текста в числовые векторы
    x_train = vectorizer.fit_transform(texts)
    # Инициализация наивного байеса
    clf = ComplementNB(alpha=0.1)
    # Обучение
    clf.fit(x_train, labels)

    @staticmethod
    def isPopular(inputTxt):
        # Определение категории введённого текста
        x_test = vectorizer.transform([inputTxt])
        result = clf.predict(x_test)[0]
        predicted_probabilities = clf.predict_proba(x_test)[0]

        if max(predicted_probabilities) > 0.2:
            return result
        return "другое"