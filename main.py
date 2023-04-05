#! python
import argparse
from converter import convert_csv_to_xml_file
import logging
import PySimpleGUIQt as sg
from sys import exit
from urllib.parse import urlparse


def convert(path_input, path_output, cli):
    try:
        convert_csv_to_xml_file(path_input, path_output)
    except Exception as err:
        print_error(str(err), cli)
        exit(1)


def print_error(message, cli):
    logging.error(message)
    if not cli:
        sg.popup_error(message)


parser = argparse.ArgumentParser()
parser.add_argument('--cli', action='store_true')
parser.add_argument('path_input', default=None, nargs='?')
parser.add_argument('path_output', default='./application', nargs='?')
args = vars(parser.parse_args())
is_cli = args['cli']

if not is_cli:
    default_path = '' if args['path_input'] is None else args['path_input']
    file_path = sg.popup_get_file('Выберите файл для конвертации', title='Аршин', keep_on_top=True, default_path=default_path, file_types=(("CSV Files","*.csv"),))
    url = urlparse(file_path, allow_fragments=False)
    if not url.path:
        print_error('Пустой путь', is_cli)
        exit(1)
    if url.scheme in ('file', ''):
        convert(url.path, args['path_output'], is_cli)
    else:
        print_error(f'Неподдерживаемая схема: {url.scheme }', is_cli)
        exit(1)
else:
    convert(args['path_input'], args['path_output'], is_cli)
