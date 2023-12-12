from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys

# Окно для выбора языка
class LanWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox1 = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()

        # Создаём выпадающий список языков
        self.btn_settings = QtWidgets.QComboBox()
        self.btn_settings.setFixedHeight(30)
        self.btn_settings.setStyleSheet("QComboBox{font-size: 9pt;}")
        self.btn_settings.addItem('Russian')
        self.btn_settings.addItem('English')

        # Заголовок окна
        self.lbl_1 = QtWidgets.QLabel('Settings')
        self.lbl_1.setStyleSheet("QLabel{font: 14pt Posterama}")
        self.lbl_1.setAlignment(QtCore.Qt.AlignCenter)
        self.font = self.lbl_1.font()
        self.font.setBold(True)
        self.lbl_1.setFont(self.font)

        # Заголовок относящийся к списку
        self.lbl = QtWidgets.QLabel('Choose language:')
        self.lbl.setStyleSheet("QLabel{font: 9pt;}")
        self.font = self.lbl.font()
        self.lbl.setFont(self.font)

        # Кнопки для продолжения программы и её закрытия
        self.btn_continue = QtWidgets.QPushButton('Continue')
        self.btn_continue.setFixedSize(200, 40)
        self.btn_continue.setStyleSheet("QPushButton{font-size: 10pt;}")
        self.btn_continue.clicked.connect(self.show_mwind)
        self.btn_close = QtWidgets.QPushButton('Close')
        self.btn_close.setFixedSize(200, 40)
        self.btn_close.setStyleSheet("QPushButton{font-size: 10pt;}")
        self.btn_close.clicked.connect(self.close)

        self.vbox1.addWidget(self.lbl_1)
        self.vbox1.addWidget(self.lbl)
        self.vbox1.addWidget(self.btn_settings)
        self.hbox.addWidget(self.btn_continue)
        self.hbox.addWidget(self.btn_close)

        self.vbox.addLayout(self.vbox1)
        self.vbox.addLayout(self.hbox)

        # Указываем размер окна и его название
        self.setLayout(self.vbox)
        self.setFixedSize(425, 170)
        self.setWindowTitle('Program for calculating Body Mass Index')

    # Функция для отображения основного окна
    def show_mwind(self):
        lan = self.btn_settings.currentText()

        # В зависимости от выбранного языка, будет открываться одно из двух соответствующих окон
        if lan == 'Russian':
            mwind.show()
        elif lan == 'English':
            ENmwind.show()


# Основное окно
class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.vbox1 = QtWidgets.QVBoxLayout()
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()

        # Заголовок окна
        self.lbl = QtWidgets.QLabel('Калькулятор ИМТ')
        self.lbl.setStyleSheet("QLabel{font: 24pt Comic Sans MS}")
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.font = self.lbl.font()
        self.font.setBold(True)
        self.lbl.setFont(self.font)

        # Основная информация
        self.lbl_information = QtWidgets.QLabel('''
С помощью индекса массы тела (ИМТ) можно установить степень лишнего веса, 
что позволяет оценить угрозу возникновения болезней, ассоциированных с ожирением.

Формула ИМТ = вес (в килограммах) / (рост (м))**2

Вы можете определить свой ИМТ с помощью нашего калькулятора.
        ''')
        self.lbl_information.setStyleSheet("QLabel{font-size: 10pt;}")
        self.lbl_information.setAlignment(QtCore.Qt.AlignCenter)

        # Создаём таблицу
        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(8)
        self.table.setColumnCount(3)

        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem('ИМТ для мужчин'))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem('ИМТ для женщин'))
        self.table.setItem(0, 2, QtWidgets.QTableWidgetItem('Результат'))
        self.table.setItem(1, 0, QtWidgets.QTableWidgetItem('16 и менее'))
        self.table.setItem(1, 1, QtWidgets.QTableWidgetItem('16 и менее'))
        self.table.setItem(1, 2, QtWidgets.QTableWidgetItem('Выраженный дефицит массы тела'))
        self.table.setItem(2, 0, QtWidgets.QTableWidgetItem('16 - 20'))
        self.table.setItem(2, 1, QtWidgets.QTableWidgetItem('16 - 19'))
        self.table.setItem(2, 2, QtWidgets.QTableWidgetItem('Недостаточная (дефицит) масса тела'))
        self.table.setItem(3, 0, QtWidgets.QTableWidgetItem('20 - 25'))
        self.table.setItem(3, 1, QtWidgets.QTableWidgetItem('19 - 24'))
        self.table.setItem(3, 2, QtWidgets.QTableWidgetItem('Норма'))
        self.table.setItem(4, 0, QtWidgets.QTableWidgetItem('25 - 30'))
        self.table.setItem(4, 1, QtWidgets.QTableWidgetItem('24 - 30'))
        self.table.setItem(4, 2, QtWidgets.QTableWidgetItem('Избыточная масса тела (предожирение)'))
        self.table.setItem(5, 0, QtWidgets.QTableWidgetItem('30 - 35'))
        self.table.setItem(5, 1, QtWidgets.QTableWidgetItem('30 - 35'))
        self.table.setItem(5, 2, QtWidgets.QTableWidgetItem('Ожирение 1 степени'))
        self.table.setItem(6, 0, QtWidgets.QTableWidgetItem('35 - 40'))
        self.table.setItem(6, 1, QtWidgets.QTableWidgetItem('35 - 40'))
        self.table.setItem(6, 2, QtWidgets.QTableWidgetItem('Ожирение 2 степени'))
        self.table.setItem(7, 0, QtWidgets.QTableWidgetItem('40 и более'))
        self.table.setItem(7, 1, QtWidgets.QTableWidgetItem('40 и более'))
        self.table.setItem(7, 2, QtWidgets.QTableWidgetItem('Ожирение 3 степени'))

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

        # Кнопки для открытия окна расчёта и закрытия данного окна
        self.btn_continue = QtWidgets.QPushButton('Перейти к расчёту')
        self.btn_continue.setFixedSize(300, 40)
        self.btn_continue.setStyleSheet("QPushButton{font-size: 10pt;}")
        self.btn_continue.clicked.connect(self.show_IMTwind)
        self.btn_close = QtWidgets.QPushButton('Закрыть')
        self.btn_close.setFixedSize(300, 40)
        self.btn_close.setStyleSheet("QPushButton{font-size: 10pt;}")
        self.btn_close.clicked.connect(self.close)

        self.vbox1.addWidget(self.lbl)
        self.vbox1.addWidget(self.lbl_information)
        self.vbox1.addWidget(self.table)
        self.hbox.addWidget(self.btn_continue)
        self.hbox.addWidget(self.btn_close)

        self.vbox.addLayout(self.vbox1)
        self.vbox.addLayout(self.hbox)

        # Указываем размер окна и его название
        self.setFixedSize(950, 640)
        self.setLayout(self.vbox)
        self.setWindowTitle('Программа расчёта Индекса Массы Тела')

    # Функция для отображения окна расчёта
    def show_IMTwind(self):
        IMTwind.show()


