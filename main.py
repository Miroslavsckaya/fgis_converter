#! python
import argparse
from converter import convert_csv_to_xml_file
import gui

parser = argparse.ArgumentParser()
parser.add_argument('path_input', default=None, nargs='?')
parser.add_argument('path_output', default='./application', nargs='?')
args = vars(parser.parse_args())

if args['path_input'] is None:
    window = gui.GuiFrontend()
    window.Start()
else:
    convert_csv_to_xml_file(args['path_input'], args['path_output'])
