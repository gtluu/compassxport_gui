# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Gordon\PycharmProjects\compassxport_gui\compassxport_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
import io
import subprocess
import ConfigParser

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(382, 431)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 291, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 120, 291, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 50, 31, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 120, 31, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 190, 341, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 260, 341, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 340, 81, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)		
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 383, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuOptions = QtGui.QMenu(self.menuBar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionChange_CompassXport_exe_Location = QtGui.QAction(MainWindow)
        self.actionChange_CompassXport_exe_Location.setObjectName(_fromUtf8("actionChange_CompassXport_exe_Location"))
        self.menuOptions.addAction(self.actionChange_CompassXport_exe_Location)
        self.menuBar.addAction(self.menuOptions.menuAction())

        self.args = {}
        self.path = ''

        self.retranslateUi(MainWindow)

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.get_input_path)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.get_output_path)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL('clicked()'), self.convert)
        QtCore.QObject.connect(self.actionChange_CompassXport_exe_Location, QtCore.SIGNAL('triggered()'), self.get_file)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_file(self):
        exe = QtGui.QFileDialog.getOpenFileName(None, 'Select Directory', 'C:\\')
        exe = str(exe).replace('/', '\\')
        config = ConfigParser.RawConfigParser()
        config.add_section('compassxport')
        config.set('compassxport', 'path', exe)
        with open(os.path.dirname(__file__) + '/config.ini', 'w') as config_file:
            config.write(config_file)

    def get_input_path(self):
        sample_directory = QtGui.QFileDialog.getExistingDirectory(None, 'Select File/Directory', 'C:\\')
        sample_directory = str(sample_directory).replace('/', '\\')
        self.lineEdit.setText(sample_directory)

    def get_output_path(self):
        sample_directory = QtGui.QFileDialog.getExistingDirectory(None, 'Select Directory', 'C:\\')
        sample_directory = str(sample_directory).replace('/', '\\')
        self.lineEdit_2.setText(sample_directory)

    def get_compassxport_path(self):
        with open(os.path.dirname(__file__) + '/config.ini', 'r') as config_file:
            config = config_file.read()
        config_parser = ConfigParser.RawConfigParser(allow_no_value=True)
        config_parser.readfp(io.BytesIO(config))
        for param in config_parser.sections():
            if param == 'compassxport':
                for option in config_parser.options(param):
                    if option == 'path':
                        self.path = config_parser.get(param, option)
                        if not os.path.isfile(self.path):
                            error_box = QtGui.QMessageBox()
                            error_box.setText('Error: CompassXportConsole.exe not found. Verify config.ini path.')
                            error_box.setWindowTitle('CompassXport GUI Wrapper')
                            error_box.exec_()

    def get_args(self):
        if self.lineEdit.text().endsWith('.d'):
            self.args['a'] = str(self.lineEdit.text()) + '\\analysis.baf'
        else:
            self.args['multi'] = str(self.lineEdit.text())
        self.args['o'] = str(self.lineEdit_2.text())
        self.args['raw'] = str(self.comboBox.currentText())
        if self.args['raw'] == 'Centroided/Line':
            self.args['raw'] = '0'
        elif self.args['raw'] == 'Profile':
            self.args['raw'] = '1'
        self.args['mode'] = str(self.comboBox_2.currentText())
        if self.args['mode'] == 'mzXML':
            self.args['mode'] = '0'
        elif self.args['mode'] == 'mzData':
            self.args['mode'] = '1'
        elif self.args['mode'] == 'mzML':
            self.args['mode'] = '2'
        elif self.args['mode'] == 'JCAMP':
            self.args['mode'] = '3'
        elif self.args['mode'] == 'CSV':
            self.args['mode'] = '4'
        if self.checkBox.isChecked():
            self.args['log'] = 'all'
        else:
            self.args['log'] = 'none'

    def convert(self):
        self.get_args()
        self.get_compassxport_path()
        if os.path.isfile(self.path):
            cmd = '"' + self.path + '" '
            for key, value in self.args.iteritems():
                cmd += '-' + key + ' '
                if ' ' in value:
                    cmd += '"' + value + '" '
                else:
                    cmd += value + ' '
            subprocess.call(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CompassXport GUI Wrapper", None))
        self.label.setText(_translate("MainWindow", "Input Directory", None))
        self.label_2.setText(_translate("MainWindow", "Output Directory", None))
        self.pushButton.setText(_translate("MainWindow", "...", None))
        self.pushButton_2.setText(_translate("MainWindow", "...", None))
        self.label_3.setText(_translate("MainWindow", "Peaks", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Centroided/Line", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Profile", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "mzXML", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "mzData", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "mzML", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "JCAMP", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "CSV", None))
        self.label_4.setText(_translate("MainWindow", "Output Format", None))
        self.checkBox.setText(_translate("MainWindow", "Verbose", None))
        self.pushButton_3.setText(_translate("MainWindow", "Run", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.actionChange_CompassXport_exe_Location.setText(
            _translate("MainWindow", "Change CompassXport.exe Location", None))


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
