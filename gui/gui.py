# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
from editorFrame import Ui_MainWindow

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
        MainWindow.resize(542, 421)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.submitQuery_btn = QtGui.QPushButton(self.centralwidget)
        self.submitQuery_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.submitQuery_btn.setObjectName(_fromUtf8("submitQuery_btn"))
        self.gridLayout.addWidget(self.submitQuery_btn, 7, 2, 1, 1)
        self.results_output = QtGui.QListView(self.centralwidget)
        self.results_output.setObjectName(_fromUtf8("results_output"))
        self.gridLayout.addWidget(self.results_output, 0, 0, 4, 3)
        self.directory_btn = QtGui.QToolButton(self.centralwidget)
        self.directory_btn.setObjectName(_fromUtf8("directory_btn"))
        self.gridLayout.addWidget(self.directory_btn, 4, 2, 1, 1)
        self.textQuery_input = QtGui.QLineEdit(self.centralwidget)
        self.textQuery_input.setObjectName(_fromUtf8("textQuery_input"))
        self.gridLayout.addWidget(self.textQuery_input, 7, 1, 1, 1)
        self.createIndex_btn = QtGui.QPushButton(self.centralwidget)
        self.createIndex_btn.setObjectName(_fromUtf8("createIndex_btn"))
        self.gridLayout.addWidget(self.createIndex_btn, 6, 2, 1, 1)
        self.union_rdb = QtGui.QRadioButton(self.centralwidget)
        self.union_rdb.setObjectName(_fromUtf8("union_rdb"))
        self.gridLayout.addWidget(self.union_rdb, 6, 0, 1, 1)
        self.phrase_rdb = QtGui.QRadioButton(self.centralwidget)
        self.phrase_rdb.setObjectName(_fromUtf8("phrase_rdb"))
        self.gridLayout.addWidget(self.phrase_rdb, 4, 0, 1, 1)
        self.intersection_rdb = QtGui.QRadioButton(self.centralwidget)
        self.intersection_rdb.setObjectName(_fromUtf8("intersection_rdb"))
        self.gridLayout.addWidget(self.intersection_rdb, 7, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Search Engine Project", None))
        self.submitQuery_btn.setText(_translate("MainWindow", "Submit", None))
        self.directory_btn.setText(_translate("MainWindow", "Change Directory", None))
        self.createIndex_btn.setText(_translate("MainWindow", "Create Index", None))
        self.union_rdb.setText(_translate("MainWindow", "Union", None))
        self.phrase_rdb.setText(_translate("MainWindow", "Phrase", None))
        self.intersection_rdb.setText(_translate("MainWindow", "Intersection", None))

