from abc import ABC, abstractmethod
from typing import Generator


class DataSourceInterface(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_verification_generator(self, file_path: str) -> Generator[VerificationData, None, None]:
        pass


class VerificationData:
    def __init__(self, reg_num: str, factory_num: str, modification: str, ver_date: str,
                 valid_date: str, metrologist: str, test_dev_num: str, pressure: str,
                 temperature: str, humidity: str) -> None:
        self.__reg_num: str = reg_num
        self.__factory_num: str = factory_num
        self.__modification: str = modification
        self.__ver_date: str = ver_date
        self.__valid_date: str = valid_date
        self.__metrologist: str = metrologist
        self.__test_dev_num: str = test_dev_num
        self.__pressure: str = pressure
        self.__temperature: str = temperature
        self.__humidity: str = humidity

    @property
    def reg_num(self):
        return self.__reg_num

    @property
    def factory_num(self):
        return self.__factory_num

    @property
    def modification (self):
        return self.__modification

    @property
    def ver_date(self):
        return self.__ver_date

    @property
    def valid_date(self):
        return self.__valid_date

    @property
    def metrologist(self):
        return self.__metrologist

    @property
    def test_dev_num(self):
        return self.__test_dev_num

    @property
    def pressure(self):
        return self.__pressure

    @property
    def temperature(self):
        return self.__temperature

    @property
    def humidity(self):
        return self.__humidity
