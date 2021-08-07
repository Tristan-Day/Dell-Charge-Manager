import configparser
import subprocess
import sys

from PyQt5 import QtWidgets

import windows


class Window(QtWidgets.QWidget, windows.Main):

    def __init__(self):

        super().__init__()
        self.generate(self)

        # Load Config File
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

        # Check sudo_elevator is set
        elevator = self.config.get("Default", "sudo_elevator").lower()
        if "none" in elevator:
            error_window = windows.Error(
                "Elevator Not Set", "Set your systems sudo gui dialogue in config.ini")
            error_window.show()
            quit()

        # Set Correct Command
        elif elevator == "kdesu":
            self.sudo_elevator = "kdesu -t -c"

        elif elevator == "gksu":
            self.sudo_elevator = "gksu"

        else:
            error_window = windows.Error(
                "Unrecognised Elevator", "Please check your have entered your elevator correctly")
            error_window.show()
            quit()

        # Configure Hooks
        self.applyButton.clicked.connect(self._setChargeLimit)

        # Load Current Settings
        self.maxCharge.setValue(self._getCurrentLimit())

    def _setChargeLimit(self):
        try:
            res = subprocess.check_output(
                f"{self.sudo_elevator} '/opt/dell/dcc/cctk --PrimaryBattChargeCfg=custom:50-{self.maxCharge.value()}'", shell=True)
            print(str(res))
        except BaseException as error:
            error_window = windows.Error(
                "Unable to apply changes", str(error))
            error_window.show()

    def _getCurrentLimit(self):
        res = subprocess.check_output(
            f"{self.sudo_elevator} '/opt/dell/dcc/cctk --PrimaryBattChargeCfg'", shell=True)
        return int(str(res).split(":")[-1].split("-")[-1][0:2])


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()

    sys.exit(app.exec())
