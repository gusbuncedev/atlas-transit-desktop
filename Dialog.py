# Form implementation generated from reading ui file './ui/departuretable.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.generatedAt = QtWidgets.QLabel(parent=Dialog)
        self.generatedAt.setObjectName("generatedAt")
        self.verticalLayout.addWidget(self.generatedAt)
        self.serviceCount = QtWidgets.QLabel(parent=Dialog)
        self.serviceCount.setObjectName("serviceCount")
        self.verticalLayout.addWidget(self.serviceCount)
        self.stationName = QtWidgets.QLabel(parent=Dialog)
        self.stationName.setObjectName("stationName")
        self.verticalLayout.addWidget(self.stationName)
        self.serviceTable = QtWidgets.QTableWidget(parent=Dialog)
        self.serviceTable.setObjectName("serviceTable")
        self.serviceTable.setColumnCount(5)
        self.serviceTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.serviceTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.serviceTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.serviceTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.serviceTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.serviceTable.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.serviceTable)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.generatedAt.setText(_translate("Dialog", "Generated At:"))
        self.serviceCount.setText(_translate("Dialog", "Service Count: "))
        self.stationName.setText(_translate("Dialog", "Station Name: "))
        item = self.serviceTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Departure Time"))
        item = self.serviceTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Destination"))
        item = self.serviceTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Operator"))
        item = self.serviceTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Coaches"))
        item = self.serviceTable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Service GUID"))