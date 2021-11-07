
from test.utilities import TestEventListener, verify_error

import pytest
from src.pdf.appsvc import PDFAppSevice
from src.pdf.event import error, event
from src.pdf.repo.pdfrepo import PikePDFRepository
from src.pdf.domain.pdffile import PDFSrcPath, PDFDstPath

repo = PikePDFRepository()
app_service = PDFAppSevice(repo)


def test_extract_normal():
    el = TestEventListener()

    src = r'test/rsc/multipage.pdf'
    dst = r'test/rsc/extract.pdf'

    app_service.extract_pdf(src, '1-4, 8-end, 3-1, 10-7, 5', dst)

    expected_events = [event.EventFileRead(src),
                       event.EventFileWrite(dst),
                       event.EventExtractComplete()]
    assert el.verify_history(expected_events)


def test_extract_outofrange():
    src = r'test/rsc/multipage.pdf'
    dst = r'test/rsc/extract.pdf'

    with pytest.raises(error.PageIndexOutOfRange) as e:
        app_service.extract_pdf(src, '2-11', dst)

    assert verify_error(e.value, error.PageIndexOutOfRange())


def test_extract_nosource():
    src = r''
    dst = r'test/rsc/extract.pdf'

    with pytest.raises(error.InputFileNotSpecified) as e:
        app_service.extract_pdf(src, '2-11', dst)

    assert verify_error(e.value, error.InputFileNotSpecified())


def test_extract_nodest():
    src = r'test/rsc/multipage.pdf'
    dst = r''

    with pytest.raises(error.OutputFileNotSpccified) as e:
        app_service.extract_pdf(src, '2-11', dst)

    assert verify_error(e.value, error.OutputFileNotSpccified())


def test_extract_filenotfound():
    src = r'test/rsc/notfound.pdf'
    dst = r'test/rsc/extract.pdf'

    with pytest.raises(error.FileReadError) as e:
        repo.extract(PDFSrcPath(src), '1-10', PDFDstPath(dst))

    assert verify_error(e.value, error.FileReadError(src))


def test_extract_notpdf():
    src = r'test/rsc/non-pdf.pdf'
    dst = r'test/rsc/extract.pdf'

    with pytest.raises(error.NotPDFFileError) as e:
        repo.extract(PDFSrcPath(src), '1-10', PDFDstPath(dst))

    assert verify_error(e.value, error.NotPDFFileError(src))


def test_extract_passwordfail():
    src = r'test/rsc/encrypted.pdf'
    dst = r'test/rsc/extract.pdf'

    with pytest.raises(error.DecryptPasswordFail) as e:
        repo.extract(PDFSrcPath(src), '1-10', PDFDstPath(dst))

    assert verify_error(e.value, error.DecryptPasswordFail())
