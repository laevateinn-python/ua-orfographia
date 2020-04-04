import sys, os
import requests
import random
from bs4 import BeautifulSoup
from PySide2.QtWidgets import *
from PySide2.QtCore import QFile, QRect
from PySide2.QtGui import QIcon
from programs import Ui_MainWindow
from widget_answer import Ui_Form
from instruction import Ui_Dialog
from about import Ui_About
from settings import Ui_Settings
from my_parser import MyParser



ANSWER_LETTER = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
DATA_DIR = os.path.join(os.path.dirname(__file__),'data_dir')


class FileExport(QWidget):
    def __init__(self, data,row,words):
        super(FileExport, self).__init__()
        self.data = data
        self.row = row
        self.words = words
    def txt(self):
        p = QFileDialog.getSaveFileName(self,'SaveFile','відповідь','.txt')
        if len(self.data) == 1:
            with open(p[0]+p[1],'w') as f:
                f.write(str(self.data))
        else:
            with open(p[0]+p[1],'w') as f:
                for i in range(self.row):
                    f.write(str(self.data[i])+"\n")
                f.close()

    def json(self):
        p = QFileDialog.getSaveFileName(self,'SaveFile','відповідь','.json')
        if len(self.data) == 1:
            with open(p[0]+p[1],'w') as f:
                f.write("{\n")
                f.write("answer: ()\n}".format(self.data))
                f.close()
        else:
            with open(p[0]+p[1],'w') as f:
                f.write('{')
                for i in range(self.row):
                    f.write('"answer' + str([i]) + '" : "' + str(self.data[i])+'",\n')
                f.write("}")
                f.close()