# Основное окно на английском
class ENMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.vbox1 = QtWidgets.QVBoxLayout()
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()

        self.lbl = QtWidgets.QLabel('BMI Сalculator')
        self.lbl.setStyleSheet("QLabel{font: 24pt Comic Sans MS}")
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.font = self.lbl.font()
        self.font.setBold(True)
        self.lbl.setFont(self.font)

        self.lbl_information = QtWidgets.QLabel('''
The Body Mass Index (BMI) measures how overweight you are.
which allows assessing the risk of obesity-associated diseases.

BMI formula = weight (in kilograms) / (height (m))**2

You can determine your BMI using our calculator.
                ''')
        self.lbl_information.setStyleSheet("QLabel{font-size: 10pt;}")
        self.lbl_information.setAlignment(QtCore.Qt.AlignCenter)

        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(8)
        self.table.setColumnCount(3)

        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem('BMI for men'))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem('BMI for women'))
        self.table.setItem(0, 2, QtWidgets.QTableWidgetItem('Result'))
        self.table.setItem(1, 0, QtWidgets.QTableWidgetItem('16 and under'))
        self.table.setItem(1, 1, QtWidgets.QTableWidgetItem('16 and under'))
        self.table.setItem(1, 2, QtWidgets.QTableWidgetItem('Severe underweight'))
        self.table.setItem(2, 0, QtWidgets.QTableWidgetItem('16 - 20'))
        self.table.setItem(2, 1, QtWidgets.QTableWidgetItem('16 - 19'))
        self.table.setItem(2, 2, QtWidgets.QTableWidgetItem('Insufficient (deficit) body weight'))
        self.table.setItem(3, 0, QtWidgets.QTableWidgetItem('20 - 25'))
        self.table.setItem(3, 1, QtWidgets.QTableWidgetItem('19 - 24'))
        self.table.setItem(3, 2, QtWidgets.QTableWidgetItem('Norm'))
        self.table.setItem(4, 0, QtWidgets.QTableWidgetItem('25 - 30'))
        self.table.setItem(4, 1, QtWidgets.QTableWidgetItem('24 - 30'))
        self.table.setItem(4, 2, QtWidgets.QTableWidgetItem('Overweight (preobesity)'))
        self.table.setItem(5, 0, QtWidgets.QTableWidgetItem('30 - 35'))
        self.table.setItem(5, 1, QtWidgets.QTableWidgetItem('30 - 35'))
        self.table.setItem(5, 2, QtWidgets.QTableWidgetItem('Obesity 1 degree'))
        self.table.setItem(6, 0, QtWidgets.QTableWidgetItem('35 - 40'))
        self.table.setItem(6, 1, QtWidgets.QTableWidgetItem('35 - 40'))
        self.table.setItem(6, 2, QtWidgets.QTableWidgetItem('Obesity 2 degree'))
        self.table.setItem(7, 0, QtWidgets.QTableWidgetItem('40 or more'))
        self.table.setItem(7, 1, QtWidgets.QTableWidgetItem('40 or more'))
        self.table.setItem(7, 2, QtWidgets.QTableWidgetItem('Obesity 3 degree'))

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

        self.btn_continue = QtWidgets.QPushButton('Go to calculation')
        self.btn_continue.setFixedSize(300, 40)
        self.btn_continue.setStyleSheet("QPushButton{font-size: 10pt;}")
        self.btn_continue.clicked.connect(self.show_IMTwind)
        self.btn_close = QtWidgets.QPushButton('Close')
        self.btn_close.setFixedSize(300, 40)
        self.btn_close.setStyleSheet("QPushButton{font-size: 10pt;}")
        self.btn_close.clicked.connect(self.close)

        self.vbox1.addWidget(self.lbl)
        self.vbox1.addWidget(self.lbl_information)
        self.vbox1.addWidget(self.table)
        self.hbox.addWidget(self.btn_continue)
        self.hbox.addWidget(self.btn_close)

        self.vbox.addLayout(self.vbox1)
        self.vbox.addLayout(self.hbox)

        self.setFixedSize(950, 640)
        self.setLayout(self.vbox)
        self.setWindowTitle('Program for calculating Body Mass Index')

    def show_IMTwind(self):
        ENIMTwind.show()


