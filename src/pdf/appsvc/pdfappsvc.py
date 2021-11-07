from typing import List

from ..event import error
from ..domain.pdffile import PDFSrcPathList, PDFDstPath, PDFSrcPath
from ..domain.encrypt import Encryption
from ..domain.pages import PageListWithEnd, PageList
from ..repo.pdfrepo import IPDFRepository


class IPDFAppSevice:

    def __init__(self, pdf_repository: IPDFRepository):
        pass

    def concat_pdf(self, pdfsrcpaths: List[str], pdfdst: str) -> None:
        pass

    def decrypt_pdf(self, pdfsrcpath: str,
                    password: str, pdfdstpath: str) -> None:
        pass

    def encrypt_pdf(self, pdfsrcpath: str, pdfdstpath: str,
                    writepass: str, readpass: str = '') -> None:
        pass

    def extract_pdf(self, pdfsrcpath: str, pagestring: str,
                    pdfdstpath: str) -> None:
        pass


class PDFAppSevice(IPDFAppSevice):

    def __init__(self, pdf_repository: IPDFRepository):
        self.__pdfrepo = pdf_repository

    def concat_pdf(self, pdfsrcpaths: List[str], pdfdst: str) -> None:
        """application service function to concat pdfs"""

        sources = PDFSrcPathList.create_pdfsrclist_frompath(pdfsrcpaths)
        dest = PDFDstPath(pdfdst)

        # error check
        if sources.is_empty():
            raise error.InputFileNotSpecified()
        if dest.is_null():
            raise error.OutputFileNotSpccified()

        self.__pdfrepo.concat(sources, dest)

    def decrypt_pdf(self, pdfsrcpath: str,
                    password: str, pdfdstpath: str) -> None:
        """application service function to decrypt pdf"""

        source = PDFSrcPath(pdfsrcpath)
        dest = PDFDstPath(pdfdstpath)

        # error check
        if source.is_null():
            raise error.InputFileNotSpecified()
        if dest.is_null():
            raise error.OutputFileNotSpccified()

        self.__pdfrepo.decrypt(source, password, dest)

    def encrypt_pdf(self, pdfsrcpath: str, pdfdstpath: str,
                    writepass: str, readpass: str = '') -> None:
        """application service function to encrypt pdf"""
        source = PDFSrcPath(pdfsrcpath)
        dest = PDFDstPath(pdfdstpath)
        encrypt = Encryption(writepass, writepass)

        # error check
        if source.is_null():
            raise error.InputFileNotSpecified()
        if dest.is_null():
            raise error.OutputFileNotSpccified()

        self.__pdfrepo.encrypt(source, dest, encrypt, readpass)

    def extract_pdf(self, pdfsrcpath: str, pagestring: str,
                    pdfdstpath: str) -> None:

        source = PDFSrcPath(pdfsrcpath)
        pagelist = PageListWithEnd.create_pagelist_from_str(
            pagestring)  # raises InvalidPageString
        dest = PDFDstPath(pdfdstpath)

        # error check
        if source.is_null():
            raise error.InputFileNotSpecified()
        if dest.is_null():
            raise error.OutputFileNotSpccified()

        # retrieve information about PDF page number
        pdfinfo = self.__pdfrepo.retrieve_pdfinfo(source)

        # replace 'end' with NumOfPages
        pagelist_endreplaced = PageList(
            pagelist, pdfinfo.NumOfPages)  # raises PageIndexOutOfRange

        self.__pdfrepo.extract(source, pagelist_endreplaced, dest)
