
from test.utilities import TestEventListener, verify_error

import pytest
from src.pdf.appsvc import PDFAppSevice
from src.pdf.event import error, event
from src.pdf.repo.pdfrepo import PikePDFRepository

repo = PikePDFRepository()
app_service = PDFAppSevice(repo)


def test_decrypt_normal():
    el = TestEventListener()

    src = r'test\rsc\encrypted.pdf'
    passwd = 'password'
    dst = r'test\rsc\decrypted.pdf'

    app_service.decrypt_pdf(src, passwd, dst)

    expected_events = [event.EventFileRead(src),
                       event.EventFileWrite(dst),
                       event.EventDecryptComplete()]
    assert el.verify_history(expected_events)


def test_decrypt_password_fail():
    el = TestEventListener()

    src = r'test\rsc\encrypted.pdf'
    passwd = 'passwd'
    dst = r'test\rsc\decrypted.pdf'

    with pytest.raises(error.DecryptPasswordFail) as e:
        app_service.decrypt_pdf(src, passwd, dst)

    assert verify_error(e.value, error.DecryptPasswordFail())

    expected_events = [event.EventFileRead(src)]
    assert el.verify_history(expected_events)


def test_decrypt_not_encrypted_error():
    el = TestEventListener()

    src = r'test\rsc\a.pdf'
    passwd = 'password'
    dst = r'test\rsc\decrypted.pdf'

    with pytest.raises(error.DecryptUnencryptedError) as e:
        app_service.decrypt_pdf(src, passwd, dst)

    assert verify_error(e.value, error.DecryptUnencryptedError())

    expected_events = [event.EventFileRead(src)]
    assert el.verify_history(expected_events)


def test_decrypt_no_source():
    el = TestEventListener()

    src = ''
    passwd = 'password'
    dst = r'test\rsc\decrypted.pdf'

    with pytest.raises(error.InputFileNotSpecified) as e:
        app_service.decrypt_pdf(src, passwd, dst)

    assert verify_error(e.value, error.InputFileNotSpecified())

    expected_events = []
    assert el.verify_history(expected_events)


def test_decrypt_no_output():
    el = TestEventListener()

    src = r'test\rsc\encrypted.pdf'
    passwd = 'password'
    dst = ''

    with pytest.raises(error.OutputFileNotSpccified) as e:
        app_service.decrypt_pdf(src, passwd, dst)

    assert verify_error(e.value, error.OutputFileNotSpccified())

    expected_events = []
    assert el.verify_history(expected_events)


def test_decrypt_not_pdf_file():
    el = TestEventListener()

    src = r'test\rsc\non-pdf.pdf'
    passwd = 'passwd'
    dst = r'test\rsc\decrypted.pdf'

    with pytest.raises(error.NotPDFFileError) as e:
        app_service.decrypt_pdf(src, passwd, dst)

    assert verify_error(e.value, error.NotPDFFileError(src))

    expected_events = []
    assert el.verify_history(expected_events)
