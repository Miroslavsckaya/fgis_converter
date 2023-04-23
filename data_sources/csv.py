import csv
import logging
from data_sources.base import BaseDataSource
from data_sources.interface import VerificationData
from typing import Generator


class CsvDataSource(BaseDataSource):
    def __init__(self, delimiter: str = ';') -> None:
        self.__NAME = 'csv'
        self.__delimiter = delimiter

    def get_name(self) -> str:
        return self.__NAME

    def get_verification_generator(self, file_path: str) -> Generator[VerificationData, None, None]:
        file = self.open_file(file_path, 'r')
        reader = csv.reader(file, delimiter=self.__delimiter)
        for row in reader:
            verification_data = self.convert_to_verification_data(row, reader.line_num)
            if verification_data is None:
                continue
            yield verification_data
        file.close()

    @staticmethod
    def convert_to_verification_data(row: list[str], line_num: int) -> VerificationData | None:
        """Expected order:
            1) registration number, 2) factory number, 3) modification, 4) verification date, 5) valid date,
            6) metrologist, 7) test device number, 8) temperature, 9) pressure, 10) humidity"""
        if not all(row[:4] + row[5:]):
            logging.warning(f'Строка №{line_num} не может быть cконвертирована. Все поля должны быть заполнены')
            return None
        return VerificationData(*row)
