__author__ = 'Shadow - shadowsgovernment.com'

from PySide.QtGui import (QMainWindow, QAction, QFileDialog, QApplication)
from addresswidget import AddressWidget


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.addressWidget = AddressWidget()
        self.setCentralWidget(self.addressWidget)
        self.createMenus()
        self.setGeometry(600, 400, 600, 400)
        self.setWindowTitle("[sAB] Shadow Address Book")


    def createMenus(self):
        # Create the main menuBar menu items
        fileMenu = self.menuBar().addMenu("&File")
        toolMenu = self.menuBar().addMenu("&Tools")

        # Populate the File menu
        openAction = self.createAction("&Open...", fileMenu, self.openFile)
        saveAction = self.createAction("&Save As...", fileMenu, self.saveFile)
        fileMenu.addSeparator()
        exitAction = self.createAction("E&xit", fileMenu, self.close)

        # Populate the Tools menu
        addAction = self.createAction("&Add Entry...", toolMenu, self.addressWidget.addEntry)
        self.editAction = self.createAction("&Edit Entry...", toolMenu, self.addressWidget.editEntry)
        toolMenu.addSeparator()
        self.removeAction = self.createAction("&Remove Entry", toolMenu, self.addressWidget.removeEntry)

        # Disable the edit and remove menu items initally, as there are
        # no items yet.
        self.editAction.setEnabled(False)
        self.removeAction.setEnabled(False)

        # Wire up the updateActions slot
        self.addressWidget.selectionChanged.connect(self.updateActions)

    def createAction(self, text, menu, slot):
        """ Helper function to save typing when populating menus
            with action.
        """
        action = QAction(text, self)
        menu.addAction(action)
        action.triggered.connect(slot)
        return action

    # Quick  gotcha:
    #
    # QFiledialog.getOpenFilename and QFileDialog.get.SaveFileName don't
    # behave in PySide as they do in QT, where they return a QString
    # containing the filename.
    #
    # In PySide (and, I believe, PyQT), these functions return a tuple:
    # (filename, filter)
    #
    # http://www.pyside.org/docs/pyside/PySide/QtGui/QFileDialog.html

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self)
        if filename:
            self.addressWidget.readFromFile(filename)

    def saveFile(self):
        filename, _ = QFileDialog.getSaveFileName(self)
        if filename:
            self.addressWidget.writeToFile(filename)

    def updateActions(self, selection):
        """ Only allow the user to remove or edit an item if an item
            is actually selected.
        """
        indexes = selection.indexes()

        if len(indexes) > 0:
            self.removeAction.setEnabled(True)
            self.editAction.setEnabled(True)
        else:
            self.removeAction.setEnabled(False)
            self.editAction.setEnabled(False)


if __name__ == "__main__":
    """ Run the application. """
    import sys
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())