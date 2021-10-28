import wx
from src.pdfui.frames.mainframe import MainFrame
from test.test_gui.rsc.guitest_util import MockPDFAppService,\
    MockPDFRepository, EventTestEntries
from ..utilities import TestEventListener

app = wx.App()
frame = MainFrame(None)
frame._MainFrame__pdf_app_service = MockPDFAppService(MockPDFRepository())


def test_concat_btn_normal():
    el = TestEventListener()

    sources = ['a.pdf', 'b.pdf', 'c.pdf']
    dest = 'z.pdf'

    frame.concat_srclistbox.AppendItems(sources)
    frame.concat_destpicker.SetPath(dest)
    frame.concat_clickconcat(None)

    expected_entry = {'pdfsrcpaths': sources,
                      'pdfdst': dest}
    expected_events = [EventTestEntries(expected_entry)]

    assert el.verify_history(expected_events)


