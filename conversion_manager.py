import data_sources
import exceptions
import factory
from xsdata.formats.dataclass.serializers import XmlSerializer


class ConversionManager:
    def __init__(self, serializer: XmlSerializer, dispatcher: data_sources.dispatcher.DataSourceDispatcher) -> None:
        self.serializer = serializer
        self.dispatcher = dispatcher

    def convert(self, input_filename: str, output_filename: str, data_source: str) -> None:
        verification_dto = self.dispatcher.get_data_generator_by_source_name(input_filename, data_source)
        application_xml = factory.ApplicationFactory(verification_dto)
        xml_string = self.serializer.render(application_xml)
        self.write_to_output(xml_string, output_filename)

    @staticmethod
    def write_to_file(xml_str: str, file_path: str) -> None:
        try:
            file = open(file_path, 'w')
        except PermissionError:
            raise exceptions.FilePermissionError('Файл недоступен для записи', file_path)
        file.write(xml_str)
        file.close()