# Окно для расчёта ИМТ
class IMTWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox1 = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()

        # Заголовок окна
        self.lbl = QtWidgets.QLabel('Расчёт Индекса Массы Тела')
        self.lbl.setStyleSheet("QLabel{font: 18pt Comic Sans MS}")
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.font = self.lbl.font()
        self.font.setBold(True)
        self.lbl.setFont(self.font)

        # Создаём остальные заголовки, находящиеся на коне
        self.lbl_height = QtWidgets.QLabel('Введите рост (см): ')
        self.lbl_height.setStyleSheet("QLabel{font: 10pt;}")

        self.lbl_weight = QtWidgets.QLabel('Введите вес (кг): ')
        self.lbl_weight.setStyleSheet("QLabel{font: 10pt;}")

        self.lbl_sex = QtWidgets.QLabel('Выберите пол: ')
        self.lbl_sex.setStyleSheet("QLabel{font: 10pt;}")

        self.lbl_itog = QtWidgets.QLabel('Итог: ')
        self.lbl_itog.setStyleSheet("QLabel{font: 10pt;}")

        # Пустые заголовки для всплывающей информации
        self.lbl_result = QtWidgets.QLabel('')
        self.lbl_recommendations = QtWidgets.QLabel('')
        self.lbl_ideal = QtWidgets.QLabel('')

        # Поля ввода информации
        self.height = QtWidgets.QLineEdit()
        self.height.setStyleSheet("QLineEdit{font-size: 9pt;}")
        self.weight = QtWidgets.QLineEdit()
        self.weight.setStyleSheet("QLineEdit{font-size: 9pt;}")

        # Выпадающий список выбора пола
        self.sex = QtWidgets.QComboBox()
        self.sex.addItem('Мужчина')
        self.sex.addItem('Женщина')
        self.sex.setStyleSheet("QComboBox{font-size: 9pt;}")

        # Кнопки для расчёта ИМТ и закрытия окна
        self.btn_raschet = QtWidgets.QPushButton('Рассчитать ИМТ')
        self.btn_raschet.clicked.connect(self.right)
        self.btn_raschet.setFixedSize(300, 40)
        self.btn_raschet.setStyleSheet("QPushButton{font-size: 10pt;}")
        self.btn_close = QtWidgets.QPushButton('Закрыть')
        self.btn_close.clicked.connect(self.close)
        self.btn_close.setFixedSize(300, 40)
        self.btn_close.setStyleSheet("QPushButton{font-size: 10pt;}")

        self.vbox1.addWidget(self.lbl)
        self.vbox1.addWidget(self.lbl_height)
        self.vbox1.addWidget(self.height)
        self.vbox1.addWidget(self.lbl_weight)
        self.vbox1.addWidget(self.weight)
        self.vbox1.addWidget(self.lbl_sex)
        self.vbox1.addWidget(self.sex)
        self.hbox.addWidget(self.btn_raschet)
        self.vbox1.addWidget(self.lbl_itog)
        self.vbox1.addWidget(self.lbl_result)
        self.hbox.addWidget(self.btn_close)

        self.vbox.addLayout(self.vbox1)
        self.vbox.addLayout(self.hbox)

        # Указываем размер окна и его название
        self.setLayout(self.vbox)
        self.setWindowTitle('Программа расчёта Индекса Массы Тела')

    # Функция для проверки данных на наличие ошибок
    def right(self):
        # Проверяем данные на наличие ошибок
        try:
            # Ввёл ли пользователь числа
            height = float(self.height.text())
            self.lbl_height.setText('Введите рост (см): ')
            self.lbl_height.setStyleSheet("QLabel{font: 10pt;}")
            # Длина ввадимого значения
            if len(self.height.text()) > 5:
                self.lbl_height.setText('Введите рост (см): ЗНАЧЕНИЕ НЕ ДОЛЖНО ПРЕВЫЩАТЬ 5 ЗНАКОВ')
                self.lbl_height.setStyleSheet("QLabel{font: 10pt; color: red;}")
                self.lbl_result.setText('')
                self.lbl_recommendations.setText('')
                self.lbl_ideal.setText('')
            # Какого размера введённые данные
            if 0 < height < 100000:
                try:
                    # Ввёл ли пользователь числа
                    weight = float(self.weight.text())
                    self.lbl_weight.setText('Введите вес (кг): ')
                    self.lbl_weight.setStyleSheet("QLabel{font: 10pt;}")
                    # Длина ввадимого значения
                    if len(self.weight.text()) > 5:
                        self.lbl_weight.setText('Введите вес (кг): ЗНАЧЕНИЕ НЕ ДОЛЖНО ПРЕВЫЩАТЬ 5 ЗНАКОВ')
                        self.lbl_weight.setStyleSheet("QLabel{font: 10pt; color: red;}")
                        self.lbl_result.setText('')
                        self.lbl_recommendations.setText('')
                        self.lbl_ideal.setText('')
                    # Какого размера введённые данные
                    elif 0 < weight < 100000:
                        self.raschet()
                    elif weight < 1:
                        self.lbl_weight.setText('Введите вес (кг): ЗНАЧЕНИЕ СЛИШКОМ МАЛО')
                        self.lbl_weight.setStyleSheet("QLabel{font: 10pt; color: red;}")
                        self.lbl_result.setText('')
                        self.lbl_recommendations.setText('')
                        self.lbl_ideal.setText('')
                    elif weight > 99999:
                        self.lbl_weight.setText('Введите вес (кг): ПРЕВЫШЕНО МАКСИМАЛЬНОЕ ЗНАЧЕНИЕ')
                        self.lbl_weight.setStyleSheet("QLabel{font: 10pt; color: red;}")
                        self.lbl_result.setText('')
                        self.lbl_recommendations.setText('')
                        self.lbl_ideal.setText('')
                    # Длина ввадимого значения
                    elif len(self.weight.text()) > 5:
                        self.lbl_weight.setText('Введите вес (кг): ЗНАЧЕНИЕ НЕ ДОЛЖНО ПРЕВЫЩАТЬ 5 ЗНАКОВ')
                        self.lbl_weight.setStyleSheet("QLabel{font: 10pt; color: red;}")
                        self.lbl_result.setText('')
                        self.lbl_recommendations.setText('')
                        self.lbl_ideal.setText('')
                except ValueError:
                    self.lbl_weight.setText('Введите вес (кг): ДАННЫЕ ВВЕДЕНЫ НЕВЕРНО')
                    self.lbl_weight.setStyleSheet("QLabel{font: 10pt; color: red;}")
                    self.lbl_result.setText('')
                    self.lbl_recommendations.setText('')
                    self.lbl_ideal.setText('')
            # Какого размера введённые данные
            elif height < 1:
                self.lbl_height.setText('Введите рост (см): ЗНАЧЕНИЕ СЛИШКОМ МАЛО')
                self.lbl_height.setStyleSheet("QLabel{font: 10pt; color: red;}")
                self.lbl_result.setText('')
                self.lbl_recommendations.setText('')
                self.lbl_ideal.setText('')
            elif height > 99999:
                self.lbl_height.setText('Введите рост (см): ПРЕВЫШЕНО МАКСИМАЛЬНОЕ ЗНАЧЕНИЕ')
                self.lbl_height.setStyleSheet("QLabel{font: 10pt; color: red;}")
                self.lbl_result.setText('')
                self.lbl_recommendations.setText('')
                self.lbl_ideal.setText('')
            # Длина ввадимого значения
            elif len(self.height.text()) > 5:
                self.lbl_height.setText('Введите рост (см): ЗНАЧЕНИЕ НЕ ДОЛЖНО ПРЕВЫЩАТЬ 5 ЗНАКОВ')
                self.lbl_height.setStyleSheet("QLabel{font: 10pt; color: red;}")
                self.lbl_result.setText('')
                self.lbl_recommendations.setText('')
                self.lbl_ideal.setText('')
        except ValueError:
            self.lbl_height.setText('Введите рост (см): ДАННЫЕ ВВЕДЕНЫ НЕВЕРНО')
            self.lbl_height.setStyleSheet("QLabel{font: 10pt; color: red;}")
            self.lbl_result.setText('')
            self.lbl_recommendations.setText('')
            self.lbl_ideal.setText('')

    # Функция для произведения расчётов
    def raschet(self):
        height = float(self.height.text())
        weight = float(self.weight.text())
        sex = self.sex.currentText()

        mheight = height/100
        kwheight = mheight*mheight

        I = weight / kwheight

        result = str(round(I, 2))

        # Выводимая информация если пол мужской
        if sex == 'Мужчина':
            # Выраженный дефицит массы тела
            if I <= 16:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Выраженный дефицит массы тела')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Единственный способ поправиться — больше кушать. 
