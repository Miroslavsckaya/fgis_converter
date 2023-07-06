from conversion_manager import ConversionManager
from path_helper import PathHelper
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon, QDragEnterEvent, QDropEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QWidget, QFileDialog, \
    QMessageBox, QGridLayout


class LineEdit(QLineEdit):
    droped = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.setDragEnabled(True)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        data = event.mimeData()
        if data.hasUrls() and data.urls()[0].scheme() == 'file':
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        path: str = event.mimeData().urls()[0].toLocalFile()
        self.setText(path)
        self.droped.emit()


class MainWindow(QMainWindow):
    def __init__(self, conversion_manager: ConversionManager, input_path: str, output_path: str) -> None:
        super().__init__()
        self.setWindowTitle("Аршин-конвертер")

        self.conversion_manager: ConversionManager = conversion_manager
        self.layout = QGridLayout()

        text_input_file_label = QLabel('Выбрать файл')
        self.line_edit_input_file = LineEdit()
        button_search_input_file = QPushButton("Обзор")

        text_output_file_label = QLabel('Сохранить в')
        self.line_edit_output_file = LineEdit()
        button_search_output_file = QPushButton("Обзор")

        button_start = QPushButton("Начать")

        button_search_input_file.clicked.connect(self.__search_input_button_clicked)
        button_search_output_file.clicked.connect(self.__search_output_button_clicked)
        button_start.clicked.connect(self.__start_button_clicked)
        self.line_edit_input_file.droped.connect(self.__line_edit_input_file_droped)

        if input_path:
            input_path = PathHelper.to_absolute(input_path)
            self.line_edit_input_file.setText(input_path)
        if output_path:
            output_path = PathHelper.to_absolute(output_path)
            self.line_edit_output_file.setText(output_path)

        self.layout.addWidget(text_input_file_label, 0, 0)
        self.layout.addWidget(self.line_edit_input_file, 0, 1)
        self.layout.addWidget(button_search_input_file, 0, 2)
        self.layout.addWidget(text_output_file_label, 1, 0)
        self.layout.addWidget(self.line_edit_output_file, 1, 1)
        self.layout.addWidget(button_search_output_file, 1, 2)
        self.layout.addWidget(button_start, 2, 2)
        self.layout.setColumnMinimumWidth(1, 250)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def __line_edit_input_file_droped(self) -> None:
        if not self.line_edit_output_file.text():
            output_path: str = PathHelper.replace_suffix(self.line_edit_input_file.text(), '.xml')
            self.line_edit_output_file.setText(output_path)

    def __search_input_button_clicked(self) -> None:
        input_path: str = QFileDialog.getOpenFileName(caption='Выбрать файл', filter='CSV файлы (*.csv);;'
                                                                                     'Таблицы Excel (*.xlsx)')[0]
        if input_path:
            self.line_edit_input_file.setText(input_path)
            if not self.line_edit_output_file.text():
                self.line_edit_output_file.setText(PathHelper.replace_suffix(input_path, '.xml'))

    def __search_output_button_clicked(self) -> None:
        output_path: str = QFileDialog.getSaveFileName(caption='Сохранить файл')[0]
        if not output_path:
            return

        output_path: str = PathHelper.replace_suffix(output_path, '.xml')
        self.line_edit_output_file.setText(output_path)

    def __start_button_clicked(self) -> None:
        input_path: str = self.line_edit_input_file.text()
        output_path: str = self.line_edit_output_file.text()
        if not input_path:
            QMessageBox.warning(self, 'Файл не выбран', 'Выберите файл для конвертации')
            return
        if not output_path:
            QMessageBox.warning(self, 'Путь не выбран', 'Выберите путь для сохранения')
            return

        self.conversion_manager.convert(input_path, output_path, 'csv')
        self.line_edit_input_file.setText('')
        self.line_edit_output_file.setText('')


class Application:
    @staticmethod
    def start(conversion_manager: ConversionManager, input_path: str, output_path: str) -> None:
        app = QApplication([])
        app.setWindowIcon(QIcon('icons/RST.ico'))

        window = MainWindow(conversion_manager, input_path, output_path)
        window.show()

        app.exec()
