#! python
import argparse
from converter import convert_csv_to_xml_file
import logging
import PySimpleGUIQt as sg
from sys import exit
from urllib.parse import urlparse

parser = argparse.ArgumentParser()
parser.add_argument('path_input', default=None, nargs='?')
parser.add_argument('path_output', default='./application', nargs='?')
args = vars(parser.parse_args())

if args['path_input'] is None:
    file_path = sg.popup_get_file('Выберите файл для конвертации', title='Аршин', keep_on_top=True)
    url = urlparse(file_path, allow_fragments=False)
    if url.scheme in ('file', ''):
        convert_csv_to_xml_file(url.path)
    else:
        logging.error('unsupported scheme')
        exit(1)
else:
    convert_csv_to_xml_file(args['path_input'], args['path_output'])
