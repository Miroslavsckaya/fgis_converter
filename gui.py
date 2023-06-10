from conversion_manager import ConversionManager
from path_helper import PathHelper
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, \
    QWidget, QFileDialog, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, conversion_manager: ConversionManager, input_path: str | None, output_path: str | None) -> None:
        super().__init__()
        self.setMinimumSize(QSize(300, 150))

        self.conversion_manager: ConversionManager = conversion_manager
        self.input_path: str | None = input_path
        self.output_path: str | None = output_path

        self.setWindowTitle("Аршин-конвертер")
        self.layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        search_button = QPushButton("Обзор")
        start_button = QPushButton("Начать")
        search_button.clicked.connect(self.__the_search_button_was_clicked)
        start_button.clicked.connect(self.__the_start_button_was_clicked)

        if self.input_path is not None:
            self.input_path = PathHelper.get_abspath(self.input_path)
            text_input_path_label = 'Выбран файл: ' + self.input_path
        else:
            text_input_path_label = 'Выберите файл для конвертации'
        self.input_path_label = QLabel(text_input_path_label)

        text_output_path_label = 'Сохранить в: '
        if self.output_path is not None:
            self.output_path = PathHelper.get_abspath(self.output_path)
            text_output_path_label += self.output_path
        self.output_path_label = QLabel(text_output_path_label)

        button_layout.addWidget(search_button)
        button_layout.addWidget(start_button)

        self.layout.addWidget(self.input_path_label)
        self.layout.addWidget(self.output_path_label)
        self.layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def __the_search_button_was_clicked(self) -> None:
        self.input_path: str = QFileDialog.getOpenFileName(caption='Выбрать файл', filter='CSV файлы (*.csv);;'
                                                                                     'Таблицы Excel (*.xlsx)')[0]
        if self.input_path:
            self.input_path_label.setText('Выбран файл: ' + self.input_path)

    def __the_start_button_was_clicked(self) -> None:
        if self.input_path is None:
            QMessageBox.warning(self, 'Файл не выбран', 'Выберите файл для конвертации')
            return

        if self.output_path is None:
            self.output_path: str = QFileDialog.getSaveFileName(caption='Сохранить файл',
                                                                directory=PathHelper.change_suffix(self.input_path))[0]

        self.output_path = PathHelper.change_suffix(self.output_path)
        self.output_path_label.setText('Сохранить в: ' + self.output_path)
        self.conversion_manager.convert(self.input_path, self.output_path, 'csv')


class Application:
    @staticmethod
    def start(conversion_manager: ConversionManager, input_path: str | None, output_path: str | None) -> None:
        app = QApplication([])
        app.setWindowIcon(QIcon('icons/RST.ico'))

        window = MainWindow(conversion_manager, input_path, output_path)
        window.show()

        app.exec()
