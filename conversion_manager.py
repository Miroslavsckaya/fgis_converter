import data_sources
import exceptions
import factory
from xsdata.formats.dataclass.serializers import XmlSerializer


class ConversionManager:
    serializer = XmlSerializer()

    @classmethod
    def convert(cls, input_filename: str, output_filename: str, par: str) -> None:
        data_source = cls.get_data_source(par)
        verification_dto = data_source.get_verfication_dto(input_filename)
        application_xml = factory.ApplicationFactory(verification_dto)
        xml_string = cls.serializer.render(application_xml)
        cls.write_to_output(xml_string, output_filename)

    @staticmethod
    def get_data_source(par: str) -> Any:
        data_source = None
        if par == 'csv':
            data_source = data_sources.csv.DataSourceScv
        return data_source

    @staticmethod
    def write_to_output(xml_str: str, output: str) -> None:
        try:
            file = open(output, 'w')
        except PermissionError:
            raise exceptions.FilePermissionError('Файл недоступен для записи', output)
        file.write(xml_str)
        file.close()
