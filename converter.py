import csv
import exceptions
import factory
from chardet.universaldetector import UniversalDetector
from arshin import Application
from typing import BinaryIO
from xsdata.formats.dataclass.serializers import XmlSerializer


def detect_encoding(file: BinaryIO) -> str:
    detector = UniversalDetector()
    for line in file:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    return detector.result['encoding']


def convert_csv_to_xml_file(input_filename: str, output_filename: str) -> None:
    application = Application()

    try:
        file = open(input_filename, 'rb')
    except FileNotFoundError:
        raise exceptions.FileDoesNotExistError('Файл не найден:', input_filename)
    except PermissionError:
        raise exceptions.FilePermissionError('Файл недоступен для чтения:', input_filename)

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
