import sys
import requests
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QMainWindow

from MainWindow import Ui_MainWindow
from Dialog import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.url = "https://huxley2.azurewebsites.net"
        self.setupUi(self)
        self.stationTable.setColumnWidth(0, 400)
        self.stationTable.setColumnWidth(1, 200)
        self.load_data()
        self.fetchButton.clicked.connect(self.fetch_data)

    def fetch_data(self):
        dlg = Dialog(self)
        dlg.exec()

    def load_data(self):
        r = requests.get(f"{self.url}/crs")

        stations = r.json()

        row = 0

        self.stationTable.setRowCount(len(stations))

        for station in stations:
            self.stationTable.setItem(
                row, 0, QtWidgets.QTableWidgetItem(station["stationName"]))
            self.stationTable.setItem(
                row, 1, QtWidgets.QTableWidgetItem(station["crsCode"]))
            row += 1


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.url = "https://huxley2.azurewebsites.net"
        requestdepartures = requests.get(f"{self.url}/departures/eus")
        departures = requestdepartures.json()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.generatedAt.setText(f"Generated At: {departures['generatedAt']}")
        self.ui.serviceCount.setText(
            f"Service Count: {str(len(departures['trainServices']))}")
        self.ui.stationName.setText(f"Station Name: {departures['locationName']}")

        row = 0

        services = departures["trainServices"]

        self.ui.serviceTable.setRowCount(len(services))
        self.ui.serviceTable.setColumnWidth(0, 100)
        self.ui.serviceTable.setColumnWidth(1, 300)
        self.ui.serviceTable.setColumnWidth(2, 175)
        self.ui.serviceTable.setColumnWidth(3, 75)
        self.ui.serviceTable.setColumnWidth(4, 300)

        for service in services:
            self.ui.serviceTable.setItem(row, 2, QtWidgets.QTableWidgetItem(service["operator"]))
            formation = service.get("formation")
            if formation is not None:
                coaches = formation.get("coaches")
                if coaches is not None:
                    self.ui.serviceTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(len(coaches))))

            if service["destination"][0]["via"] is not None:
                self.ui.serviceTable.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{service["destination"][0]["locationName"]} {service["destination"][0]["via"]}'))
            else:
                self.ui.serviceTable.setItem(row, 1, QtWidgets.QTableWidgetItem(service["destination"][0]["locationName"]))
            self.ui.serviceTable.setItem(row, 0, QtWidgets.QTableWidgetItem(service["std"]))

            self.ui.serviceTable.setItem(row, 4, QtWidgets.QTableWidgetItem(service["serviceIdGuid"]))
            row += 1


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
