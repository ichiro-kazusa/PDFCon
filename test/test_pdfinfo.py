from test.utilities import verify_error

import pytest
from src.pdf.repo.pdfrepo import PikePDFRepository
from src.pdf.domain.pdfinfo import PDFInfo
from src.pdf.domain.pdffile import PDFSrcPath
from src.pdf.event import error


repo = PikePDFRepository()


def test_pdfinfo_maxpagenum():
    src = r'test/rsc/multipage.pdf'
    srcobj = PDFSrcPath(src)
    info: PDFInfo = repo.retrieve_pdfinfo(srcobj)
    assert info.PDFPath.path == src
    assert info.NumOfPages == 10


def test_pdfinfo_filenotfound():
    src = r'test/rsc/q.pdf'
    srcobj = PDFSrcPath(src)

    with pytest.raises(error.FileReadError) as e:
        repo.retrieve_pdfinfo(srcobj)

    assert verify_error(e.value, error.FileReadError(src))


def test_pdfinfo_notpdf():
    src = r'test/rsc/non-pdf.pdf'
    srcobj = PDFSrcPath(src)

    with pytest.raises(error.NotPDFFileError) as e:
        repo.retrieve_pdfinfo(srcobj)

    assert verify_error(e.value, error.NotPDFFileError(src))


def test_pdfinfo_passwordfail():
    src = r'test/rsc/encrypted.pdf'
    srcobj = PDFSrcPath(src)

    with pytest.raises(error.DecryptPasswordFail) as e:
        repo.retrieve_pdfinfo(srcobj)

    assert verify_error(e.value, error.DecryptPasswordFail())
