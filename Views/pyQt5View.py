import sys
import time
from multiprocessing.pool import ThreadPool
from PyQt5.QtGui import QImage, QPalette, QBrush
import settings
from PyQt5 import QtCore, QtWidgets
from matplotlib import patches
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Models.Filters import *
from PyQt5.QtCore import QSize


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1000, 680)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        oImage = QImage("../oddetect.jpg")
        sImage = oImage.scaled(QSize(1000, 680))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.MainWindow.setPalette(palette)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 50, 131, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 80, 91, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 110, 111, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(150, 50, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(160, 20, 71, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setGeometry(QtCore.QRect(320, 20, 71, 22))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 21, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 80, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 80, 21, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 80, 21, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 80, 21, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 80, 21, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 80, 21, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 110, 111, 17))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(500, 110, 111, 17))
        self.label_8.setObjectName("label_8")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 80, 21, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 50, 75, 23))

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(500, 590, 75, 23))

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(400, 590, 75, 23))

        self.progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progress.setGeometry(QtCore.QRect(250, 630, 500, 20))

        self.pushButton.setObjectName("pushButton")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 21))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(lambda: self.get_filters())

        self.retranslateUi(MainWindow)
        self.m = PlotCanvas(main_df.head(1), MainWindow, width=5, height=3)  # why main_df.head(1)!!!!!!
        self.m.move(150, 150)
        self.pushButton1.clicked.connect(lambda: self.m.next_plot())
        self.pushButton2.clicked.connect(lambda: self.m.back_plot())
        self.checkBox_4.clicked.connect(
            lambda: self.m.squares() if self.checkBox_4.isChecked() else self.m.remove_squares())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Time Filter"))
        self.checkBox_2.setText(_translate("MainWindow", "Date Filter"))
        self.checkBox_3.setText(_translate("MainWindow", "Location Filter"))
        self.checkBox_4.setText(_translate("MainWindow", "Choose Boxs Filter"))
        self.label.setText(_translate("MainWindow", "Start Time"))
        self.label_2.setText(_translate("MainWindow", "End Time"))
        self.label_3.setText(_translate("MainWindow", "X1"))
        self.label_4.setText(_translate("MainWindow", "Y1"))
        self.label_5.setText(_translate("MainWindow", "X2"))
        self.label_6.setText(_translate("MainWindow", "Y2"))

        self.label_7.setText(_translate("MainWindow", "Paths number: "))
        self.label_8.setText(_translate("MainWindow", "0"))

        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton1.setText(_translate("MainWindow", "Next"))
        self.pushButton2.setText(_translate("MainWindow", "Back"))

        self.progress.hide()
        self.pushButton1.hide()
        self.pushButton2.hide()

    def get_filters(self):

        self.progress.show()
        self.progress.setValue(0)
        self.m.plot([])
        self.checkBox.setDisabled(True)
        self.checkBox_2.setDisabled(True)
        self.checkBox_3.setDisabled(True)
        self.checkBox_4.setDisabled(True)
        self.pushButton.setDisabled(True)
        self.pushButton1.setDisabled(True)
        self.pushButton2.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        self.dateEdit.setDisabled(True)
        self.timeEdit.setDisabled(True)
        self.timeEdit_2.setDisabled(True)
        QtCore.QCoreApplication.processEvents()

        dr = {}
        s = {}
        if self.checkBox.checkState() == 2:
            s1 = str(self.timeEdit.text()) + ":00"
            s["start_time"] = s1
            s1 = str(self.timeEdit_2.text()) + ":00"
            s["end_time"] = s1
            dr["time_filter"] = s
        if self.checkBox_2.checkState() == 2:
            s["date"] = str(self.dateEdit.text())
            dr["date_filter"] = s

        if self.checkBox_3.checkState() == 2:
            s["x1"] = int(self.lineEdit.text())
            s["y1"] = int(self.lineEdit_2.text())
            s["x2"] = int(self.lineEdit_3.text())
            s["y2"] = int(self.lineEdit_4.text())
            dr["location_filter"] = s
        if self.checkBox_4.checkState() == 2:
            s['set_of_coordinates'] = settings.set_of_coordinates
            dr['multi_location_filter'] = s

        print("Hiiiiiii!")
        df = Arguments_Receiver_And_Filter(dr)
        pool = ThreadPool(processes=4)
        result = pool.apply_async(df.arguments_receiver_and_filter)
        while not result.ready():
            QtCore.QCoreApplication.processEvents()

        dataframe = result.get()
        self.label_8.setText(str(len(dataframe.groupby(['filename', 'objectNum']).size())))
        x = len(dataframe.groupby(['filename', 'objectNum']).size())
        t = time.time()
        result = pool.apply_async(self.m.plot, (dataframe,))
        while not result.ready():
            self.progress.setValue((((time.time() - t) / 0.017) / x) * 100)
            QtCore.QCoreApplication.processEvents()
        print(time.time() - t)
        self.progress.setValue(100)
        self.pushButton1.show()
        self.pushButton2.show()
        print("Byeeeeee!")

        self.checkBox.setDisabled(False)
        self.checkBox_2.setDisabled(False)
        self.checkBox_3.setDisabled(False)
        self.checkBox_4.setDisabled(False)
        self.pushButton.setDisabled(False)
        self.pushButton1.setDisabled(False)
        self.pushButton2.setDisabled(False)
        self.lineEdit.setDisabled(False)
        self.lineEdit_2.setDisabled(False)
        self.lineEdit_3.setDisabled(False)
        self.lineEdit_4.setDisabled(False)
        self.dateEdit.setDisabled(False)
        self.timeEdit.setDisabled(False)
        self.timeEdit_2.setDisabled(False)
        settings.set_of_coordinates = set()


