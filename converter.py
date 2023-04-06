import csv
import exceptions
import factory
from chardet.universaldetector import UniversalDetector
from models.arshin import Application
from xsdata.formats.dataclass.serializers import XmlSerializer


def detect_encoding(file):
    detector = UniversalDetector()
    for line in file:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    return detector.result['encoding']


def convert_csv_to_xml_file(input_filename, output_filename):
    application = Application()

    try:
        file = open(input_filename, 'rb')
    except FileNotFoundError:
        raise exceptions.FileDoesNotExistError(f'Файл не найден: {input_filename}')

    encoding = detect_encoding(file)
    file.close()

    file = open(input_filename, 'r', encoding=encoding)
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        if all(string == '' for string in row):
            continue
        verification = factory.RecInfoFactory.create_verification_from_csv_row(row)
        application.result.append(verification)
    file.close()

    serializer = XmlSerializer()
    with open(f'{output_filename}.xml', 'w', encoding='UTF-8') as file:
        serializer.write(file, application)
