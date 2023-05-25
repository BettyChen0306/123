from PyQt5.QtWidgets import * #輸入QT裡的所有東西 "*"->引入模組內所有的class，此方法會有風險，如果未來有相同模組相同名稱 就會ERROR
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from maindow_calculator_plus import Ui_Dialog #將Main window 引入Ui
import sys 

def clicked_hello():
    print(ui.comboBox.currentText())
    print(ui.comboBox.currentIndex())
    ui.progressBar.setValue(20)

def go_count():
    x = ui.lineEdit.text()#將lineEdit的輸入存入x中
    y = ui.lineEdit_2.text()#將lineEdit的輸入存入x中
    if is_float(x) and is_float(y):  
        if ui.radioButton_Add.isChecked():
            ans = float(x)+float(y)
            ui.label_3.setText("+")
        elif ui.radioButton_Sub.isChecked():
            ans = float(x)-float(y)
            ui.label_3.setText("-")
        elif ui.radioButton_Multi.isChecked():
            ans = float(x)*float(y)
            ui.label_3.setText("*")
        elif ui.radioButton_Divs.isChecked():
            try:
                ans = float(x)/float(y)
            except:
                message = QMessageBox() #跳出額外視窗，需設定文字左上角/中間
                message.setWindowTitle(" Error!!! ") #
                message.setInformativeText(" 不可除以0 ")
                message.exec_() #啟動     
                return             
            ui.label_3.setText("/")

        print(ans)
        ans_text=check_comboBox()
        ui.label.setText(str(ans_text)+str(ans))

        return ans

    else:
        message = QMessageBox() #跳出額外視窗，需設定文字左上角/中間
        message.setWindowTitle(" Error!!! ") #
        message.setInformativeText(" 請輸入數字 ")
        message.exec_() #啟動  
        return

def check_comboBox():
    if ui.comboBox.currentText()== "中文":
        ans_text="答案是"
        # ui.label.setText("答案是")
    elif ui.comboBox.currentText()== "英文":
        ans_text="The Answer is"
        # ui.label.setText("The Answer is")
    elif ui.comboBox.currentText()== "日文":
        ans_text="答えは"
        # ui.label.setText("答えは") 
    return ans_text
                
def check_box():
    ui.lineEdit.text,ui.lineEdit_2.text =ui.lineEdit_2.text,ui.lineEdit.text

def is_float(num):
    try:
        float(num)
        return True
    except:
        return False

def silder_change():
    x=ui.horizontalSlider.value() #數值為int
    ui.progressBar.setValue(x)

def silder_release():
    answer=go_count()
    if is_float(answer):
        # message = QMessageBox() #跳出額外視窗，需設定文字左上角/中間
        # message.setWindowTitle(" show ") #
        # message.setInformativeText(" 選擇的數值為 "+str(ui.horizontalSlider.value()))
        # message.exec_() #啟動 
        multiValue=ui.horizontalSlider.value()
        ui.label_5.setText("拉霸數值為 "+str(multiValue))
        ui.label_6.setText("相乘後數值為 "+ str(multiValue*answer))
        print(multiValue*answer)
        ans_text=check_comboBox()
        ui.label.setText(str(ans_text)+str(multiValue*answer))
        ui.progressBar.setValue(int(multiValue))
    else:
        return


app = QApplication(sys.argv) #系統呼叫sys.argv 固定格式
widge = QWidget()#固定格式


#注意!!要放在Qwidget後面
t=QTranslator()#引入翻譯檔
t.load("chinese.qm")#匯入翻譯檔
app.installTranslator(t) #安裝置app中  
#注意!!要放在setup前面


ui = Ui_Dialog()#固定格式
ui.setupUi(widge)#固定格式



group1 = QButtonGroup(widge)
group1.addButton(ui.radioButton_Add)
group1.addButton(ui.radioButton_Sub)
group1.addButton(ui.radioButton_Multi)
group1.addButton(ui.radioButton_Divs)

ui.checkBox.clicked.connect(check_box)
ui.radioButton_Add.clicked.connect(go_count)
ui.radioButton_Sub.clicked.connect(go_count)
ui.radioButton_Multi.clicked.connect(go_count)
ui.radioButton_Divs.clicked.connect(go_count)

ui.pushButton.clicked.connect(go_count)

#拉霸
ui.progressBar.setMaximum(100) #設定最大值
ui.progressBar.setMinimum(0) #設定最小值
ui.progressBar.setValue(1) #設定起始數值

#滑動bar
ui.horizontalSlider.setMaximum(100)
ui.horizontalSlider.setMinimum(0)
ui.horizontalSlider.valueChanged.connect(silder_change) #移動時，會一直呼叫
ui.horizontalSlider.sliderReleased.connect(silder_release)


#下拉式選單
# ui.comboBox.addItems(["cat","dog","bird"])
# ui.pushButton_2.clicked.connect(clicked_hello)

ui.comboBox.addItems(["中文","英文","日文","-"])
# ui.pushButton_2.clicked.connect(change_Lan_strButton)

# ui.comboBox.activated.connect(change_Lan_combo)
# 


widge.show()#設定要在此程式碼之上
sys.exit(app.exec()) #執行完後，回傳一值回去、固定格式


