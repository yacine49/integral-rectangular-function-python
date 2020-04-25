from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtWidgets  import * 
from  PyQt5.uic  import  loadUi
from scipy.integrate import quad   
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
from  matplotlib.backends.backend_qt5agg  import  FigureCanvas
from  matplotlib.figure  import  Figure
import matplotlib.pyplot as plt
import matplotlib
import math
import pandas as pd
import matplotlib.patches as plp
import  numpy  as  np 
class  MplWidget ( QWidget ):
    
    def  __init__ ( self ,  parent  =  None ):

        QWidget . __init__ ( self ,  parent )
        
        self . canvas  =  FigureCanvas ( Figure ())
        
        vertical_layout  =  QVBoxLayout () 
        vertical_layout . addWidget ( self . canvas )
        
        self . canvas . axes  =  self . canvas . figure . add_subplot ( 111 ) 
        self . setLayout ( vertical_layout )

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 508)
        MainWindow.setStyleSheet(" background-color: white; color: white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(0, 0, 591, 481))
        self.MplWidget.setObjectName("MplWidget")
        self.fline = QtWidgets.QLineEdit(self.centralwidget)
        self.fline.setGeometry(QtCore.QRect(790, 28, 41, 33))
        self.fline.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fline.setStyleSheet(" background-color: white; color: black")
        self.fline.setInputMask("")
        self.fline.setText("")
        self.fline.setAlignment(QtCore.Qt.AlignCenter)
        self.fline.setPlaceholderText("")
        self.fline.setClearButtonEnabled(False)
        self.fline.setObjectName("fline")
        self.dline = QtWidgets.QLineEdit(self.centralwidget)
        self.dline.setGeometry(QtCore.QRect(660, 28, 41, 33))
        self.dline.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.dline.setStyleSheet(" background-color: white; color: black")
        self.dline.setText("")
        self.dline.setAlignment(QtCore.Qt.AlignCenter)
        self.dline.setObjectName("dline")
        self.x3 = QtWidgets.QRadioButton(self.centralwidget)
        self.x3.setGeometry(QtCore.QRect(780, 160, 81, 31))
        self.x3.setStyleSheet(" background-color: white; color: white")
        self.x3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Screenshot from 2020-04-21 03-52-04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x3.setIcon(icon)
        self.x3.setIconSize(QtCore.QSize(50, 50))
        self.x3.setObjectName("x3")
        self.exp = QtWidgets.QRadioButton(self.centralwidget)
        self.exp.setGeometry(QtCore.QRect(780, 200, 81, 31))
        self.exp.setStyleSheet(" background-color: white; color: white")
        self.exp.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Screenshot from 2020-04-21 04-03-03.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exp.setIcon(icon1)
        self.exp.setIconSize(QtCore.QSize(50, 50))
        self.exp.setObjectName("exp")
        self.draw = QtWidgets.QPushButton(self.centralwidget)
        self.draw.setGeometry(QtCore.QRect(690, 250, 100, 31))
        self.draw.setObjectName("draw")
        self.Nrect = QtWidgets.QLineEdit(self.centralwidget)
        self.Nrect.setGeometry(QtCore.QRect(630, 160, 81, 31))
        self.Nrect.setStyleSheet(" background-color: white; color: black")
        self.Nrect.setAlignment(QtCore.Qt.AlignCenter)
        self.Nrect.setObjectName("Nrect")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 110, 151, 31))
        self.label.setStyleSheet(" background-color: white; color: black")
        self.label.setObjectName("label")
        self.Srectup = QtWidgets.QLabel(self.centralwidget)
        self.Srectup.setGeometry(QtCore.QRect(600, 300, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Srectup.setFont(font)
        self.Srectup.setStyleSheet(" background-color: white; color: black")
        self.Srectup.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Srectup.setObjectName("Srectup")
        self.integral = QtWidgets.QLabel(self.centralwidget)
        self.integral.setGeometry(QtCore.QRect(590, 370, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.integral.setFont(font)
        self.integral.setStyleSheet(" background-color: white; color: black")
        self.integral.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.integral.setObjectName("integral")
        self.Percentage = QtWidgets.QLabel(self.centralwidget)
        self.Percentage.setGeometry(QtCore.QRect(680, 400, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Percentage.setFont(font)
        self.Percentage.setStyleSheet(" background-color: white; color: blue")
        self.Percentage.setText("")
        self.Percentage.setAlignment(QtCore.Qt.AlignCenter)
        self.Percentage.setObjectName("Percentage")
        self.Srectup2 = QtWidgets.QLabel(self.centralwidget)
        self.Srectup2.setGeometry(QtCore.QRect(780, 300, 91, 31))
        self.Srectup2.setStyleSheet(" background-color: white; color: black")
        self.Srectup2.setText("")
        self.Srectup2.setAlignment(QtCore.Qt.AlignCenter)
        self.Srectup2.setObjectName("Srectup2")
        self.integral2 = QtWidgets.QLabel(self.centralwidget)
        self.integral2.setGeometry(QtCore.QRect(780, 370, 91, 31))
        self.integral2.setStyleSheet(" background-color: white; color: black")
        self.integral2.setText("")
        self.integral2.setAlignment(QtCore.Qt.AlignCenter)
        self.integral2.setObjectName("integral2")
        self.Srectdown = QtWidgets.QLabel(self.centralwidget)
        self.Srectdown.setGeometry(QtCore.QRect(600, 330, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Srectdown.setFont(font)
        self.Srectdown.setStyleSheet(" background-color: white; color: black")
        self.Srectdown.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Srectdown.setObjectName("Srectdown")
        self.Srectdown2 = QtWidgets.QLabel(self.centralwidget)
        self.Srectdown2.setGeometry(QtCore.QRect(780, 330, 91, 31))
        self.Srectdown2.setStyleSheet(" background-color: white; color: black")
        self.Srectdown2.setText("")
        self.Srectdown2.setAlignment(QtCore.Qt.AlignCenter)
        self.Srectdown2.setObjectName("Srectdown2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 30, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(" background-color: white; color: black")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.x2 = QtWidgets.QRadioButton(self.centralwidget)
        self.x2.setGeometry(QtCore.QRect(780, 120, 81, 31))
        self.x2.setStyleSheet(" background-color: white; color: white")
        self.x2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Screenshot from 2020-04-21 05-47-15.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x2.setIcon(icon2)
        self.x2.setIconSize(QtCore.QSize(50, 50))
        self.x2.setObjectName("x2")
        self.lnx = QtWidgets.QRadioButton(self.centralwidget)
        self.lnx.setGeometry(QtCore.QRect(780, 80, 81, 31))
        self.lnx.setStyleSheet(" background-color: white; color: white")
        self.lnx.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Screenshot from 2020-04-21 05-47-49.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lnx.setIcon(icon3)
        self.lnx.setIconSize(QtCore.QSize(50, 50))
        self.lnx.setObjectName("lnx")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(670, 0, 151, 21))
        self.label_3.setStyleSheet(" background-color: white; color: black")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(830, 410, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(" background-color: white; color: black")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 919, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
##########################################################################################################################################################
        #self . setWindowTitle ( "Fonction Escalier" )
        self.x3.setChecked(True)
        try:
            self.draw.clicked.connect(self.update_graph)
        except:
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Erreur')
            msg.setText("Erreur intervalle est hors du domain de la definition")

        #self . addToolBar ( NavigationToolbar ( self . MplWidget . canvas ,  self ))
        self.Nrect.returnPressed.connect(self.update_graph)
        


    def  update_graph ( self ):
        rect_up=0
        rect_down=0
        self.MplWidget.canvas.axes.clear()
        d = float(self.dline.text()) ; f =float(self.fline.text()) 
        n=int(self.Nrect.text())      
        def do(x):
            if self.x3.isChecked():
                return x**3
            if self.exp.isChecked():
                return math.exp(x)
            if self.lnx.isChecked():
                return math.log(x)
            if self.x2.isChecked():
                return x**2
        x  = np.arange(d,f+(f-d)/100,(f-d)/100)
        y = pd.DataFrame(x,index=None,columns=['y'])
        y  = y['y'].apply(lambda x: do(x))
        fig,ax = plt.subplots(nrows=1,ncols=1)
        self.MplWidget.canvas.axes.plot(x,y,color='black')
        step=0
        for i in range(n):
            z =d+step+(f-d)/n
            if z > f :
                z= f
            self.MplWidget.canvas.axes.add_patch(plp.Rectangle((d+step,0),(f-d)/n,do(z),color='#FF3333',fill=False))
            rect_up += ((f-d)/n)*do(z)
            self . MplWidget.canvas.axes.add_patch(plp.Rectangle((d+step,0),(f-d)/n,do(d+step),color='#B5FF33',fill=False))
            rect_down+= ((f-d)/n)*do(d+step)
            step += (f-d)/n
        self . MplWidget . canvas . draw ()
        up = '%.2f'%(rect_up)
        self.Srectup2.setText("{}".format(up))
        down = '%.2f'%(rect_down)
        self.Srectdown2.setText("{}".format(down))
        h = quad(do,d,f)[0]
        p = (rect_up - rect_down)*100/h
        h= '%.2f'% (h)
        self.integral2.setText("{}".format(h))
        p = '%.2f'%p
        self.Percentage.setText("{}%".format(p))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.draw.setText(_translate("MainWindow", "Dessiner"))
        self.label.setText(_translate("MainWindow", "Nombre de rectangle"))
        self.Srectup.setText(_translate("MainWindow", "Rectangles rouges"))
        self.integral.setText(_translate("MainWindow", "Intégrale"))
        self.Srectdown.setText(_translate("MainWindow", " Rectangles verts"))
        self.label_2.setText(_translate("MainWindow", "----->"))
        self.label_3.setText(_translate("MainWindow", "Intervalle"))
        self.label_4.setText(_translate("MainWindow", "Flici.Yacine"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
