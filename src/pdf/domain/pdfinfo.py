from .pdffile import PDFSrcPath


class PDFInfo:

    def __init__(self, pdfpath: PDFSrcPath, numofpages: int) -> None:
        self.__PDFPath = pdfpath
        self.__NumOfPages = numofpages

    @property
    def PDFPath(self) -> PDFSrcPath:
        return self.__PDFPath

    @property
    def NumOfPages(self) -> int:
        return self.__NumOfPages
