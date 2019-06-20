import sys
from PyQt5.QtWidgets import QDialog, QApplication
from airfoil import *
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.b1.clicked.connect(self.predictions)
        self.show()

    def predictions(self):
        f1=float(self.ui.f1.text())
        a1=float(self.ui.a1.text())
        cl1=float(self.ui.cl1.text())
        fsv1=float(self.ui.fsv1.text())
        dt1=float(self.ui.dt1.text())
        data = pd.read_csv("airfoil_self_noise.dat",sep="\t",header=None)
        X_train,X_test,y_train,y_test = train_test_split(data.drop(5,axis=1),data[5],test_size=0.3)
        linreg = LinearRegression()
        linreg.fit(X_train,y_train)
        res = round(linreg.predict([[f1,a1,cl1,fsv1,dt1]])[0],2)
        self.ui.r1.setText(str(res))
        self.ui.r2.setText('3.90')

if __name__=="__main__":   
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
