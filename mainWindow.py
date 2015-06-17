# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Mon Jun  8 11:19:36 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(601, 356)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/app-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabContainer = QtGui.QTabWidget(self.centralwidget)
        self.tabContainer.setGeometry(QtCore.QRect(0, 0, 601, 311))
        self.tabContainer.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabContainer.setObjectName("tabContainer")
        self.t1 = QtGui.QWidget()
        self.t1.setAutoFillBackground(False)
        self.t1.setObjectName("t1")
        self.columnView = QtGui.QColumnView(self.t1)
        self.columnView.setGeometry(QtCore.QRect(0, 0, 601, 281))
        self.columnView.setObjectName("columnView")
        self.tabContainer.addTab(self.t1, "")
        self.t2 = QtGui.QWidget()
        self.t2.setObjectName("t2")
        self.tabContainer.addTab(self.t2, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)
        self.menuMain = QtGui.QMenuBar(mainWindow)
        self.menuMain.setGeometry(QtCore.QRect(0, 0, 601, 25))
        self.menuMain.setObjectName("menuMain")
        self.menuMain_2 = QtGui.QMenu(self.menuMain)
        self.menuMain_2.setObjectName("menuMain_2")
        self.menuTools = QtGui.QMenu(self.menuMain)
        self.menuTools.setObjectName("menuTools")
        self.menuAbout = QtGui.QMenu(self.menuMain)
        self.menuAbout.setObjectName("menuAbout")
        mainWindow.setMenuBar(self.menuMain)
        self.actionAdd = QtGui.QAction(mainWindow)
        self.actionAdd.setIcon(icon)
        self.actionAdd.setObjectName("actionAdd")
        self.actionDelete = QtGui.QAction(mainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSave = QtGui.QAction(mainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtGui.QAction(mainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionAbout_sAB = QtGui.QAction(mainWindow)
        self.actionAbout_sAB.setObjectName("actionAbout_sAB")
        self.actionClose = QtGui.QAction(mainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionTools = QtGui.QAction(mainWindow)
        self.actionTools.setObjectName("actionTools")
        self.actionLoad_2 = QtGui.QAction(mainWindow)
        self.actionLoad_2.setObjectName("actionLoad_2")
        self.actionSave_2 = QtGui.QAction(mainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionExit = QtGui.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd_2 = QtGui.QAction(mainWindow)
        self.actionAdd_2.setObjectName("actionAdd_2")
        self.actionDelete_2 = QtGui.QAction(mainWindow)
        self.actionDelete_2.setObjectName("actionDelete_2")
        self.actionAbout_sAB_2 = QtGui.QAction(mainWindow)
        self.actionAbout_sAB_2.setObjectName("actionAbout_sAB_2")
        self.menuMain_2.addAction(self.actionLoad_2)
        self.menuMain_2.addAction(self.actionSave_2)
        self.menuMain_2.addSeparator()
        self.menuMain_2.addAction(self.actionExit)
        self.menuTools.addAction(self.actionAdd_2)
        self.menuTools.addAction(self.actionDelete_2)
        self.menuAbout.addAction(self.actionAbout_sAB_2)
        self.menuMain.addAction(self.menuMain_2.menuAction())
        self.menuMain.addAction(self.menuTools.menuAction())
        self.menuMain.addAction(self.menuAbout.menuAction())

        self.retranslateUi(mainWindow)
        self.tabContainer.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "[sAB] Shadow Address Book", None, QtGui.QApplication.UnicodeUTF8))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.t1), QtGui.QApplication.translate("mainWindow", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.tabContainer.setTabText(self.tabContainer.indexOf(self.t2), QtGui.QApplication.translate("mainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMain_2.setTitle(QtGui.QApplication.translate("mainWindow", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("mainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("mainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd.setText(QtGui.QApplication.translate("mainWindow", "Add Contact", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("mainWindow", "Delete Contact", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("mainWindow", "Save ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("mainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_sAB.setText(QtGui.QApplication.translate("mainWindow", "About [sAB]", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("mainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTools.setText(QtGui.QApplication.translate("mainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_2.setText(QtGui.QApplication.translate("mainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_2.setText(QtGui.QApplication.translate("mainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("mainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_2.setText(QtGui.QApplication.translate("mainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_2.setText(QtGui.QApplication.translate("mainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_sAB_2.setText(QtGui.QApplication.translate("mainWindow", "About [sAB]", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
