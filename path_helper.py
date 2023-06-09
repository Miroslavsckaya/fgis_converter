import pathlib


class PathHelper:
    @staticmethod
    def to_absolute(relative: str) -> str:
        return str(pathlib.Path(relative).resolve())

    @staticmethod
    def replace_suffix(input_path: str, extension: str) -> str:
        if not input_path:
            return ''
        return str(pathlib.Path(input_path).with_suffix(extension))
