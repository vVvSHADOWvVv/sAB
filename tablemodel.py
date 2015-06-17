__author__ = 'Shadow - shadowsgovernment.com'

from PySide.QtCore import (Qt, QAbstractTableModel, QModelIndex)

class TableModel(QAbstractTableModel):

    def __init__(self, addresses=None, parent=None):
        super(TableModel, self).__init__(parent)

        if addresses is None:
            self.addresses = []
        else:
            self.addresses = addresses

    def rowCount(self, index=QModelIndex()):
        """ Returns the number of rows the model holds. """
        return len(self.addresses)

    def columnCount(self, index=QModelIndex()):
        """ Returns the number of columns the model holds. """
        return 3

    def data(self, index, role=Qt.DisplayRole):
        """ Depending on the index and role given, return data. If not 
            returning data, return None (PySide equivalent of QT's 
            "invalid QVariant").
        """
        if not index.isValid():
            return None

        if not 0 <= index.row() < len(self.addresses):
            return None

        if role == Qt.DisplayRole:
            name = self.addresses[index.row()]["name"]
            email = self.addresses[index.row()]["email"]
            phone = self.addresses[index.row()]["phone"]

        if index.column() == 0:
            return name
        elif index.column() == 1:
            return email
        elif index.column() == 2:
            return phone

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """ Set the headers to be displayed. """
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section == 0:
                return "Name"
            elif section == 1:
                return "e-Mail"
            elif section == 2:
                return "Phone"
        
        return None

    def insertRows(self, position, rows=1, index=QModelIndex()):
        """ Insert a row into the model. """
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)

        for row in range(rows):
            self.addresses.insert(position + row, {"name": "", "email": "", "phone": ""})

        self.endInsertRows()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """ Remove a row from the model. """
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)

        del self.addresses[position:position+rows]

        self.endRemoveRows()
        return True

    def setData(self, index, value, role=Qt.EditRole):
        """ Adjust the data (set it to <value>) depending on the given 
            index and role. 
        """
        if role != Qt.EditRole:
            return False

        if index.isValid() and 0 <= index.row() < len(self.addresses):
            address = self.addresses[index.row()]
            if index.column() == 0:
                address["name"] = value
            elif index.column() == 1:
                address["email"] = value
            elif index.column() == 2:
                address["phone"] = value
            else:
                return False

            self.dataChanged.emit(index, index)

            return True

        return False

    def flags(self, index):
        """ Set the item flags at the given index. Seems like we're 
            implementing this function just to see how it's done, as we 
            manually adjust each tableView to have NoEditTriggers.
        """
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable)