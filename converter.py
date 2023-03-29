import csv
from models.arshin import Application
from xsdata.formats.dataclass.serializers import XmlSerializer
import factory


def CsvToXmlConverter(input_filename, output_filename='application'):
    application = Application()

    with open(input_filename, 'r', encoding='Windows-1251') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if all(string == '' for string in row):
                break
            verification = factory.RecInfoFactory.create_verification_from_csv_row(row)
            application.result.append(verification)

    xml_creator = XmlSerializer()
    with open(f'{output_filename}.xml', 'w', encoding='UTF-8') as file:
        xml_creator.write(file, application)