Наращивать объемы лучше с добавлением в рацион высококалорийных продуктов — орехов, 
сложных углеводов, молока, кефира, творога. Для поднятия веса лучше прибегать к силовым тренировкам.

Эффективным будет добавление витаминов и БАДов. Однако важно проконсультироваться с лечащим врачом, 
чтобы он определил, каких именно полезных веществ не хватает организму. 
Безопасный и быстрый способ повысить вес — прием пивных дрожжей. 
Для улучшения пищеварения врач может порекомендовать пробиотики.
                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-100) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Недостаточная (дефицит) масса тела
            elif 16 < I <= 20:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Недостаточная (дефицит) масса тела')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Единственный способ поправиться — больше кушать. 
Наращивать объемы лучше с добавлением в рацион высококалорийных продуктов — орехов, 
сложных углеводов, молока, кефира, творога. Для поднятия веса лучше прибегать к силовым тренировкам.
                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-100) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Норма
            elif 20 < I <= 25:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Норма')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Нормальный вес не является гарантией богатырского здоровья, но значительно снижает риск появления нарушений и 
заболеваний, вызываемых избыточным или недостаточным весом. Кроме того, обладатели нормального веса, как правило, 
пребывают в хорошем самочувствии даже после интенсивных физических нагрузок.
                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-100) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Избыточная масса тела (предожирение)
            elif 25 < I <= 30:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Избыточная масса тела (предожирение)')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Достаточно скорректировать образ жизни, питание:

- Отказаться от любого алкоголя;
- Увеличить потребление фруктов, овощей;
- Уменьшить количество калорий;
- Заниматься спортом минимум 150 минут в неделю.

Поддерживать организм в тонусе помогают зеленые, травяные чаи, цитрусовые фрукты, 
кисломолочные продукты жирностью не более 2,5%.

Бороться с лишним весом — тяжелая работа, поэтому следите за питанием, занимайтесь спортом, 
больше двигайтесь и будьте здоровы!
                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-100) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Ожирение 1 степен
            elif 30 < I <= 35:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Ожирение 1 степени')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Ожирение требует не просто коррекции образа жизни. Врач должен выяснить корень проблемы, назначить лечение. 
Причиной может быть как банальное переедание, так и гормональный сбой. 
Наряду с соответствующими лекарствами эффективным будет прием витаминов для коррекции веса. 
Их подбором должен заниматься лечащий врач или диетолог.      

Бороться с лишним весом — тяжелая работа, поэтому следите за питанием, занимайтесь спортом, 
больше двигайтесь и будьте здоровы!          
                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-100) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Ожирение 2 степен
            elif 35 < I <= 40:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Ожирение 2 степени')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Кроме коррекции питания, физических нагрузок врач должен назначить лечение в соответствии с причиной ожирения. 
Это могут быть как пищевые привычки, малоактивный образ жизни, так и гормонально-эндокринные заболевания, 
а у женщин — синдром поликистозных яичников. В большинстве случаев назначают препараты для нормализации обмена веществ.

Бороться с лишним весом — тяжелая работа, поэтому следите за питанием, занимайтесь спортом, 
больше двигайтесь и будьте здоровы!
                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-100) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Ожирение 3 степен
            elif I > 40:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Ожирение 3 степени')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Победить ожирение высокой степени можно только комплексом мер, силой воли. Необходима лекарственная терапия, 
направленная на устранение причин, сопутствующих заболеваний, а также постепенное изменение пищевых привычек.

Бороться с лишним весом — тяжелая работа, поэтому следите за питанием, занимайтесь спортом, 
больше двигайтесь и будьте здоровы!
                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-100) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")


        # Выводимая информация если пол женский
        elif sex == 'Женщина':
            # Выраженный дефицит массы тела
            if I <= 16:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Выраженный дефицит массы тела')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Единственный способ поправиться — больше кушать. 
Наращивать объемы лучше с добавлением в рацион высококалорийных продуктов — орехов, 
сложных углеводов, молока, кефира, творога. Для поднятия веса лучше прибегать к силовым тренировкам.

Эффективным будет добавление витаминов и БАДов. Однако важно проконсультироваться с лечащим врачом, 
чтобы он определил, каких именно полезных веществ не хватает организму. 
Безопасный и быстрый способ повысить вес — прием пивных дрожжей. 
Для улучшения пищеварения врач может порекомендовать пробиотики.
                                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-110) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Недостаточная (дефицит) масса тела
            elif 16 < I <= 19:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Недостаточная (дефицит) масса тела')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Единственный способ поправиться — больше кушать. 
Наращивать объемы лучше с добавлением в рацион высококалорийных продуктов — орехов, 
сложных углеводов, молока, кефира, творога. Для поднятия веса лучше прибегать к силовым тренировкам.
                            ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-110) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Норма
            elif 19 < I <= 24:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Норма')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Нормальный вес не является гарантией богатырского здоровья, но значительно снижает риск появления нарушений и 
заболеваний, вызываемых избыточным или недостаточным весом. Кроме того, обладатели нормального веса, как правило, 
пребывают в хорошем самочувствии даже после интенсивных физических нагрузок.
                                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-110) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Избыточная масса тела (предожирение)
            elif 24 < I <= 30:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Избыточная масса тела (предожирение)')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Достаточно скорректировать образ жизни, питание:

- Отказаться от любого алкоголя;
- Увеличить потребление фруктов, овощей;
- Уменьшить количество калорий;
- Заниматься спортом минимум 150 минут в неделю.

Поддерживать организм в тонусе помогают зеленые, травяные чаи, цитрусовые фрукты, 
кисломолочные продукты жирностью не более 2,5%.

Бороться с лишним весом — тяжелая работа, поэтому следите за питанием, занимайтесь спортом, 
больше двигайтесь и будьте здоровы!
                            ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-110) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Ожирение 1 степен
            elif 30 < I <= 35:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Ожирение 1 степени')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Ожирение требует не просто коррекции образа жизни. Врач должен выяснить корень проблемы, назначить лечение. 
Причиной может быть как банальное переедание, так и гормональный сбой. 
Наряду с соответствующими лекарствами эффективным будет прием витаминов для коррекции веса. 
Их подбором должен заниматься лечащий врач или диетолог.      

