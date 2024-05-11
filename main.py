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
