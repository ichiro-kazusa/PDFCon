"""Domain objects about PDF file."""
# import re
from typing import Generator, List


class PDFSrcPath:
    """Value Object which specifies PDF source file"""

    __slots__ = ["__srcpath"]

    def __init__(self, pdfsrcpath: str):
        self.__srcpath = pdfsrcpath

    @property
    def path(self) -> str:
        return self.__srcpath

    def equal(self, otherpath: str) -> bool:
        return self.__srcpath == otherpath

    def is_null(self) -> bool:
        return self.path == ""


class PDFSrcPathList:
    """First Class Collection to handle PdfSrcFile object"""

    def __init__(self, pdfsrcfiles: List[PDFSrcPath] = None):
        self.__pdfsrclist = [] if pdfsrcfiles is None else pdfsrcfiles

    def append(self, pdfsrc: PDFSrcPath) -> None:
        self.__pdfsrclist.append(pdfsrc)

    def iter(self) -> Generator[PDFSrcPath, None, None]:
        return (e for e in self.__pdfsrclist)

    def is_empty(self) -> bool:
        return len(self.__pdfsrclist) == 0

    @staticmethod
    def create_pdfsrclist_frompath(pdfsrcpaths: List[str]):
        sources = PDFSrcPathList()
        for path in pdfsrcpaths:
            srcfile = PDFSrcPath(path)
            sources.append(srcfile)
        return sources


class PDFDstPath:
    """Value Object which specifies PDF destination file"""

    __slots__ = ["__dstpath"]

    def __init__(self, pdfdstpath: str):
        self.__dstpath = pdfdstpath

    @property
    def path(self) -> str:
        return self.__dstpath

    def equal(self, otherpath: str) -> bool:
        return self.__dstpath == otherpath

    def is_null(self) -> bool:
        return self.path == ""
