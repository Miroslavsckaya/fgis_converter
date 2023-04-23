import exceptions
from chardet.universaldetector import UniversalDetector
from data_sources.interface import DataSourceInterface
from typing import BinaryIO, IO


class BaseDataSource(DataSourceInterface):
    __NAME: str = 'base_data_source_class'

    def get_name(self) -> str:
        return self.__NAME

    def open_file(self, path: str, mode: str) -> IO:
        try:
            file = open(path, 'rb')
        except FileNotFoundError:
            raise exceptions.FileDoesNotExistError('Файл не найден:', path)
        except PermissionError:
            raise exceptions.FilePermissionError('Файл недоступен для чтения:', path)
        encoding = self.detect_encoding(file)
        file.close()
        return open(path, mode, encoding=encoding)

    @staticmethod
    def detect_encoding(file: BinaryIO) -> str:
        detector = UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']

