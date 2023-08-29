import sys
import csv

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, \
    QTableWidget, QTableWidgetItem, QFileDialog


class CSVEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Param Values")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.import_button = QPushButton("Import CSV")
        self.import_button.clicked.connect(self.import_csv)
        self.layout.addWidget(self.import_button)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.save_button = QPushButton("Save CSV")
        self.save_button.clicked.connect(self.save_csv)
        self.layout.addWidget(self.save_button)

        self.data = []

    def import_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Import CSV", "", "CSV Files (*.csv)", options=options)

        if file_path:
            self.table.clearContents()
            self.data = []

            with open(file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if len(row) == 2:
                        self.data.append(row)

            self.table.setRowCount(len(self.data))
            self.table.setColumnCount(2)  # Update to 3 columns
            for row_idx, (address, value) in enumerate(self.data):  # Update row data extraction
                address_item = QTableWidgetItem(address)
                address_item.setFlags(address_item.flags() & ~Qt.ItemIsEditable)  # Make the item not editable
                value_item = QTableWidgetItem(value)
                # new_column_item = QTableWidgetItem(new_column_data)
                self.table.setItem(row_idx, 0, address_item)
                self.table.setItem(row_idx, 1, value_item)
                # self.table.setItem(row_idx, 2, new_column_item)  # Set new column item

    def save_csv(self):
        if self.data:
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv)", options=options)

            if file_path:
                new_data = []

                for row_idx in range(self.table.rowCount()):
                    address_item = self.table.item(row_idx, 0)
                    value_item = self.table.item(row_idx, 1)
                    # new_column_item = self.table.item(row_idx, 2)

                    if address_item and value_item:
                        new_data.append([address_item.text(), value_item.text()])


                with open(file_path, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerows(new_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CSVEditorApp()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())