Бороться с лишним весом — тяжелая работа, поэтому следите за питанием, занимайтесь спортом, 
больше двигайтесь и будьте здоровы!          
                                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-110) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Ожирение 2 степен
            elif 35 < I <= 40:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Ожирение 2 степени')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Кроме коррекции питания, физических нагрузок врач должен назначить лечение в соответствии с причиной ожирения. 
Это могут быть как пищевые привычки, малоактивный образ жизни, так и гормонально-эндокринные заболевания, 
а у женщин — синдром поликистозных яичников. В большинстве случаев назначают препараты для нормализации обмена веществ.

Бороться с лишним весом — тяжелая работа, поэтому следите за питанием, занимайтесь спортом, 
больше двигайтесь и будьте здоровы!
                            ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-110) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            # Ожирение 3 степен
            elif I > 40:
                self.lbl_result.setText('Ваш ИМТ ' + result + ' - Ожирение 3 степени')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Рекомендация:
Победить ожирение высокой степени можно только комплексом мер, силой воли. Необходима лекарственная терапия, 
направленная на устранение причин, сопутствующих заболеваний, а также постепенное изменение пищевых привычек.

Бороться с лишним весом — тяжелая работа, поэтому следите за питанием, занимайтесь спортом, 
больше двигайтесь и будьте здоровы!
                            ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Ваш идеальный вес: ' + str(height-110) + ' кг')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")


# Окно для произведения расчётов на английском
class ENIMTWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox1 = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()

        self.lbl = QtWidgets.QLabel('Body Mass Index Calculation')
        self.lbl.setStyleSheet("QLabel{font: 18pt Comic Sans MS}")
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.font = self.lbl.font()
        self.font.setBold(True)
        self.lbl.setFont(self.font)

        self.lbl_height = QtWidgets.QLabel('Enter height (cm):')
        self.lbl_height.setStyleSheet("QLabel{font: 10pt;}")

        self.lbl_weight = QtWidgets.QLabel('Enter weight (kg):')
        self.lbl_weight.setStyleSheet("QLabel{font: 10pt;}")

        self.lbl_sex = QtWidgets.QLabel('Select gender: ')
        self.lbl_sex.setStyleSheet("QLabel{font: 10pt;}")

        self.lbl_itog = QtWidgets.QLabel('Outcome:')
        self.lbl_itog.setStyleSheet("QLabel{font: 10pt;}")

        self.lbl_result = QtWidgets.QLabel('')
        self.lbl_recommendations = QtWidgets.QLabel('')
        self.lbl_ideal = QtWidgets.QLabel('')

        self.height = QtWidgets.QLineEdit()
        self.height.setStyleSheet("QLineEdit{font: 9pt;}")
        self.weight = QtWidgets.QLineEdit()
        self.weight.setStyleSheet("QLineEdit{font: 9pt;}")

        self.sex = QtWidgets.QComboBox()
        self.sex.addItem('Man')
        self.sex.addItem('Woman')
        self.sex.setStyleSheet("QComboBox{font: 9pt;}")

        self.btn_raschet = QtWidgets.QPushButton('Calculate BMI')
        self.btn_raschet.clicked.connect(self.right)
        self.btn_raschet.setFixedSize(300, 40)
        self.btn_raschet.setStyleSheet("QPushButton{font-size: 10pt;}")
        self.btn_close = QtWidgets.QPushButton('Close')
        self.btn_close.clicked.connect(self.close)
        self.btn_close.setFixedSize(300, 40)
        self.btn_close.setStyleSheet("QPushButton{font-size: 10pt;}")


        self.vbox1.addWidget(self.lbl)
        self.vbox1.addWidget(self.lbl_height)
        self.vbox1.addWidget(self.height)
        self.vbox1.addWidget(self.lbl_weight)
        self.vbox1.addWidget(self.weight)
        self.vbox1.addWidget(self.lbl_sex)
        self.vbox1.addWidget(self.sex)
        self.hbox.addWidget(self.btn_raschet)
        self.vbox1.addWidget(self.lbl_itog)
        self.vbox1.addWidget(self.lbl_result)
        self.hbox.addWidget(self.btn_close)

        self.vbox.addLayout(self.vbox1)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)
        self.setWindowTitle('Program for calculating Body Mass Index')


    def right(self):
        try:
            height = float(self.height.text())
            self.lbl_height.setText('Enter height (cm): ')
            self.lbl_height.setStyleSheet("QLabel{font: 10pt;}")
            if len(self.height.text()) > 5:
                self.lbl_height.setText('Enter height (cm): VALUE MUST NOT EXCEED 5 DIGITS')
                self.lbl_height.setStyleSheet("QLabel{font: 10pt; color: red;}")
                self.lbl_result.setText('')
                self.lbl_recommendations.setText('')
                self.lbl_ideal.setText('')
            elif 0 < height < 100000:
                try:
                    weight = float(self.weight.text())
                    self.lbl_weight.setText('Enter weight (kg): ')
                    self.lbl_weight.setStyleSheet("QLabel{font: 10pt;}")
                    if len(self.weight.text()) > 5:
                        self.lbl_weight.setText('Enter weight (kg): VALUE MUST NOT EXCEED 5 DIGITS')
                        self.lbl_weight.setStyleSheet("QLabel{font: 10pt; color: red;}")
                        self.lbl_result.setText('')
                        self.lbl_recommendations.setText('')
                        self.lbl_ideal.setText('')
                    elif 0 < weight < 100000:
                        self.raschet()
                    elif weight < 1:
                        self.lbl_weight.setText('Enter weight (kg): VALUE TOO SMALL')
                        self.lbl_weight.setStyleSheet("QLabel{font: 10pt; color: red;}")
                        self.lbl_result.setText('')
                        self.lbl_recommendations.setText('')
                        self.lbl_ideal.setText('')
                    elif weight > 99999:
                        self.lbl_weight.setText('Enter weight (kg): MAXIMUM VALUE EXCEEDED')
                        self.lbl_weight.setStyleSheet("QLabel{font: 10pt; color: red;}")
                        self.lbl_result.setText('')
                        self.lbl_recommendations.setText('')
                        self.lbl_ideal.setText('')
                    elif len(self.weight.text()) > 5:
                        self.lbl_weight.setText('Enter weight (kg): VALUE MUST NOT EXCEED 5 DIGITS')
                        self.lbl_weight.setStyleSheet("QLabel{font: 10pt; color: red;}")
                        self.lbl_result.setText('')
                        self.lbl_recommendations.setText('')
                        self.lbl_ideal.setText('')
                except ValueError:
                    self.lbl_weight.setText('Enter weight (kg): DATA ENTERED INCORRECTLY')
                    self.lbl_weight.setStyleSheet("QLabel{font: 10pt; color: red;}")
                    self.lbl_result.setText('')
                    self.lbl_recommendations.setText('')
                    self.lbl_ideal.setText('')
            elif height < 1:
                self.lbl_height.setText('Enter height (cm): VALUE TOO SMALL')
                self.lbl_height.setStyleSheet("QLabel{font: 10pt; color: red;}")
                self.lbl_result.setText('')
                self.lbl_recommendations.setText('')
                self.lbl_ideal.setText('')
            elif height > 99999:
                self.lbl_height.setText('Enter height (cm): MAXIMUM VALUE EXCEEDED')
                self.lbl_height.setStyleSheet("QLabel{font: 10pt; color: red;}")
                self.lbl_result.setText('')
                self.lbl_recommendations.setText('')
                self.lbl_ideal.setText('')
            elif len(self.height.text()) > 5:
                self.lbl_height.setText('Enter height (cm): VALUE MUST NOT EXCEED 5 DIGITS')
                self.lbl_height.setStyleSheet("QLabel{font: 10pt; color: red;}")
                self.lbl_result.setText('')
                self.lbl_recommendations.setText('')
                self.lbl_ideal.setText('')
        except ValueError:
            self.lbl_height.setText('Enter height (cm): DATA ENTERED INCORRECTLY')
            self.lbl_height.setStyleSheet("QLabel{font: 10pt; color: red;}")
            self.lbl_result.setText('')
            self.lbl_recommendations.setText('')
            self.lbl_ideal.setText('')


    def raschet(self):
        height = float(self.height.text())
        weight = float(self.weight.text())
        sex = self.sex.currentText()

        mheight = height/100
        kwheight = mheight*mheight

        I = weight / kwheight

        result = str(round(I, 2))

        if sex == 'Man':
            if I <= 16:
                self.lbl_result.setText('Your BMI ' + result + ' - Severe underweight')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