class Another(QWidget):
    def __init__(self):
        super(Another, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    def instruction(self):
        self.show()

class About(QWidget):
    def __init__(self):
        super(About, self).__init__()
        self.ui = Ui_About()
        self.ui.setupUi(self)
    def about(self):
        self.show()

class Settings(QWidget):
    def __init__(self):
        super(Settings, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

    def show_set(self):
        self.show()


class AnswerWindow(QMainWindow):
    def __init__(self,row,words):
        super(AnswerWindow, self).__init__()
        self.ROW = row
        self.WORDS = words
        self.window = Ui_Form()
        self.window.setupUi(self)
        self.setWindowIcon(QIcon(DATA_DIR+'/icon.png'))
        self.setWindowTitle('Результат')

    def show_text(self,text):
        self.window.toolBox.hide()
        self.window.textBrowser.setText(self.right_output(text))
        self.show()

    def show_table(self,data):
        self.window.textBrowser.hide()
        for i in range(self.ROW):
            page = self.create_page()
            tab_widget = self.create_tab_widget(page)
            for j in range(self.WORDS):
                d = data[i][j]
                tab_widget.addTab(self.create_tab(self.create_table(d)),str(self.my_masive[i][j]))

            self.window.toolBox.addItem(page,str(ANSWER_LETTER[i]))

        self.show()

    def right_output(self,text):
        return '\n'.join([str(i) for i in text])

    def create_table(self,data):
        tableWidget = QTableWidget()
        tableWidget.setObjectName(u"tableWidget"+str(random.getrandbits(10)))
        tableWidget.setGeometry(QRect(100, 100, 401, 261))
        tableWidget.setRowCount(7)
        tableWidget.setColumnCount(2)

        name_col=["Однина","Множина"]
        for m in range(2):
            name = QTableWidgetItem(name_col[m])
            tableWidget.setHorizontalHeaderItem(m,name)
        for k in range(7):
            d = data[k]
            vid_name = QTableWidgetItem(d[0])
            if len(d) > 3:
                odnina = QTableWidgetItem(d[2])
                mnogina = QTableWidgetItem(d[3])
            else:
                odnina = QTableWidgetItem(d[1])
                mnogina = QTableWidgetItem(d[2])

            tableWidget.setVerticalHeaderItem(k,vid_name)
            tableWidget.setItem(k,0,odnina)
            tableWidget.setItem(k,1,mnogina)
        return tableWidget

    def create_tab(self,obj):
        tab = obj
        tab.setObjectName(u"tab_"+str(random.getrandbits(10)))
        return tab

    def create_page(self):
        page = QWidget()
        page.setObjectName(u"page_"+str(random.getrandbits(12)))
        page.setGeometry(QRect(0, 0, 681, 503))
        return page

    def create_tab_widget(self,bind):
        tabWidget = QTabWidget(bind)
        tabWidget.setObjectName(u"tabWidget_"+str(random.getrandbits(12)))
        tabWidget.setGeometry(QRect(10, 0, 661, 431))
        return tabWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(DATA_DIR+'/icon.png'))
        self.setWindowTitle('Програма для граматичного розбору слова, та вирішування тестів')
        self.ui.pushButton_solve.clicked.connect(self.solve)
        self.parser_obj = MyParser()
        self.another = Another()
        self.ab = About()
        self.settings  = Settings()
        self.ui.action.triggered.connect(self.another.instruction)
        self.ui.action_about.triggered.connect(self.ab.about)
        self.ui.action_3.triggered.connect(self.settings.show_set)
        self.settings.ui.checkBox.clicked.connect(self.hide_predict)

        self.show_message('Програма не гарантує 100% правильність відповіді')

    def hide_predict(self):
        self.ui.checkBox_predict.hide()
        self.ui.groupBox_predict.hide()


    def solve(self):
        self.ROW = int(self.ui.lineEdit_number_of_row.text())
        self.WORDS = int(self.ui.lineEdit_number_of_words.text())
        self.answer = AnswerWindow(self.ROW,self.WORDS)
        text = self.ui.plainTextEdit.toPlainText()
        massive = self.make_2d_massive(text)
        self.answer.my_masive = massive
        self.check_parameters(massive)
        self.export = FileExport(self.global_save,self.ROW,self.WORDS)
        self.ui.actionTXT.triggered.connect(self.export.txt)
        self.ui.actionJSON.triggered.connect(self.export.json)

    def check_parameters(self,massive):
        if self.ui.checkBox_predict.isChecked():
            if self.ui.radioButton_rid.isChecked():
                msg = 'Я думаю відповідь '
                self.show_message(msg+self.predict_by_rid(self.find_rid(massive),
                                    woman=self.ui.checkBox_2.isChecked(),
                                    man = self.ui.checkBox_3.isChecked(),
                                    ser = self.ui.checkBox_4.isChecked()))

            elif self.ui.radioButton_chislo.isChecked():
                msg = 'Я думаю відповідь '
                self.show_message(msg + self.predict_by_chislo(self.find_chislo(self.find_vidminok(massive),massive),
                                                                mnog = self.ui.radioButton_5.isChecked(),
                                                                odni = self.ui.radioButton_6.isChecked()))

            elif self.ui.radioButton_vidmina.isChecked():
                msg = 'Я думаю відповідь '
                self.show_message(msg + self.predict_by_vidmina(self.find_vidmina(massive),
                                        a0 = self.ui.checkBox_vidm_1.isChecked(),
                                        a1 = self.ui.checkBox_vidm_2.isChecked(),
                                        a2 = self.ui.checkBox_vidm_3.isChecked(),
                                        a3 = self.ui.checkBox_vidm_4.isChecked()))
            else:
                self.show_message("Виберіть що хочете знайти")
        else:
            if self.ui.radioButton_rid.isChecked():
                self.answer.show_text(self.find_rid(massive))
            elif self.ui.radioButton_chislo.isChecked():
                self.answer.show_text(self.find_chislo(self.find_vidminok(massive),massive))
            elif self.ui.radioButton_vidminok.isChecked():
                self.answer.show_table(self.find_vidminok(massive))
            elif self.ui.radioButton_vidmina.isChecked():
                self.answer.show_text(self.find_vidmina(massive))
            else:
                self.show_message("Виберіть що хочете знайти")

    def show_message(self,answ):
        self.ui.msg.setText(str(answ))
        self.ui.msg.show() #print answer

    def make_2d_massive(self,PText):
        txt = PText.split('\n')
        l = []
        for n in range(len(txt)): #make 2d massive
            l.append(txt[n].split(","))
        for k in range(len(txt)): # delete upper letter
            text = l[k][0]
            text = text[1:len(text)]
            l[k][0] = text
        for i in range(self.ROW): #delete space in front of
            for j in range(self.WORDS):
                text = l[i][j]
                text = text[1:len(l[i][j])]
                l[i][j] = text
        return(l)

#--------------------------- find block ---------------------------------------
    def find_rid(self,massive):
        res = []
        for i in range(self.ROW):
            n = []
            for j in range(self.WORDS):
                try:
                    html = self.parser_obj.get_html("https://slovnyk.ua/index.php?swrd={}".format(massive[i][j]))
                    tmp = self.parser_obj.parse_word_data(html)[1]
                    tmp = tmp[1:len(tmp)-4]
                    n.append(tmp)
                except:
                    n.append("Слова немає в базі")
            res.append(n)
        self.global_save = res
        return(res)

    def find_vidminok(self,massive):
        res = []
        for i in range(self.ROW):
            n = []
            for j in range(self.WORDS):
                try:
                    html = self.parser_obj.get_html("https://slovnyk.ua/index.php?swrd={}".format(massive[i][j]))
                    n.append(self.parser_obj.parse_word_vidminok(html))
                except:
                    mb = []
                    for b in range(7):
                        mb.append(["Слова немає в базі","X","X"])
                    n.append(mb)
            res.append(n)
        self.global_save = res
        return res

    def find_chislo(self,massive,massive2):
        odnina = []
        mnogina = []
        res = []
        for i in range(self.ROW):
            n = []
            for j in range(self.WORDS):
                d = massive[i][j]
                wrd = massive2[i][j]
                for k in range(len(d)):
                    odnina.append(d[k][1])
                    mnogina.append(d[k][len(d[k])-1])
                if wrd in odnina:
                    n.append("Однина")
                elif wrd in mnogina:
                    n.append("Множина")
                else:
                    n.append("Слова немає в базі")
            res.append(n)
        self.global_save = res
        return res

    def find_vidmina(self,massive):
        vidminok = self.find_vidminok(massive)
        rid = self.find_rid(massive)
        res = []
        for i in range(self.ROW):
            n = []
            for j in range(self.WORDS):
                d = vidminok[i][j]
                if rid[i][j] == 'чоловічий':
                    if d[0][1][len(d[0][1])-1] == 'а':
                        n.append("1 відміна")
                    elif d[0][1][len(d[0][1])-1] == 'я':
                        n.append("1 відміна")
                    else:
                        n.append("2 відміна")
                elif rid[i][j] == 'жіночий':
                    if d[0][1][len(d[0][1])-1] == 'а':
                        n.append("1 відміна")
                    elif d[0][1][len(d[0][1])-1] == 'я':
                        n.append("1 відміна")
                    else:
                        n.append("3 відміна")
                elif rid[i][j] == 'середній':
                    count = 0
                    for bn in range(7):
                        if 'ат' in d[bn][1]:
                            count += 1
                        elif 'ят' in d[bn][1]:
                            count += 1
                        elif 'ен' in d[bn][1]:
                            count += 1
                    if count:
                        n.append("4 відміна")
                    else:
                        n.append("2 відміна")
                else:
                    n.append("X")
            res.append(n)
        self.global_save = res
        return(res)

#--------------------------- predict block ------------------------------------
    def predict_by_rid(self,data,**params):
        l = []
        if params['woman']:
            l.append("жіночий")
        if params['man']:
            l.append("чоловічий")
        if params['ser']:
            l.append("середній")
        if len(l) > 1:
            if l[0] == 'жіночий':
                if l[1] == 'чоловічий':
                    l.append("чоловічий і жіночий")
        res = []
        for i in range(self.ROW):
            count = 0
            for j in range(self.WORDS):
                if data[i][j] in l:
                    count +=1
            res.append(count)
        answer = ANSWER_LETTER[res.index(max(res))]
        self.global_save = answer
        return(answer)

    def predict_by_chislo(self,data,**params):
        l =[]
        if params['mnog']:
            l.append("Множина")
        if params['odni']:
            l.append("Однина")
        res = []
        for i in range(self.ROW):
            count = 0
            for j in range(self.WORDS):
                if data[i][j] in l:
                    count += 1
            res.append(count)
        answer = ANSWER_LETTER[res.index(max(res))]
        self.global_save = answer
        return(answer)

    def predict_by_vidmina(self,data,**params):
        l = []
        for k in range(4):
            if params["a"+str(k)]:
                l.append(str(k+1)+ " відміна")
        res = []
        for i in range(self.ROW):
            count = 0
            for j in range(self.WORDS):
                if data[i][j] in l:
                    count += 1
            res.append(count)
        answer = ANSWER_LETTER[res.index(max(res))]
        self.global_save = answer
        return(answer)








#------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()

    sys.exit(app.exec_())
