# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_servce_main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_w_main(object):
    def setupUi(self, w_main):
        w_main.setObjectName("w_main")
        w_main.resize(331, 170)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        w_main.setWindowIcon(icon)
        w_main.setToolTip("")
        self.splitter_2 = QtWidgets.QSplitter(w_main)
        self.splitter_2.setGeometry(QtCore.QRect(30, 40, 96, 12))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        self.label.setObjectName("label")
        self.label_status = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_status")
        self.pushButton_save = QtWidgets.QPushButton(w_main)
        self.pushButton_save.setGeometry(QtCore.QRect(140, 120, 71, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.pushButton_save.setFont(font)
        self.pushButton_save.setCheckable(False)
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_close = QtWidgets.QPushButton(w_main)
        self.pushButton_close.setGeometry(QtCore.QRect(220, 120, 75, 23))
        self.pushButton_close.setMinimumSize(QtCore.QSize(75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_stop = QtWidgets.QPushButton(w_main)
        self.pushButton_stop.setGeometry(QtCore.QRect(60, 120, 71, 23))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.checkBox = QtWidgets.QCheckBox(w_main)
        self.checkBox.setGeometry(QtCore.QRect(30, 70, 101, 16))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(w_main)
        self.pushButton_close.clicked.connect(w_main.close)
        QtCore.QMetaObject.connectSlotsByName(w_main)
        w_main.setTabOrder(self.pushButton_stop, self.pushButton_save)
        w_main.setTabOrder(self.pushButton_save, self.pushButton_close)
        w_main.setTabOrder(self.pushButton_close, self.checkBox)

    def retranslateUi(self, w_main):
        _translate = QtCore.QCoreApplication.translate
        w_main.setWindowTitle(_translate("w_main", "本地服务监控程序[Blrise]"))
        self.label.setText(_translate("w_main", "服务状态："))
        self.label_status.setText(_translate("w_main", "未启动"))
        self.pushButton_save.setText(_translate("w_main", "保存"))
        self.pushButton_close.setText(_translate("w_main", "关闭"))
        self.pushButton_stop.setText(_translate("w_main", "停止服务"))
        self.checkBox.setText(_translate("w_main", "自动启动服务"))


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_w_main()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())