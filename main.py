#! python
import argparse
from converter import convert_csv_to_xml_file
import exceptions
import logging
import PySimpleGUIQt as sg
from sys import exit
from urllib.parse import urlparse


def convert(path_input: str, path_output: str, cli: bool) -> None:
    try:
        convert_csv_to_xml_file(path_input, path_output)
    except Exception as err:
        print_error(err, cli)
        exit(1)


def print_error(err: Exception, cli: bool) -> None:
    logging.error(err)
    if not cli:
        sg.popup_error(*err.args)


parser = argparse.ArgumentParser()
parser.add_argument('--cli', action='store_true')
parser.add_argument('path_input', default='', nargs='?')
parser.add_argument('path_output', default='./application', nargs='?')
args = vars(parser.parse_args())
is_cli = args['cli']

if not is_cli:
    file_path = sg.popup_get_file('Выберите файл для конвертации', title='Аршин', keep_on_top=True, default_path=args['path_input'], file_types=(("CSV Files","*.csv"),))
    if file_path is None:
        exit()

    url = urlparse(file_path, allow_fragments=False)
    if not url.path:
        print_error(exceptions.FilePathError('Пустой путь'), is_cli)
        exit(1)
    if url.scheme in ('file', ''):
        convert(url.path, args['path_output'], is_cli)
    else:
        print_error(exceptions.FilePathError('Неподдерживаемая схема:', url.scheme), is_cli)
        exit(1)
else:
    convert(args['path_input'], args['path_output'], is_cli)
