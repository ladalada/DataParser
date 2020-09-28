from PyQt5.QtGui import QIcon

from parsers.parser_DOCX import document_parser
from parsers.parser_HTML import html_text, html_links
from parsers.parser_PDF import pdf_parser
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from style2 import Ui_MainWindow
from tkinter import filedialog as fd, Tk
import sys


def get_document_type(document_link):
    filename, file_extension = os.path.splitext(document_link)
    if file_extension == '.pdf':
        return 'pdf'
    elif file_extension == '.docx':
        return 'docx'
    else:
        return f'{file_extension} - wrong document type'


def get_links():
    link = ui.lineEdit_Link.text()
    try:
        ui.label_Data.setText("Links:\n" + html_links(link))
        try:
            save_to_file(ui.lineEdit_SaveTo.text(), "Links:\n" + html_links(link))
        except:
            ui.lineEdit_SaveTo.setText("Fill in this line to save to file")
    except:
        if len(link) > 0:
            ui.label_Data.setText("Wrong html link")
        else:
            ui.lineEdit_Link.setText("Fill in this line!")


def get_data():
    data_type = ui.comboBox_Type.currentIndex()
    link = ui.lineEdit_Link.text()

    #HTML
    if data_type == 0:
        try:
            if len(link) > 0:
                ui.label_Data.setText(html_text(link))
                try:
                    save_to_file(ui.lineEdit_SaveTo.text(), html_text(link))
                except:
                    ui.lineEdit_SaveTo.setText("Fill in this line to save to file")
            else:
                ui.lineEdit_Link.setText("Fill in this line!")
        except:
            ui.label_Data.setText("Wrong html link")

    #Documents
    elif data_type == 1:

        if len(link) > 0:
            try:
                document_type = get_document_type(link)
                if document_type == 'pdf':
                    try:
                        text = pdf_parser(link)
                        ui.label_Data.setText(text)
                    except:
                        ui.label_Data.setText("Wrong pdf document")
                elif document_type == 'docx':
                    try:
                        text = document_parser(link)
                        ui.label_Data.setText(text)
                    except:
                        ui.label_Data.setText("Wrong docx document")

                else:
                    ui.label_Data.setText(document_type)
            except:
                ui.label_Data.setText("Wrong document link")
        else:
            ui.lineEdit_Link.setText("Fill in!")


def save_to_file(file_name, data):
    f = open(file_name, 'w', encoding='utf-8')
    f.write(data)
    f.close()


def selectParsingPath():
    Tk().withdraw()
    file_name = fd.askopenfilename(filetypes=(("PDF", "*.pdf"),
                                              ("DOCX files", "*.docx")
                                              ))
    ui.lineEdit_Link.setText(file_name)


def insertParsingPath():
    Tk().withdraw()
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("All files", "*.*")))
    if len(file_name.split('.')) == 2:
        ui.lineEdit_SaveTo.setText(file_name)
    else:
        ui.lineEdit_SaveTo.setText(file_name + ".txt")


def change_type(e):
    if e == 0:
        ui.lineEdit_Link.setText("")
        ui.label_Data.setText("The result will be displayed here...")
        ui.pushButton_LinkPath.hide()
        ui.label_SaveTo.show()
        ui.lineEdit_SaveTo.show()
        ui.pushButton_SavePath.show()
        ui.pushButton_GetLinks.show()
        # documents
    elif e == 1:
        ui.lineEdit_Link.setText("")
        ui.label_Data.setText("The result will be displayed here...")
        ui.pushButton_LinkPath.show()
        ui.label_SaveTo.hide()
        ui.lineEdit_SaveTo.hide()
        ui.pushButton_SavePath.hide()
        ui.pushButton_GetLinks.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QIcon('icon.jpg'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_LinkPath.hide()
    ui.comboBox_Type.currentIndexChanged.connect(change_type)
    ui.pushButton_GetLinks.clicked.connect(get_links)
    ui.pushButton_SavePath.clicked.connect(insertParsingPath)
    ui.pushButton_LinkPath.clicked.connect(selectParsingPath)
    ui.pushButton_GetData.clicked.connect(get_data)

    MainWindow.show()
    sys.exit(app.exec_())
