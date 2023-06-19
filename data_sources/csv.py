import csv
import logging
import re
from data_sources.base import BaseFileDataSource
from data_sources.interface import DataSourceInterface, VerificationData
from typing import Generator


class CsvDataSource(BaseFileDataSource, DataSourceInterface):
    def __init__(self, delimiter: str = ';') -> None:
        self.__delimiter: str = delimiter

    def get_name(self) -> str:
        return 'csv'

    def get_verification_generator(self, file_path: str) -> Generator[VerificationData, None, None]:
        file = self._open_file(file_path, 'r')
        reader = csv.reader(file, delimiter=self.__delimiter)
        for row in reader:
            verification_data = self.__convert_to_verification_data(row, reader.line_num)
            if verification_data is None:
                continue
            yield verification_data
        file.close()

    @staticmethod
    def __convert_to_verification_data(row: list[str], line_num: int) -> VerificationData | None:
        """Expected order:
            1) registration number, 2) factory number, 3) modification, 4) verification date, 5) valid date,
            6) metrologist, 7) test device number, 8) temperature, 9) pressure, 10) humidity"""
        if not all(row[:4] + row[5:10]):
            logging.warning(f'Строка №{line_num} не может быть cконвертирована. Все поля должны быть заполнены')
            return None
        return VerificationData(reg_num=re.sub(r' +', '', row[0]), factory_num=re.sub(r' +', '', row[1]), 
                                modification=row[2], ver_date=row[3], valid_date=row[4], metrologist=row[5], 
                                test_dev_num=row[6], temperature=row[7], pressure=row[8], humidity=row[9])
