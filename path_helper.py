import pathlib


class PathHelper:
    @staticmethod
    def to_absolute(relative: str) -> str:
        return str(pathlib.PurePath(relative).resolve())

    @staticmethod
    def replace_suffix(input_path: str, extension: str) -> str:
        if not input_path:
            return ''
        return str(pathlib.PurePath(input_path).with_suffix(extension))
