#! python
import argparse
from converter import CsvToXmlConverter
import gui

parser = argparse.ArgumentParser()
parser.add_argument('path_input', default=None, nargs='?')
parser.add_argument('path_output', default='./application', nargs='?')
args = vars(parser.parse_args())

if args['path_input'] is None:
    window = gui.GuiFrontend()
    window.Start()
else:
    CsvToXmlConverter(args['path_input'], args['path_output'])
