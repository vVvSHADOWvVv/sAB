__author__ = 'Shadow - shadowsgovernment.com'

from PySide.QtCore import (Qt, Signal)
from PySide.QtGui import (QWidget, QLabel, QPushButton, QVBoxLayout)

from adddialogwidget import AddDialogWidget

class NewAddressTab(QWidget):
    """ An extra tab that prompts the user to add new contacts.
        To be displayed only when there are no contacts in the model.
    """

    sendDetails = Signal(str, str, str)

    def __init__(self, parent=None):
        super(NewAddressTab, self).__init__(parent)

        descriptionLabel = QLabel("There are no contacts in your address book."
                                   "\nClick Add to add new contacts.\n"
                                   "Don't forget to Save\n\n"
                                   " ~Shadow - shadow-corp@shadowsgovernment.com")

        addButton = QPushButton("Add")

        layout = QVBoxLayout()
        layout.addWidget(descriptionLabel)
        layout.addWidget(addButton, 0, Qt.AlignCenter)

        self.setLayout(layout)

        addButton.clicked.connect(self.addEntry)

    def addEntry(self):
        addDialog = AddDialogWidget()

        if addDialog.exec_():
            name = addDialog.name
            email = addDialog.email
            phone = addDialog.phone
            self.sendDetails.emit(name, email, phone)


if __name__ == "__main__":

    def printAddress(name, email, phone):
        print("Name:" + name)
        print("e-Mail:" + email)
        print("Phone:" + phone)

    import sys
    from PySide.QtGui import QApplication
    
    app = QApplication(sys.argv)
    newAddressTab = NewAddressTab()
    newAddressTab.sendDetails.connect(printAddress)
    newAddressTab.show()
    sys.exit(app.exec_())