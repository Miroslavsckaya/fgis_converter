class FileError(Exception):
    pass


class FileDoesNotExistError(FileError):
    pass


class FileEncodingError(FileError):
    pass


class FilePathError(FileError):
    pass


class FilePermissionError(FileError):
    pass


class DateError(Exception):
    pass


class DataSourceError(Exception):
    pass


class UnsupportedDataSourceError(DataSourceError):
    pass
