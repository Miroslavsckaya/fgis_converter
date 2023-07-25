import exceptions
from chardet.universaldetector import UniversalDetector
from typing import BinaryIO, IO


class BaseFileDataSource:
    def _open_file(self, path: str, mode: str) -> IO:
        try:
            file = open(path, 'rb')
        except FileNotFoundError:
            raise exceptions.FileDoesNotExistError('Файл не найден:', path)
        except PermissionError:
            raise exceptions.FilePermissionError('Файл недоступен для чтения:', path)
        encoding = self.__detect_encoding(file)
        file.close()
        return open(path, mode, encoding=encoding)

    @staticmethod
    def __detect_encoding(file: BinaryIO) -> str:
        detector = UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']
    