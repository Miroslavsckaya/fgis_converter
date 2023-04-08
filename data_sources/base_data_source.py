import exceptions
from data_sources.interface import DataSourceInterface


class BaseDataSource(DataSourceInterface):
    __NAME = 'Base data source class'

    def get_name(self):
        return self.__NAME

    @staticmethod
    def check_permission_file(path):
        try:
            file = open(path, 'rb')
        except FileNotFoundError:
            raise exceptions.FileDoesNotExistError('Файл не найден:', path)
        except PermissionError:
            raise exceptions.FilePermissionError('Файл недоступен для чтения:', path)
        file.close()
