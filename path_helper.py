import pathlib


class PathHelper:
    @staticmethod
    def to_absolute(relative: str):
        return str(pathlib.Path(relative).resolve())

    @staticmethod
    def change_suffix(input_path: str):
        return str(pathlib.Path(input_path).with_suffix('.xml'))
