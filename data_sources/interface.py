from abc import ABC, abstractmethod
from typing import Generator


class VerificationData:
    pass


class DataSourceInterface(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @staticmethod
    @abstractmethod
    def get_verification_generator(file_path: str) -> Generator[VerificationData, None, None]:
        pass
