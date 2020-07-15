# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        self.menuOpen_Recent_Project = QtWidgets.QMenu(self.menuProject)
        self.menuOpen_Recent_Project.setObjectName("menuOpen_Recent_Project")
        self.menuFiles_and_Cases = QtWidgets.QMenu(self.menubar)
        self.menuFiles_and_Cases.setObjectName("menuFiles_and_Cases")
        self.menuCoding = QtWidgets.QMenu(self.menubar)
        self.menuCoding.setObjectName("menuCoding")
        self.menuReports = QtWidgets.QMenu(self.menubar)
        self.menuReports.setObjectName("menuReports")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_New_Project = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Project.setObjectName("actionCreate_New_Project")
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionClose_Project = QtWidgets.QAction(MainWindow)
        self.actionClose_Project.setObjectName("actionClose_Project")
        self.actionProject_Memo = QtWidgets.QAction(MainWindow)
        self.actionProject_Memo.setObjectName("actionProject_Memo")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionManage_files = QtWidgets.QAction(MainWindow)
        self.actionManage_files.setObjectName("actionManage_files")
        self.actionManage_cases = QtWidgets.QAction(MainWindow)
        self.actionManage_cases.setObjectName("actionManage_cases")
        self.actionFile_categories = QtWidgets.QAction(MainWindow)
        self.actionFile_categories.setObjectName("actionFile_categories")
        self.actionManage_journals = QtWidgets.QAction(MainWindow)
        self.actionManage_journals.setObjectName("actionManage_journals")
        self.actionCodes = QtWidgets.QAction(MainWindow)
        self.actionCodes.setObjectName("actionCodes")
        self.actionCategories = QtWidgets.QAction(MainWindow)
        self.actionCategories.setObjectName("actionCategories")
        self.actionCodebook = QtWidgets.QAction(MainWindow)
        self.actionCodebook.setObjectName("actionCodebook")
        self.actionAssign_Attributes = QtWidgets.QAction(MainWindow)
        self.actionAssign_Attributes.setObjectName("actionAssign_Attributes")
        self.actionManage_Attributes = QtWidgets.QAction(MainWindow)
        self.actionManage_Attributes.setObjectName("actionManage_Attributes")
        self.actionImport_Attributes = QtWidgets.QAction(MainWindow)
        self.actionImport_Attributes.setObjectName("actionImport_Attributes")
        self.actionCoding_reports = QtWidgets.QAction(MainWindow)
        self.actionCoding_reports.setObjectName("actionCoding_reports")
        self.actionCoding_summary = QtWidgets.QAction(MainWindow)
        self.actionCoding_summary.setObjectName("actionCoding_summary")
        self.actionSQL_statements = QtWidgets.QAction(MainWindow)
        self.actionSQL_statements.setObjectName("actionSQL_statements")
        self.actionContents = QtWidgets.QAction(MainWindow)
        self.actionContents.setObjectName("actionContents")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionImport_survey = QtWidgets.QAction(MainWindow)
        self.actionImport_survey.setObjectName("actionImport_survey")
        self.actionManage_attributes = QtWidgets.QAction(MainWindow)
        self.actionManage_attributes.setObjectName("actionManage_attributes")
        self.actionFrequency_table = QtWidgets.QAction(MainWindow)
        self.actionFrequency_table.setObjectName("actionFrequency_table")
        self.actionCoding_comparison = QtWidgets.QAction(MainWindow)
        self.actionCoding_comparison.setObjectName("actionCoding_comparison")
        self.actionText_mining = QtWidgets.QAction(MainWindow)
        self.actionText_mining.setObjectName("actionText_mining")
        self.actionView_Graph = QtWidgets.QAction(MainWindow)
        self.actionView_Graph.setObjectName("actionView_Graph")
        self.actionExport_codebook = QtWidgets.QAction(MainWindow)
        self.actionExport_codebook.setObjectName("actionExport_codebook")
        self.actionCode_image = QtWidgets.QAction(MainWindow)
        self.actionCode_image.setObjectName("actionCode_image")
        self.actionCode_frequencies = QtWidgets.QAction(MainWindow)
        self.actionCode_frequencies.setObjectName("actionCode_frequencies")
        self.actionCoding_Matrix = QtWidgets.QAction(MainWindow)
        self.actionCoding_Matrix.setObjectName("actionCoding_Matrix")
        self.actionCode_audio_video = QtWidgets.QAction(MainWindow)
        self.actionCode_audio_video.setObjectName("actionCode_audio_video")
        self.actionProject_Exchange_Export = QtWidgets.QAction(MainWindow)
        self.actionProject_Exchange_Export.setObjectName("actionProject_Exchange_Export")
        self.actionREFI_Codebook_export = QtWidgets.QAction(MainWindow)
        self.actionREFI_Codebook_export.setObjectName("actionREFI_Codebook_export")
        self.actionREFI_Codebook_import = QtWidgets.QAction(MainWindow)
        self.actionREFI_Codebook_import.setObjectName("actionREFI_Codebook_import")
        self.actionREFI_QDA_Project_import = QtWidgets.QAction(MainWindow)
        self.actionREFI_QDA_Project_import.setObjectName("actionREFI_QDA_Project_import")
        self.actionView_Graph_2 = QtWidgets.QAction(MainWindow)
        self.actionView_Graph_2.setObjectName("actionView_Graph_2")
        self.actionRQDA_Project_import = QtWidgets.QAction(MainWindow)
        self.actionRQDA_Project_import.setObjectName("actionRQDA_Project_import")
        self.actionProject_summary = QtWidgets.QAction(MainWindow)
        self.actionProject_summary.setObjectName("actionProject_summary")
        self.actionNone = QtWidgets.QAction(MainWindow)
        self.actionNone.setObjectName("actionNone")
        self.menuOpen_Recent_Project.addAction(self.actionNone)
        self.menuProject.addAction(self.actionCreate_New_Project)
        self.menuProject.addAction(self.actionOpen_Project)
        self.menuProject.addAction(self.menuOpen_Recent_Project.menuAction())
        self.menuProject.addAction(self.actionClose_Project)
        self.menuProject.addAction(self.actionProject_Memo)
        self.menuProject.addAction(self.actionSettings)
        self.menuProject.addAction(self.actionProject_summary)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionREFI_Codebook_export)
        self.menuProject.addAction(self.actionProject_Exchange_Export)
        self.menuProject.addAction(self.actionREFI_Codebook_import)
        self.menuProject.addAction(self.actionREFI_QDA_Project_import)
        self.menuProject.addAction(self.actionRQDA_Project_import)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionExit)
        self.menuFiles_and_Cases.addAction(self.actionManage_files)
        self.menuFiles_and_Cases.addAction(self.actionManage_cases)
        self.menuFiles_and_Cases.addAction(self.actionManage_journals)
        self.menuFiles_and_Cases.addAction(self.actionImport_survey)
        self.menuFiles_and_Cases.addAction(self.actionManage_attributes)
        self.menuCoding.addAction(self.actionCodes)
        self.menuCoding.addAction(self.actionCode_image)
        self.menuCoding.addAction(self.actionCode_audio_video)
        self.menuCoding.addAction(self.actionExport_codebook)
        self.menuReports.addAction(self.actionCoding_reports)
        self.menuReports.addAction(self.actionCoding_comparison)
        self.menuReports.addAction(self.actionCode_frequencies)
        self.menuReports.addAction(self.actionView_Graph)
        self.menuReports.addAction(self.actionText_mining)
        self.menuReports.addAction(self.actionSQL_statements)
        self.menuHelp.addAction(self.actionContents)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuFiles_and_Cases.menuAction())
        self.menubar.addAction(self.menuCoding.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QualCoder"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuOpen_Recent_Project.setTitle(_translate("MainWindow", "Open Recent Project"))
        self.menuFiles_and_Cases.setTitle(_translate("MainWindow", "Files and Cases"))
        self.menuCoding.setTitle(_translate("MainWindow", "Coding"))
        self.menuReports.setTitle(_translate("MainWindow", "Reports"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionCreate_New_Project.setText(_translate("MainWindow", "Create New Project"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionClose_Project.setText(_translate("MainWindow", "Close Project"))
        self.actionProject_Memo.setText(_translate("MainWindow", "Project Memo"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionManage_files.setText(_translate("MainWindow", "Manage files"))
        self.actionManage_cases.setText(_translate("MainWindow", "Manage cases"))
        self.actionFile_categories.setText(_translate("MainWindow", "File categories"))
        self.actionManage_journals.setText(_translate("MainWindow", "Manage journals"))
        self.actionCodes.setText(_translate("MainWindow", "Code text"))
        self.actionCategories.setText(_translate("MainWindow", "Categories"))
        self.actionCodebook.setText(_translate("MainWindow", "Codebook"))
        self.actionAssign_Attributes.setText(_translate("MainWindow", "Assign Attributes"))
        self.actionManage_Attributes.setText(_translate("MainWindow", "Manage Attributes"))
        self.actionImport_Attributes.setText(_translate("MainWindow", "Import Attributes"))
        self.actionCoding_reports.setText(_translate("MainWindow", "Coding reports"))
        self.actionCoding_summary.setText(_translate("MainWindow", "Coding summary"))
        self.actionSQL_statements.setText(_translate("MainWindow", "SQL statements"))
        self.actionContents.setText(_translate("MainWindow", "Contents"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionImport_survey.setText(_translate("MainWindow", "Import survey"))
        self.actionManage_attributes.setText(_translate("MainWindow", "Manage attributes"))
        self.actionFrequency_table.setText(_translate("MainWindow", "Frequency table"))
        self.actionCoding_comparison.setText(_translate("MainWindow", "Coding comparison"))
        self.actionText_mining.setText(_translate("MainWindow", "Text mining"))
        self.actionView_Graph.setText(_translate("MainWindow", "View Graph"))
        self.actionExport_codebook.setText(_translate("MainWindow", "Export codebook"))
        self.actionCode_image.setText(_translate("MainWindow", "Code image"))
        self.actionCode_frequencies.setText(_translate("MainWindow", "Code frequencies"))
        self.actionCoding_Matrix.setText(_translate("MainWindow", "Coding Matrix"))
        self.actionCode_audio_video.setText(_translate("MainWindow", "Code audio/video"))
        self.actionProject_Exchange_Export.setText(_translate("MainWindow", "REFI-QDA Project export"))
        self.actionProject_Exchange_Export.setToolTip(_translate("MainWindow", "REFI-QDA Project export"))
        self.actionREFI_Codebook_export.setText(_translate("MainWindow", "REFI-QDA Codebook export"))
        self.actionREFI_Codebook_import.setText(_translate("MainWindow", "REFI-QDA Codebook import"))
        self.actionREFI_QDA_Project_import.setText(_translate("MainWindow", "REFI-QDA Project import"))
        self.actionView_Graph_2.setText(_translate("MainWindow", "View Graph 2"))
        self.actionRQDA_Project_import.setText(_translate("MainWindow", "RQDA Project import"))
        self.actionProject_summary.setText(_translate("MainWindow", "Project summary"))
        self.actionNone.setText(_translate("MainWindow", "None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