The only way to get better is to eat more.
It is better to increase volumes with the addition of high-calorie foods to the diet - nuts,
complex carbohydrates, milk, kefir, cottage cheese. To lift weight, it is better to resort to strength training.

The addition of vitamins and dietary supplements will be effective. However, it is important to consult with your doctor
so that he determines which nutrients the body lacks.
A safe and fast way to gain weight is to take brewer's yeast.
Your doctor may recommend probiotics to improve digestion.
                                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-100) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif 16 < I <= 20:
                self.lbl_result.setText('Your BMI ' + result + ' - Insufficient (deficit) body weight')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
The only way to get better is to eat more.
It is better to increase volumes with the addition of high-calorie foods to the diet - nuts,
complex carbohydrates, milk, kefir, cottage cheese. To lift weight, it is better to resort to strength training.
                                            ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-100) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif 20 < I <= 25:
                self.lbl_result.setText('Your BMI ' + result + ' - Norm')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
Normal weight is not a guarantee of good health, but it significantly reduces the risk of disorders and
diseases caused by overweight or underweight. In addition, people of normal weight tend to
stay in good health even after intense physical exertion.
                                                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-100) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif 25 < I <= 30:
                self.lbl_result.setText('Your BMI ' + result + ' - Overweight (preobesity)')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
It is enough to adjust the lifestyle, nutrition:

- Refuse any alcohol;
- Increase consumption of fruits, vegetables;
- Reduce the number of calories;
- Exercise at least 150 minutes per week.

Green, herbal teas, citrus fruits,
fermented milk products with a fat content of not more than 2.5%.

Fighting excess weight is hard work, so watch your diet, exercise,
move more and be healthy!
                                            ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-100) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif 30 < I <= 35:
                self.lbl_result.setText('Your BMI ' + result + ' - Obesity 1 degree')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
Obesity requires more than just lifestyle changes. The doctor must find out the root of the problem, prescribe treatment.
The reason can be both banal overeating and hormonal failure.
Along with appropriate medications, taking vitamins for weight correction will be effective.
Their selection should be handled by the attending physician or nutritionist.

