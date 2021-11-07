from abc import ABC
import pikepdf


from ..event import error, event
from ..domain.pdffile import PDFDstPath, PDFSrcPath, PDFSrcPathList
from ..domain.encrypt import Encryption
from ..domain.pdfinfo import PDFInfo
from ..domain.pages import PageList


class IPDFRepository(ABC):
    def __init__(self):
        pass

    def concat(self, pdfsrclist: PDFSrcPathList, pdfdst: PDFDstPath):
        pass

    def decrypt(self, pdfsrc: PDFSrcPath, password: str, pdfdst: PDFDstPath):
        pass

    def encrypt(self, pdfsrc: PDFSrcPath,
                pdfdst: PDFDstPath, password: Encryption,
                readpass: str):
        pass

    def retrieve_pdfinfo(self, pdfsrc: PDFSrcPath) -> PDFInfo:
        pass

    def extract(self, pdfsrc: PDFSrcPath,
                pagelist: PageList, pdfdst: PDFDstPath):
        pass


class PikePDFRepository(IPDFRepository):

    def __init__(self):
        self.__es = event.get_event_subject()

    def concat(self, pdfsrclist: PDFSrcPathList, pdfdst: PDFDstPath):
        doc_save = pikepdf.new()

        for file in pdfsrclist.iter():
            try:
                with pikepdf.open(file.path) as doc:
                    self.__es.notify(event.EventFileRead(file.path))

                    doc_save.pages.extend(doc.pages)
            except FileNotFoundError:
                raise error.FileReadError(file.path)
            except pikepdf.PdfError:
                raise error.NotPDFFileError(file.path)
            except pikepdf.PasswordError:
                self.__es.notify(event.EventFileRead(file.path))
                raise error.ConcatEncryptedError(file.path)

        self.__es.notify(event.EventFileWrite(pdfdst.path))
        doc_save.save(pdfdst.path)
        self.__es.notify(event.EventConcatComplete())

    def decrypt(self, pdfsrc: PDFSrcPath, password: str, pdfdst: PDFDstPath):
        try:
            with pikepdf.open(pdfsrc.path, password=password) as document:
                self.__es.notify(event.EventFileRead(pdfsrc.path))

                if not document.is_encrypted:
                    raise error.DecryptUnencryptedError()

                self.__es.notify(event.EventFileWrite(pdfdst.path))
                document.save(pdfdst.path)
                self.__es.notify(event.EventDecryptComplete())

        except FileNotFoundError:
            raise error.FileReadError(pdfsrc.path)
        except pikepdf.PdfError:
            raise error.NotPDFFileError(pdfsrc.path)
        except pikepdf.PasswordError:
            self.__es.notify(event.EventFileRead(pdfsrc.path))
            raise error.DecryptPasswordFail()

    def encrypt(self, pdfsrc: PDFSrcPath,
                pdfdst: PDFDstPath, encryption: Encryption,
                readpass: str = ''):
        try:
            with pikepdf.open(pdfsrc.path, password=readpass) as document:
                self.__es.notify(event.EventFileRead(pdfsrc.path))

                enc = pikepdf.models.Encryption(owner=encryption.owner,
                                                user=encryption.user)

                self.__es.notify(event.EventFileWrite(pdfdst.path))
                document.save(pdfdst.path, encryption=enc)
                self.__es.notify(event.EventEncryptComplete())

        except FileNotFoundError:
            raise error.FileReadError(pdfsrc.path)
        except pikepdf.PdfError:
            raise error.NotPDFFileError(pdfsrc.path)
        except pikepdf.PasswordError:
            self.__es.notify(event.EventFileRead(pdfsrc.path))
            raise error.DecryptPasswordFail()

    def retrieve_pdfinfo(self, pdfsrc: PDFSrcPath) -> PDFInfo:
        try:
            with pikepdf.open(pdfsrc.path) as document:
                numofpages: int = len(document.pages)
                return PDFInfo(pdfsrc, numofpages)

        except FileNotFoundError:
            raise error.FileReadError(pdfsrc.path)
        except pikepdf.PdfError:
            raise error.NotPDFFileError(pdfsrc.path)
        except pikepdf.PasswordError:
            raise error.DecryptPasswordFail()

    def extract(self, pdfsrc: PDFSrcPath,
                pagelist: PageList, pdfdst: PDFDstPath):
        try:
            with pikepdf.open(pdfsrc.path) as document:
                self.__es.notify(event.EventFileRead(pdfsrc.path))

                # backup all pages to memory
                page_backup = pikepdf.Pdf.new()
                page_backup.pages.extend(document.pages)

                # delete all pages
                del document.pages[:]

                # re-append pages from backup by pagelist
                for pageidx in pagelist.as_zero_based_list():
                    document.pages.append(page_backup.pages[pageidx])

                self.__es.notify(event.EventFileWrite(pdfdst.path))
                document.save(pdfdst.path)
                self.__es.notify(event.EventExtractComplete())

        except FileNotFoundError:
            raise error.FileReadError(pdfsrc.path)
        except pikepdf.PdfError:
            raise error.NotPDFFileError(pdfsrc.path)
        except pikepdf.PasswordError:
            self.__es.notify(event.EventFileRead(pdfsrc.path))
            raise error.DecryptPasswordFail()
