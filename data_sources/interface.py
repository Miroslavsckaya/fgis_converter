from abc import ABC, abstractmethod
from exceptions import VerificationKeyError
from typing import Generator


class VerificationData:
    def __init__(self, info: dict) -> None:
        """Expected keys in the dict"""
        keys = ['reg_num', 'factory_num', 'modification', 'ver_date', 'valid_date',
                'metrologist', 'test_dev_num', 'pressure', 'temperature', 'humidity']
        for key in keys:
            try:
                self.__dict__[f'_VerificationData__{key}'] = info[key]
            except KeyError:
                raise VerificationKeyError('Missing key:', key)

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


class DataSourceInterface(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_verification_generator(self, file_path: str) -> Generator[VerificationData, None, None]:
        pass

