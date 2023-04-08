import exceptions
from data_sources.interface import VerificationData, DataSourceInterface
from typing import Generator


class DataSourceDispatcher:
    def __init__(self, *args: DataSourceInterface) -> None:
        self.__sources: dict[DataSourceInterface] = {}
        for source in args:
            self.register_source(source)

    def register_source(self, source: DataSourceInterface) -> None:
        if not isinstance(source, DataSourceInterface):
            raise exceptions.DataSourceInterfaceError('Only DataSourceInterface implementations are supported')
        self.__sources[source.get_name()] = source

    def get_data_generator_by_source_name(self, data_source: str, file_name: str) -> Generator[VerificationData]:
        if data_source not in self.__sources:
            raise exceptions.UnsupportedDataSourceError('Источник данных не поддерживается', data_source,
                                                        'Поддерживаемые источники:', *self.__sources)
        return self.__sources[data_source].get_verification_generator(file_name)
