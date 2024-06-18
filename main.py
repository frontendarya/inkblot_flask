"""Основная логика работы приложения,
Подсчёт ответов,
Интерпретация результатов"""
import pandas as pd
class Main():
    def __init__(self):
        super(Main, self).__init__()
        self.answers_counter = 0  # счётчик общего числа ответов
        self.rejection_counter = 0  # счётчик общего отказов
        # Форма
        self.scoreW = 0;  # целое изображение
        self.scoreD = 0;  # большие части пятна
        self.scoreDd = 0;  # малые детали пятна
        # Цвет
        self.scoreFC = 0;  # форма доминирует
        self.scoreCF = 0;  # цвет доминирует
        self.scoreC = 0;  # цвет
        self.scoreF = 0;  # форма
        # Кинестетические показатели
        self.scoreM = 0;  # движение/ искажение
        self.scoreMH = 0;  # человевческие кинестезии
        self.scoreMA = 0;  # кинестезии животных
        # Локализация
        self.scoreS = 0;  # белый фон
        # scoreWS = 0;    #
        # scoreDdS = 0; #
        # Популярность
        self.scoreOrig = 0;  # оригинальные ответы
        self.scorePopular = 0;  # популярные ответы

        self.conflict, self.determinants, self.intelligence, self.type_of_experience = [], [], "", ""   #Результаты, которые в файле будем искать,
        # потом убрать, сразу из файла выводить

        self.scoreA #СЧЁТЧИК ОТВЕТОВ ЖИВОТНОЕ
        self.scoreMythH #магические человеки



    # Тип переживания

    # чтение из бд результатов
    # Загрузка изображения по порядковому номеру
    # отдельно считать сумму цвета fc, cf, c
    def setImg(self, numCard):
        pixmap = QPixmap(('cards/{numCard}.jpg').format(numCard=numCard))
        self.ui.cardImg.setPixmap(pixmap)

    # Подсчёт ответа по категории в процентах
    def countScoreInPercent(self, param):
        return param / self.numberOfReplies * 100

    # Подсчёт количества ответов по животным
    def countAnimal(self, score):
        if score == 1:
            self.a += 1
        return self.a

    # Подсчёт количества популярных ответов
    def countPopular(self, category):
        if (category != "другое"):
            match self.slideNumber:
                case 0:
                    if (category == "летучая мышь" or "бабочка" or "птица" or "человек"):
                        self.p += 1
                case 1:
                    if (category == "медведь" or "слон" or "собака" or "человек"):
                        self.p += 1
                case 2:
                    if (category == "человек"):
                        self.p += 1
                case 3:
                    if (category == "летучая мышь" or "бабочка"):
                        self.p += 1
                case 4:
                    if (category == "летучая мышь" or "бабочка" or "птица"):
                        self.p += 1
                case 5:
                    if (category == "черепаха"):
                        self.p += 1
                case 6:
                    if (category == "облако"):
                        self.p += 1
                case 7:
                    if (category == "собака" or "ящерица" or "тигр"):
                        self.p += 1
                case 8:
                    if (category == "голова человека"):
                        self.p += 1
                case 9:
                    if (category == "краб" or "осьминог" or "паук" or "собака" or "кролик" or "заяц" or "лев"):
                        self.p += 1
        return self.p


    # def countDeterminants(self):    #Общие показатели
        # match():
        #     case:
    def countTypeOfExperience(self):    #Тип переживания
        c = (3*self.c + 2*self.scoreCF + self.scoreFC)/2
        if (self.scoreM <=1 & c<=1):
            self.type_of_experience = 'коартированный'
        elif (self.scoreM <= 3 & c <= 3):
            self.type_of_experience = 'коартивный'
        elif (self.scoreM - c <= 3 & self.scoreM <=3 & c <= 3):
            self.type_of_experience = 'aмбиэквальный'
        elif (self.scoreM - c > 3):
            self.type_of_experience = 'интраверсивный'
        elif (c - self.scoreM > 3):
            self.type_of_experience = 'экстратенсивный'

    def countIntelligence(self):    #Интеллект
        if (self.scoreF >= 0 & self.scoreA & self.scoreOrig != 0 & self.scoreM != 0):
            self.intelligence = 'высокий'
        elif (self.scoreM == 0):
            self.intelligence = 'низкий'
        elif (self.scoreM == 0):
            self.intelligence = 'недостаточно'

    def countConflict(self):    #Конфликт и способ защиты
        if ((self.scoreCF + self.scoreC) > self.scoreFC & self.scoreF > 0.75):
            self.conflict+='конфликт'
            if (self.rejection_counter > 0.4 & self.scoreMythH != 0):
                self.conflict += 'вытеснение'
            elif (self.scoreM):
                self.conflict += 'изоляция'


    def sendResults(self):  # отправить результаты
        data= pd.read_csv('data/results/***.csv', sep=';', names=['label', 'text'], encoding='cp1251')
        # if (array or str == null)
        #     'Нет дополнительной информации по детерминантам'
        #     'Конфликт отсутствует'