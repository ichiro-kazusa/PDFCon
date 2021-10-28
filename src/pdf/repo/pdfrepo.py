from abc import ABC
import pikepdf


from ..event import error, event
from ..domain.pdffile import PdfDstFile, PdfSrcFile, PdfSrcList
from ..domain.encrypt import Encryption


class IPDFRepository(ABC):
    def __init__(self):
        pass

    def concat(self, pdfsrclist: PdfSrcList, pdfdst: PdfDstFile):
        pass

    def decrypt(self, pdfsrc: PdfSrcFile, password: str, pdfdst: PdfDstFile):
        pass

    def encrypt(self, pdfsrc: PdfSrcFile,
                pdfdst: PdfDstFile, password: Encryption,
                readpass: str):
        pass


class PikePDFRepository(IPDFRepository):

    def __init__(self):
        self.__es = event.get_event_subject()

    def concat(self, pdfsrclist: PdfSrcList, pdfdst: PdfDstFile):
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

    def decrypt(self, pdfsrc: PdfSrcFile, password: str, pdfdst: PdfDstFile):
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

    def encrypt(self, pdfsrc: PdfSrcFile,
                pdfdst: PdfDstFile, encryption: Encryption,
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
