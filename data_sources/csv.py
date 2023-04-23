import csv
from data_sources.base import BaseDataSource
from interface import VerificationData
from typing import Generator


class CsvDataSource(BaseDataSource):
    def __init__(self, delimiter=';') -> None:
        self.__NAME = 'csv'
        self.__delimiter = delimiter

    def get_verification_generator(self, file_path: str) -> Generator[VerificationData, None, None]:
        file = self.open_file(file_path, 'r')
        reader = csv.reader(file, delimiter=self.__delimiter)
        for row in reader:
            yield self.convert_to_verification_data(row)
        file.close()

    def convert_to_verification_data(self, row: list[str]) -> VerificationData:
        pass
