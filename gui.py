import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon

from conversion_manager import ConversionManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, \
    QWidget, QFileDialog, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, conversion_manager: ConversionManager) -> None:
        super().__init__()
        self.setFixedSize(QSize(300, 150))

        self.conversion_manager: ConversionManager = conversion_manager
        self.input_path: str = ''

        self.setWindowTitle("Аршин-конвертер")
        self.layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        search_button = QPushButton("Обзор")
        start_button = QPushButton("Начать")
        search_button.clicked.connect(self.__the_search_button_was_clicked)
        start_button.clicked.connect(self.__the_start_button_was_clicked)

        self.label = QLabel('Выберите файл для конвертации')

        button_layout.addWidget(search_button)
        button_layout.addWidget(start_button)

        self.layout.addWidget(self.label)
        self.layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def __the_search_button_was_clicked(self) -> None:
        self.input_path: str = QFileDialog.getOpenFileName(caption='Выбрать файл', filter='CSV файлы (*.csv);;'
                                                                                     'Таблицы Excel (*.xlsx)')[0]
        if self.input_path:
            self.label.setText(self.input_path)

    def __the_start_button_was_clicked(self) -> None:
        if not self.input_path:
            QMessageBox.warning(self, 'Файл не выбран', 'Выберите файл для конвертации')
            return
        output_path: str = QFileDialog.getSaveFileName(caption='Сохранить файл', directory=self.input_path)[0]
        self.conversion_manager.convert(self.input_path, output_path + '.xml', 'csv')


class Application:
    @staticmethod
    def start(conversion_manager: ConversionManager) -> None:
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon('icons/RST.ico'))

        window = MainWindow(conversion_manager)
        window.show()

        app.exec()
