#! python
import gui
import argparse
import exceptions
import logging
from conversion_manager import ConversionManager
from data_sources.csv import CsvDataSource
from data_sources.dispatcher import DataSourceDispatcher
from sys import exit
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


def convert(input_path: str, output_path: str, manager: ConversionManager,
            data_source: str, cli: bool) -> None:
    try:
        manager.convert(input_path, output_path, data_source)
    except Exception as err:
        print_error(err, cli)
        exit(1)


def print_error(err: Exception, cli: bool) -> None:
    logging.error(err)
    if not cli:
        sg.popup_error(*err.args)


def get_output_path(input_path: str, output_path: str | None) -> str:
    if output_path is None:
        return input_path + '.xml'
    return output_path


dispatcher = DataSourceDispatcher(CsvDataSource())
serializer_config = SerializerConfig(pretty_print=True)
xml_serializer = XmlSerializer(config=serializer_config)
conversion_manager = ConversionManager(xml_serializer, dispatcher)

parser = argparse.ArgumentParser()
parser.add_argument('--cli', action='store_true')
parser.add_argument('input_path', default='', nargs='?')
parser.add_argument('output_path', nargs='?')
args = vars(parser.parse_args())
is_cli = args['cli']

if not is_cli:
    gui.Application.start(conversion_manager)
else:
    output_path = get_output_path(args['input_path'], args['output_path'])
    convert(args['input_path'], output_path, conversion_manager, 'csv', is_cli)
