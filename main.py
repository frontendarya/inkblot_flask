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

    # Соответствие ответа критериям, постановка преддиагноза
    def chooseDiagnosis(self):
        scoreP = self.countScoreInPercent(self.p)
        scoreA = self.countScoreInPercent(self.a)
        scoreF = self.countScoreInPercent(self.f)
        scoreM = self.countScoreInPercent(self.m)
        scoreW = self.countScoreInPercent(self.w)
        scoreS = self.countScoreInPercent(self.s)
        scoreD = self.countScoreInPercent(self.d)
        scoreC = self.countScoreInPercent(self.c)

        if (scoreP>90 and 30>scoreA>35 and 70>scoreF>80 and scoreM<10 and 65<scoreW<70 and 14<scoreC<18):
            self.diagnosis = "Здоровый тестируемый"
        elif (18>scoreP>22 and 58>scoreA>62 and scoreF<50 and 5>scoreF>9 and 25>scoreW>29 and 4>scoreS>7 and 56>scoreD>60 and 5>scoreC>9):
            self.diagnosis = "Больные с алкогольным делирием"
        elif (65>scoreF>69 and 8>scoreM>12 and 40>scoreW>44 and 5>scoreD>9 and 14>scoreC>18):
            self.diagnosis = "Больные с остбредовыми формами шизофрении"
        elif (27>scoreP>31 and 48>scoreA>52 and 68>scoreF>72 and 8>scoreM>12 and 26>scoreW>30 and 1>scoreD>5 and 3>scoreC>7):
            self.diagnosis = "Атеросклероз"
        elif (scoreP>25 and scoreF>70 and scoreM>10 and scoreC<90):
            self.diagnosis = "Органические поражения головного мозга"
        else:
            self.diagnosis = "Ваши показатели не подходят к категориям, которые тестирует данное приложение"
        # Сохранение результата в базу данных
        with open('result.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.ui.nameInput.toPlainText(), self.diagnosis])
        return "Предварительный диагноз: "+self.diagnosis

    def countScore(self):
        self.numberOfReplies += 1
        what_result = self.ui.whatInput.toPlainText()
        self.p = self.countPopular(Popular.isPopular(what_result))
        self.a = self.countAnimal(Animal.isAnimal(what_result))

        if self.ui.formYesRadioBtn.isChecked(): #f (ответы с чёткой формой)
            self.f += 1
        if self.ui.actionYesRadioBtn.isChecked():   #m (ответы по движению)
            self.m += 1
        if self.ui.allPartRadioBtn.isChecked(): #w (целостные ответы)
            self.w += 1
        if self.ui.partBackRadioBtn.isChecked(): #s (ответы на белый фон)
            self.s += 1
        if self.ui.partSeparateRadioBtn.isChecked(): #d (ответы на мелкие детали)
            self.d += 1
        if self.ui.signColorFormRadioBtn.isChecked() or self.ui.signColoRadioBtn.isChecked(): #c (цветоформовые ответы и первичные по цвету)
            self.c += 1

    def countSlideNumber(self):
        self.slideNumber += 1
        match self.slideNumber:
            case 0:
                self.setImg(1)
            case 1:
                self.setImg(2)
            case 2:
                self.setImg(3)
            case 3:
                self.setImg(4)
            case 4:
                self.setImg(5)
            case 5:
                self.setImg(6)
            case 6:
                self.setImg(7)
            case 7:
                self.setImg(8)
            case 8:
                self.setImg(9)
            case 9:
                self.setImg(10)
            case _:
                self.ui.cardImg.setText(self.chooseDiagnosis())
                for i in self.elements_to_hide:
                    i.hide()


    # def countDeterminants(self):    #Общие показатели
    #     match():
    #         case:
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


    # def sendResults(self):  # отправить результаты
    #     data= pd.read_csv('data/results/***.csv', sep=';', names=['label', 'text'], encoding='cp1251')
    #     if (array or str == null)
    #         'Нет дополнительной информации по детерминантам'
    #         'Конфликт отсутствует'