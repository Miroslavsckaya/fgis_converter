from abc import ABC, abstractmethod


class DataSourceInterface(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @staticmethod
    @abstractmethod
    def get_verification_generator(file_path):
        pass


class VerificationData:
    pass