def start():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# *****************************************Omair classes*********************************

class PlotCanvas(FigureCanvas):

    def __init__(self, m, parent=None, width=5, height=4, dpi=140):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.objs = m.groupby(['filename', 'objectNum']).size()
        self.p = -1
        self.plot(m)
        self.color = ['red', 'black', 'blue', 'brown', 'green']

    def plot(self, pln):

        self.p = -1
        ax = self.figure.add_subplot(111)
        ax.cla()
        ax.imshow(settings.im.bg)
        ax.set_title('Draw Paths')
        print('xzzzzzzzzzzzzzzzz')
        if len(pln) > 0:
            self.objs = pln.groupby(['filename', 'objectNum']).size()
            for t, n in self.objs.iteritems():
                tn = time.time()
                o = settings.df_by_obj.loc[t]
                ax.plot(o.x, o.y)
                print(time.time() - tn, "********************", len(o), "&&&&&&&&&&&&&&&")

        self.draw()

    def next_plot(self):
        ax = self.figure.add_subplot(111)
        ax.set_title('Draw Paths')
        ax.cla()
        ax.imshow(settings.im.bg)
        if self.p == len(self.objs) - 1:
            self.p = self.p % (len(self.objs) - 1) - 1
        self.p += 1
        print(self.objs.index[self.p], "8888888888888888")
        o = settings.df_by_obj.loc[self.objs.index[self.p]]
        ax.plot(o.x, o.y, color=self.color[self.p % 5])

        self.draw()
        print(len(self.objs))

    def back_plot(self):
        if self.p == -1 or self.p == 0:
            self.p = len(self.objs)
        ax = self.figure.add_subplot(111)
        ax.set_title('Draw Paths')
        ax.cla()
        ax.imshow(settings.im.bg)
        self.p -= 1
        print(self.objs.index[self.p], "8888888888888888")
        o = settings.df_by_obj.loc[self.objs.index[self.p]]
        ax.plot(o.x, o.y, color=self.color[self.p % 5])
        self.draw()

    def squares(self):
        self.mpl_connect('button_press_event', self.onclick)
        ax = self.figure.add_subplot(111)

        ax.set_title('Draw Paths')
        ax.cla()
        ax.imshow(settings.im.bg)
        print("*******************************************************8")
        for x1 in range(0, settings.im.image_width, settings.im.image_width // 10):
            for y1 in range(0, settings.im.image_height,
                            settings.im.image_height // 10):
                ax.add_patch(
                    patches.Rectangle((x1, y1), settings.im.image_width // 10 -1, settings.im.image_height // 10 -1,
                                      linewidth=0.1, edgecolor='r',
                                      facecolor='none'))
        self.draw()

    def remove_squares(self):
        self.mpl_disconnect(self.mpl_connect('button_press_event', self.onclick))
        ax = self.figure.add_subplot(111)
        ax.set_title('Draw Paths')
        ax.cla()
        ax.imshow(settings.im.bg)
        self.draw()
        settings.set_of_coordinates = set()

    def onclick(self, event):
        print(event.xdata, event.ydata)
        x1 = (int(event.xdata) // (settings.im.image_width // 10)) * settings.im.image_width // 10
        y1 = (int(event.ydata) // (settings.im.image_height // 10)) * settings.im.image_height // 10
        x2 = x1 + settings.im.image_width // 10
        y2 = y1 + settings.im.image_height // 10
        settings.set_of_coordinates.add((x1, y1, x2, y2))
        listx = []
        listy = []
        s = []
        print(settings.set_of_coordinates)
        for x in range(x1, x2, 4):
            for y in range(y1, y2, 4):
                listx.append(x)
                listy.append(y)
                s.append(0.02)

        ax = self.figure.add_subplot(111)
        ax.scatter(listx, listy, s=s, color='#0B38A9')
        self.draw()
