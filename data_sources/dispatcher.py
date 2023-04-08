import exceptions
from _cython_0_29_32 import generator


class DataSourceDispatcher:
    def __init__(self, *args) -> None:
        self.__sources = {}
        for source in args:
            self.register_source(source)

    def register_source(self, source) -> None:
        self.__sources[source.get_name()] = source

    def get_data_generator_by_source_name(self, file_name: str, data_source: str) -> generator:
        if data_source not in self.__sources:
            raise exceptions.UnsupportedDataSourceError('Источник данных не поддерживается', data_source,
                                                        'Поддерживаемые источники:', *self.__sources)
        return self.__sources[data_source].get_verification_generator(file_name)
