import sys
from datetime import datetime
import requests
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QMainWindow
from PyQt6.QtCore import Qt

from MainWindow import Ui_MainWindow
from Dialog import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.url = "https://huxley2.azurewebsites.net"
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.search)
        self.stationTable.setColumnWidth(0, 600)
        self.stationTable.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.stationTable.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Fixed
        )
        self.load_data()
        self.showDepartureBoard.clicked.connect(self.fetch_data)

    def fetch_data(self):
        dlg = Dialog(self, self.stationTable.currentItem().text())
        dlg.exec()

    def load_data(self):
        r = requests.get(f"{self.url}/crs")

        stations = r.json()

        row = 0

        self.stationTable.setRowCount(len(stations))

        for station in stations:
            self.stationTable.setItem(
                row, 0, QtWidgets.QTableWidgetItem(station["stationName"])
            )
            row += 1

    def search(self, s):
        items = self.stationTable.findItems(s, Qt.MatchFlag.MatchStartsWith)
        if items:
            item = items[0]
            self.stationTable.setCurrentItem(item)


class Dialog(QDialog):
    def __init__(self, parent, station):
        super().__init__(parent)
        self.url = "https://huxley2.azurewebsites.net"
        self.station = "EUS"
        requestdepartures = requests.get(f"{self.url}/departures/{station}")
        departures = requestdepartures.json()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.generatedAt.setText(
            str(
                datetime.strptime(
                    departures["generatedAt"].split(".")[0], "%Y-%m-%dT%H:%M:%S"
                )
            )
        )
        if (
            departures["trainServices"] is not None
            and len(departures["trainServices"]) > 0
        ):
            self.ui.serviceCount.setText(
                f"Service Count: {str(len(departures['trainServices']))}"
            )
        else:
            self.ui.serviceCount.setText(
                "Service Count: Fuck you there are no trains... sucks to suck"
            )
        self.ui.stationName.setText(f"Station Name: {departures['locationName']}")

        row = 0

        services = departures["trainServices"]
        if (
            departures["trainServices"] is not None
            and len(departures["trainServices"]) > 0
        ):
            self.ui.serviceTable.setRowCount(len(services))
        else:
            self.ui.serviceTable.setRowCount(0)
        self.ui.serviceTable.setColumnWidth(0, 100)
        self.ui.serviceTable.setColumnWidth(1, 300)
        self.ui.serviceTable.setColumnWidth(2, 175)
        self.ui.serviceTable.setColumnWidth(3, 75)
        self.ui.serviceTable.setColumnWidth(4, 300)

        if services is not None and len(services) > 0:
            for service in services:
                self.ui.serviceTable.setItem(
                    row, 2, QtWidgets.QTableWidgetItem(service["operator"])
                )
                formation = service.get("formation")
                if formation is not None:
                    coaches = formation.get("coaches")
                    if coaches is not None:
                        self.ui.serviceTable.setItem(
                            row, 3, QtWidgets.QTableWidgetItem(str(len(coaches)))
                        )

                r = requests.get(f"{self.url}/service/{service['serviceIdGuid']}")
                platform = r.json()
                self.ui.serviceTable.setItem(
                    row, 5, QtWidgets.QTableWidgetItem(platform["platform"])
                )
                if service["destination"][0]["via"] is not None:
                    self.ui.serviceTable.setItem(
                        row,
                        1,
                        QtWidgets.QTableWidgetItem(
                            f'{service["destination"][0]["locationName"]} {service["destination"][0]["via"]}'
                        ),
                    )
                else:
                    self.ui.serviceTable.setItem(
                        row,
                        1,
                        QtWidgets.QTableWidgetItem(
                            service["destination"][0]["locationName"]
                        ),
                    )
                self.ui.serviceTable.setItem(
                    row, 0, QtWidgets.QTableWidgetItem(service["std"])
                )

                self.ui.serviceTable.setItem(
                    row, 4, QtWidgets.QTableWidgetItem(service["serviceIdGuid"])
                )
                row += 1
        else:
            pass


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
