from typing import List
from src.pdf.event import event
from src.pdf.appsvc.pdfappsvc import IPDFAppSevice
from src.pdf.repo.pdfrepo import IPDFRepository


#################
# Event Objects Only Used for Test
#################
class EventTestEntries(event.PDFEvent):
    def __init__(self, entries: dict):
        self.entries = entries


#################
# Mock of pdf-application-service
#################
class MockPDFAppService(IPDFAppSevice):
    def __init__(self, pdf_repository: IPDFRepository):
        self.__es = event.get_event_subject()

    def concat_pdf(self, pdfsrcpaths: List[str], pdfdst: str) -> None:
        ret = {'pdfsrcpaths': pdfsrcpaths,
               'pdfdst': pdfdst}
        self.__es.notify(EventTestEntries(ret))

    def decrypt_pdf(self, pdfsrcpath: str,
                    password: str, pdfdstpath: str) -> None:
        ret = {'pdfsrcpath': pdfsrcpath,
               'password': password,
               'pdfdstpath': pdfdstpath}
        self.__es.notify(EventTestEntries(ret))

    def encrypt_pdf(self, pdfsrcpath: str, pdfdstpath: str,
                    writepass: str, readpass: str = '') -> None:
        ret = {'pdfsrcpath': pdfsrcpath,
               'writepass': writepass,
               'pdfdstpath': pdfdstpath,
               'readpass': readpass}
        self.__es.notify(EventTestEntries(ret))


#################
# Mock of pdf-repository
#################
class MockPDFRepository(IPDFRepository):
    pass
