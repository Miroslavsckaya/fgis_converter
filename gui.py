from converter import convert_csv_to_xml_file
import PySimpleGUIQt as sg


class GuiFrontend:
    def Start(self):
        text = sg.popup_get_file('Выберите файл', title='Аршин', keep_on_top=True)
        if text[:7] == 'file://':
            text = text[7:]
        elif text[:6] == 'file:/':
            text = text[5:]
        convert_csv_to_xml_file(text)
