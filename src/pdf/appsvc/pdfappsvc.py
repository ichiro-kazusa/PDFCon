from ..event import error
from ..domain.pdffile import PdfSrcList, PdfDstFile, PdfSrcFile
from ..repo.pdfrepo import IPDFRepository
from ..domain.encrypt import Encryption


class PDFAppSevice:

    def __init__(self, pdf_repository: IPDFRepository):
        self.__pdfrepo = pdf_repository

    def concat_pdf(self, pdfsrcpaths: list[str], pdfdst: str) -> None:
        """application service function to concat pdfs"""

        sources = PdfSrcList.create_pdfsrclist_frompath(pdfsrcpaths)
        dest = PdfDstFile(pdfdst)

        # error check
        if sources.is_empty():
            raise error.InputFileNotSpecified()
        if dest.is_null():
            raise error.OutputFileNotSpccified()

        self.__pdfrepo.concat(sources, dest)

    def decrypt_pdf(self, pdfsrcpath: str,
                    password: str, pdfdstpath: str) -> None:
        """application service function to decrypt pdf"""

        source = PdfSrcFile(pdfsrcpath)
        dest = PdfDstFile(pdfdstpath)

        # error check
        if source.is_null():
            raise error.InputFileNotSpecified()
        if dest.is_null():
            raise error.OutputFileNotSpccified()

        self.__pdfrepo.decrypt(source, password, dest)

    def encrypt_pdf(self, pdfsrcpath: str, pdfdstpath: str,
                    writepass: str, readpass: str = '') -> None:
        """application service function to encrypt pdf"""
        source = PdfSrcFile(pdfsrcpath)
        dest = PdfDstFile(pdfdstpath)
        encrypt = Encryption(writepass, writepass)

        # error check
        if source.is_null():
            raise error.InputFileNotSpecified()
        if dest.is_null():
            raise error.OutputFileNotSpccified()

        self.__pdfrepo.encrypt(source, dest, encrypt, readpass)
