import exceptions
import factory
from data_sources.dispatcher import DataSourceDispatcher
from xsdata.formats.dataclass.serializers import XmlSerializer


class ConversionManager:
    def __init__(self, serializer: XmlSerializer, dispatcher: DataSourceDispatcher) -> None:
        self.serializer: XmlSerializer = serializer
        self.dispatcher: DataSourceDispatcher = dispatcher

    def convert(self, input_filename: str, output_filename: str, data_source: str) -> None:
        verifications = self.dispatcher.get_data_generator_by_source_name(data_source, input_filename)
        application = factory.ApplicationFactory.create_application(verifications)
        xml_string = self.serializer.render(application)
        self.__write_to_file(xml_string, output_filename)

    @staticmethod
    def __write_to_file(xml: str, file_path: str) -> None:
        try:
            file = open(file_path, 'w')
        except PermissionError:
            raise exceptions.FilePermissionError('Файл недоступен для записи', file_path)
        file.write(xml)
        file.close()
