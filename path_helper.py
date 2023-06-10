import pathlib


class PathHelper:
    @staticmethod
    def get_abspath(path: str):
        return str(pathlib.Path(path).resolve())

    @staticmethod
    def change_suffix(input_path: str):
        a = pathlib.Path(input_path).with_suffix('.xml')
        return str(a)
