__author__ = 'Shadow - shadowsgovernment.com'

from PySide.QtCore import Qt
from PySide.QtGui import (QDialog, QLabel, QLineEdit, QDialogButtonBox, QGridLayout, QVBoxLayout)

class AddDialogWidget(QDialog):
    """ A dialog to add a new address to the addressbook. """

    def __init__(self, parent=None):
        super(AddDialogWidget, self).__init__(parent)

        nameLabel = QLabel("Name")
        emailLabel = QLabel("e-Mail")
        phoneLabel = QLabel("Phone")

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.nameText = QLineEdit()
        self.emailText = QLineEdit()
        self.phoneText = QLineEdit()

        grid = QGridLayout()
        grid.setColumnStretch(1, 2)
        grid.addWidget(nameLabel, 0, 0)
        grid.addWidget(self.nameText, 0, 1)
        grid.addWidget(emailLabel, 1, 0, Qt.AlignLeft | Qt.AlignTop)
        grid.addWidget(self.emailText, 1, 1, Qt.AlignLeft)
        grid.addWidget(phoneLabel, 2, 0, Qt.AlignLeft | Qt.AlignTop)
        grid.addWidget(self.phoneText, 2, 1, Qt.AlignLeft)

        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(buttonBox)

        self.setLayout(layout)

        self.setWindowTitle("Shadow | Add Contact")

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    # These properties make using this dialog a little cleaner. It's much 
    # nicer to type "addDialog.address" to retrieve the address as compared 
    # to "addDialog.addressText.toPlainText()"
    @property
    def name(self):
        return self.nameText.text()

    @property
    def email(self):
        return self.emailText.text()

    @property
    def phone(self):
        return self.phoneText.text()

if __name__ == "__main__":
    import sys
    from PySide.QtGui import QApplication
    
    app = QApplication(sys.argv)

    dialog = AddDialogWidget()
    if (dialog.exec_()):
        name = dialog.name
        email = dialog.email
        phone = dialog.phone
        print("Name:" + name)
        print("e-Mail:" + email)
        print("Phone:" + phone)