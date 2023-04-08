import data_sources
import exceptions
import factory
from xsdata.formats.dataclass.serializers import XmlSerializer


class ConversionManager:
    def __init__(self, serializer: XmlSerializer) -> None:
        self.serializer = serializer

    def convert(self, input_filename: str, output_filename: str, par: str) -> None:
        data_source = self.get_data_source(par)
        verification_dto = data_source.get_verfication_dto(input_filename)
        application_xml = factory.ApplicationFactory(verification_dto)
        xml_string = self.serializer.render(application_xml)
        self.write_to_output(xml_string, output_filename)

    @staticmethod
    def get_data_source(par: str) -> Any:
        data_source = None
        if par == 'csv':
            data_source = data_sources.csv.DataSourceScv
        return data_source

    @staticmethod
    def write_to_file(xml_str: str, file_path: str) -> None:
        try:
            file = open(file_path, 'w')
        except PermissionError:
            raise exceptions.FilePermissionError('Файл недоступен для записи', file_path)
        file.write(xml_str)
        file.close()
