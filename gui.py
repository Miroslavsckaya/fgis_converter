from conversion_manager import ConversionManager
from path_helper import PathHelper
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QWidget, QFileDialog, \
    QMessageBox, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self, conversion_manager: ConversionManager, input_path: str, output_path: str) -> None:
        super().__init__()
        self.setWindowTitle("Аршин-конвертер")

        self.conversion_manager: ConversionManager = conversion_manager
        self.layout = QGridLayout()

        widgets: list[list] = []
        widgets.append(self.__create_input_file_widgets())
        widgets.append(self.__create_output_file_widgets())

        self.button_start = QPushButton("Начать")
        widgets.append([self.button_start])

        self.__connect_buttons()
        self.__set_text_to_line_edit(input_path, output_path)
        self.__init_layout(widgets)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def __search_input_button_clicked(self) -> None:
        input_path: str = QFileDialog.getOpenFileName(caption='Выбрать файл', filter='CSV файлы (*.csv);;'
                                                                                     'Таблицы Excel (*.xlsx)')[0]
        if input_path:
            self.line_edit_input_file.setText(input_path)
            if not self.line_edit_output_file.text():
                self.line_edit_output_file.setText(PathHelper.replace_extension(input_path, '.xml'))

    def __search_output_button_clicked(self) -> None:
        output_path: str = QFileDialog.getSaveFileName(caption='Сохранить файл')[0]
        if not output_path:
            return

        output_path = PathHelper.replace_extension(output_path, '.xml')
        self.line_edit_output_file.setText(output_path)

    def __start_button_clicked(self) -> None:
        input_path = self.line_edit_input_file.text()
        output_path = self.line_edit_output_file.text()
        if not input_path:
            QMessageBox.warning(self, 'Файл не выбран', 'Выберите файл для конвертации')
            return
        if not output_path:
            QMessageBox.warning(self, 'Путь не выбран', 'Выберите путь для сохранения')
            return

        self.conversion_manager.convert(input_path, output_path, 'csv')

    def __create_input_file_widgets(self) -> list[QLabel | QLineEdit | QPushButton]:
        widgets_row: list[QLabel | QLineEdit | QPushButton] = []
        widgets_row.append(QLabel('Выбрать файл'))
        self.line_edit_input_file = QLineEdit()
        widgets_row.append(self.line_edit_input_file)
        self.button_search_input_file = QPushButton("Обзор")
        widgets_row.append(self.button_search_input_file)
        return widgets_row

    def __create_output_file_widgets(self) -> list[QLabel | QLineEdit | QPushButton]:
        widgets_row: list[QLabel | QLineEdit | QPushButton] = []
        widgets_row.append(QLabel('Сохранить в'))
        self.line_edit_output_file = QLineEdit()
        widgets_row.append(self.line_edit_output_file)
        self.button_search_output_file = QPushButton("Обзор")
        widgets_row.append(self.button_search_output_file)
        return widgets_row

    def __connect_buttons(self) -> None:
        self.button_search_input_file.clicked.connect(self.__search_input_button_clicked)
        self.button_search_output_file.clicked.connect(self.__search_output_button_clicked)
        self.button_start.clicked.connect(self.__start_button_clicked)

    def __init_layout(self, widgets: list[list]) -> None:
        for i, row in enumerate(widgets):
            for j, widget in enumerate(row):
                if i == 2:
                    j += 2
                self.layout.addWidget(widget, i, j)
        self.layout.setColumnMinimumWidth(1, 250)

    def __set_text_to_line_edit(self, input_path, output_path) -> None:
        if input_path:
            input_path = PathHelper.to_absolute(input_path)
            self.line_edit_input_file.setText(input_path)
        if output_path:
            output_path = PathHelper.to_absolute(output_path)
            self.line_edit_output_file.setText(output_path)


class Application:
    @staticmethod
    def start(conversion_manager: ConversionManager, input_path: str, output_path: str) -> None:
        app = QApplication([])
        app.setWindowIcon(QIcon('icons/RST.ico'))

        window = MainWindow(conversion_manager, input_path, output_path)
        window.show()

        app.exec()