Fighting excess weight is hard work, so watch your diet, exercise,
move more and be healthy!          
                                                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-100) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif 35 < I < 40:
                self.lbl_result.setText('Your BMI ' + result + ' - Obesity 2 degree')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
In addition to correcting nutrition, physical activity, the doctor must prescribe treatment in accordance with the cause of obesity.
It can be both eating habits, an inactive lifestyle, and hormonal and endocrine diseases,
and in women, polycystic ovary syndrome.
In most cases, drugs are prescribed to normalize metabolism.

Fighting excess weight is hard work, so watch your diet, exercise,
move more and be healthy!
                                            ''')

                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-100) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif I >= 40:
                self.lbl_result.setText('Your BMI ' + result + ' - Obesity 3 degree')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
Defeating high obesity is possible only by a set of measures, by willpower. Requires drug therapy
aimed at eliminating the causes, concomitant diseases, as well as a gradual change in eating habits.

Fighting excess weight is hard work, so watch your diet, exercise,
move more and be healthy!
                                            ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-100) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")

        elif sex == 'Woman':
            if I <= 16:
                self.lbl_result.setText('Your BMI ' + result + ' - Severe underweight')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
The only way to get better is to eat more.
It is better to increase volumes with the addition of high-calorie foods to the diet - nuts,
complex carbohydrates, milk, kefir, cottage cheese. To lift weight, it is better to resort to strength training.

The addition of vitamins and dietary supplements will be effective. However, it is important to consult with your doctor
so that he determines which nutrients the body lacks.
A safe and fast way to gain weight is to take brewer's yeast.
Your doctor may recommend probiotics to improve digestion.
                                                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-110) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif 16 < I <= 19:
                self.lbl_result.setText('Your BMI ' + result + ' - Insufficient (deficit) body weight')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
The only way to get better is to eat more.
It is better to increase volumes with the addition of high-calorie foods to the diet - nuts,
complex carbohydrates, milk, kefir, cottage cheese. To lift weight, it is better to resort to strength training.
                                                            ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-110) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif 19 < I <= 24:
                self.lbl_result.setText('Your BMI ' + result + ' - Norm')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
Normal weight is not a guarantee of good health, but it significantly reduces the risk of disorders and
diseases caused by overweight or underweight. In addition, people of normal weight tend to
stay in good health even after intense physical exertion.
                                                                ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-110) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif 24 < I <= 30:
                self.lbl_result.setText('Your BMI ' + result + ' - Overweight (preobesity)')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
It is enough to adjust the lifestyle, nutrition:

- Refuse any alcohol;
- Increase consumption of fruits, vegetables;
- Reduce the number of calories;
- Exercise at least 150 minutes per week.

Green, herbal teas, citrus fruits,
fermented milk products with a fat content of not more than 2.5%.

Fighting excess weight is hard work, so watch your diet, exercise,
move more and be healthy!
                                                        ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-110) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif 30 < I <= 35:
                self.lbl_result.setText('Your BMI ' + result + ' - Obesity 1 degree')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
Obesity requires more than just lifestyle changes. The doctor must find out the root of the problem, prescribe treatment.
The reason can be both banal overeating and hormonal failure.
Along with appropriate medications, taking vitamins for weight correction will be effective.
Their selection should be handled by the attending physician or nutritionist.

Fighting excess weight is hard work, so watch your diet, exercise,
move more and be healthy!  
''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-110) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif 35 < I < 40:
                self.lbl_result.setText('Your BMI ' + result + ' - Obesity 2 degree')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
In addition to correcting nutrition, physical activity, the doctor must prescribe treatment in accordance with the cause of obesity.
It can be both eating habits, an inactive lifestyle, and hormonal and endocrine diseases,
and in women, polycystic ovary syndrome.
In most cases, drugs are prescribed to normalize metabolism.

Fighting excess weight is hard work, so watch your diet, exercise,
move more and be healthy!
                                                            ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-110) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")
            elif I >= 40:
                self.lbl_result.setText('Your BMI ' + result + ' - Obesity 3 degree')
                self.lbl_result.setStyleSheet("QLabel{font: 10pt;}")
                self.vbox1.addWidget(self.lbl_recommendations)
                self.lbl_recommendations.setText('''
        Recommendation:
Defeating high obesity is possible only by a set of measures, by willpower. Requires drug therapy
aimed at eliminating the causes, concomitant diseases, as well as a gradual change in eating habits.

Fighting excess weight is hard work, so watch your diet, exercise,
move more and be healthy!
                                                            ''')
                self.lbl_recommendations.setStyleSheet("QLabel{font: 9pt;}")
                self.vbox1.addWidget(self.lbl_ideal)
                self.lbl_ideal.setText('Your ideal weight: ' + str(height-110) + ' kg')
                self.lbl_ideal.setStyleSheet("QLabel{font: 10pt;}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    lwind = LanWindow()
    mwind = MainWindow()
    ENmwind = ENMainWindow()
    IMTwind = IMTWindow()
    ENIMTwind = ENIMTWindow()
    lwind.show()
    sys.exit(app.exec_())

# Пример ввода для всех вариантов
'''
2m
1. 2
2. 80
3. 100
4. 120
5. 130
6. 150
7. 200
'''