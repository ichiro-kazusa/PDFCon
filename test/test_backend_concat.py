
from test.utilities import TestEventListener, verify_error

import pytest
from src.pdf.appsvc import PDFAppSevice
from src.pdf.event import error, event
from src.pdf.repo.pdfrepo import PikePDFRepository

repo = PikePDFRepository()
app_service = PDFAppSevice(repo)


def test_concat_normal_multiple_file():
    el = TestEventListener()

    src = [r'test\rsc\a.pdf', r'test\rsc\b.pdf']
    dst = r'test\rsc\z.pdf'
    app_service.concat_pdf(src, dst)

    expected_events = [event.EventFileRead(src[0]),
                       event.EventFileRead(src[1]),
                       event.EventFileWrite(dst),
                       event.EventConcatComplete()]

    assert el.verify_history(expected_events)


def test_concat_error_source_open_fail():
    el = TestEventListener()

    src = [r'test\rsc\a.pdf', r'test\rsc\ab.pdf']
    dst = r'test\rsc\z.pdf'

    with pytest.raises(error.FileReadError) as e:
        app_service.concat_pdf(src, dst)

    assert verify_error(e.value, error.FileReadError(src[1]))

    expected_events = [event.EventFileRead(src[0])]
    assert el.verify_history(expected_events)


def test_concat_error_encrypt_file():
    el = TestEventListener()

    src = [r'test\rsc\a.pdf', r'test\rsc\encrypted.pdf',
           r'test\rsc\b.pdf']
    dst = r'test\rsc\z.pdf'

    with pytest.raises(error.ConcatEncryptedError) as e:
        app_service.concat_pdf(src, dst)

    assert verify_error(e.value, error.ConcatEncryptedError(src[1]))

    expected_events = [event.EventFileRead(src[0]),
                       event.EventFileRead(src[1])]
    assert el.verify_history(expected_events)


def test_concat_no_source():
    el = TestEventListener()
    src = []
    dst = r'test\rsc\z.pdf'

    with pytest.raises(error.InputFileNotSpecified) as e:
        app_service.concat_pdf(src, dst)

    assert verify_error(e.value, error.InputFileNotSpecified())

    expected_events = []
    assert el.verify_history(expected_events)


def test_concat_no_output():
    el = TestEventListener()
    src = [r'test\rsc\a.pdf', r'test\rsc\b.pdf']
    dst = ''

    with pytest.raises(error.OutputFileNotSpccified) as e:
        app_service.concat_pdf(src, dst)

    assert verify_error(e.value, error.OutputFileNotSpccified())

    expected_events = []
    assert el.verify_history(expected_events)


def test_concat_no_pdf():
    el = TestEventListener()
    src = [r'test\rsc\non-pdf.pdf']
    dst = r'test\rsc\z.pdf'

    with pytest.raises(error.NotPDFFileError) as e:
        app_service.concat_pdf(src, dst)

    assert verify_error(e.value, error.NotPDFFileError(src[0]))

    expected_events = []
    assert el.verify_history(expected_events)
