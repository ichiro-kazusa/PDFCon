

class PDFError(Exception):
    pass


######################
# General Errors
######################
class FileReadError(PDFError):
    def __init__(self, path: str) -> None:
        self.path = path


class NotPDFFileError(PDFError):
    def __init__(self, path: str) -> None:
        self.path = path


class InputFileNotSpecified(PDFError):
    pass


class OutputFileNotSpccified(PDFError):
    pass


######################
# Concat Errors
######################
class ConcatEncryptedError(PDFError):
    def __init__(self, path: str) -> None:
        self.path = path


######################
# Decrypt Errors
######################
class DecryptUnencryptedError(PDFError):
    pass


class DecryptPasswordFail(PDFError):
    pass


######################
# Extract Errors
######################
class InvalidPageList(PDFError):
    pass


class PageIndexOutOfRange(PDFError):
    pass
