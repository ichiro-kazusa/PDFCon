import wx
from src.pdf.appsvc import PDFAppSevice
from src.pdf.event import event, error
from src.pdf.repo.pdfrepo import PikePDFRepository


from ..error.error import SelectionNotContinuousException
from .droptarget import ListFileDropTarget, PickerFileDropTarget
from .myframe import MyFrame
from .wxlistutil import wxListUtil


class GUILogger():
    """String logger echoes strings to wxTextCtrl."""

    def __init__(self, textctrl: wx.TextCtrl) -> None:
        self.__textctrl = textctrl

    def log(self, log: str) -> None:
        self.__textctrl.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        self.__textctrl.AppendText(log + '\n')

    def err(self, err: str) -> None:
        self.__textctrl.SetDefaultStyle(wx.TextAttr(wx.RED))
        self.__textctrl.AppendText(err + '\n')


class GUIEventListener(event.BaseEventListener):
    def __init__(self, logger: GUILogger):
        super().__init__()
        self.__logger = logger

    def update(self, event_: event.PDFEvent):
        if isinstance(event_, event.EventFileRead):
            self.__logger.log(f'opened {event_.path}.')
        elif isinstance(event_, event.EventFileWrite):
            self.__logger.log(f'writing into {event_.path}')
        elif isinstance(event_, event.EventConcatComplete):
            self.__logger.log('concat completed.')
        elif isinstance(event_, event.EventDecryptComplete):
            self.__logger.log('decrypt completed.')
        elif isinstance(event_, event.EventEncryptComplete):
            self.__logger.log('encrypt completed.')
        else:
            self.__logger.log('unknown event.')


class GUiErrorHandler():
    def __init__(self, logger: GUILogger) -> None:
        self.__logger = logger

    def handle(self, error_: error.PDFError):
        if isinstance(error_, error.FileReadError):
            self.__logger.err(f'failed to open {error_.path}')
        elif isinstance(error_, error.NotPDFFileError):
            self.__logger.err(f'not seems to be a pdf file {error_.path}')
        elif isinstance(error_, error.InputFileNotSpecified):
            self.__logger.err('source file is not specified.')
        elif isinstance(error_, error.OutputFileNotSpccified):
            self.__logger.err('destination file is not specified.')
        elif isinstance(error_, error.ConcatEncryptedError):
            self.__logger.err(f'could not concat encrypted file {error_.path}')
        elif isinstance(error_, error.DecryptUnencryptedError):
            self.__logger.err('file is not encrypted.')
        elif isinstance(error_, error.DecryptPasswordFail):
            self.__logger.err('password failed.')
        else:
            self.__logger.err('unknown error.')


class MainFrame(MyFrame):

    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)

        # ## drag and drop settings
        # concat source list
        concat_droptarget = ListFileDropTarget(self.concat_srclistbox,
                                               ext_filter='.pdf')
        self.concat_srclistbox.SetDropTarget(concat_droptarget)
        # decrypt source picker
        decrypt_droptarget = PickerFileDropTarget(self.decrypt_srcpicker,
                                                  ext_filter='.pdf')
        self.decrypt_srcpicker.SetDropTarget(decrypt_droptarget)
        # encrypt source picker
        encrypt_droptarget = PickerFileDropTarget(self.encrypt_srcpicker,
                                                  ext_filter='.pdf')
        self.encrypt_srcpicker.SetDropTarget(encrypt_droptarget)

        # Prepare loggers
        self.__guilogger = GUILogger(self.log_logtextbox)
        GUIEventListener(self.__guilogger)
        self.__guierrorhandler = GUiErrorHandler(self.__guilogger)

        # Instance of PDF Engine
        pdfrepo = PikePDFRepository()
        self.__pdf_app_service = PDFAppSevice(pdfrepo)

    def concat_click_srcadd(self, _):
        dialog = wx.FileDialog(None, u'Select file(s)',
                               style=wx.FD_OPEN | wx.FD_MULTIPLE)
        dialog.SetWildcard("PDF files (*.pdf)|*.pdf")

        if dialog.ShowModal() == wx.ID_OK:
            files_path = dialog.GetPaths()
            self.concat_srclistbox.AppendItems(files_path)
            dialog.Destroy()

    def concat_clicksrcrmv(self, _):
        wxListUtil.list_delete_selections(self.concat_srclistbox)

    def concat_clicksrcclr(self, _):
        self.concat_srclistbox.Clear()

    def concat_clickmvtop(self, _):
        wxListUtil.list_move_selections(self.concat_srclistbox, 'head')

    def concat_clickmvup(self, _):
        try:
            wxListUtil.list_move_selections(self.concat_srclistbox, -1)
        except SelectionNotContinuousException:
            self.__guilogger.err('selection must be continuous')

    def concat_clickmvdn(self, _):
        try:
            wxListUtil.list_move_selections(self.concat_srclistbox, 1)
        except SelectionNotContinuousException:
            self.__guilogger.err('selection must be continuous')

    def concat_clickmvbtm(self, _):
        wxListUtil.list_move_selections(self.concat_srclistbox, 'tail')

    def concat_clickconcat(self, _):
        sources = self.concat_srclistbox.GetItems()
        destination = self.concat_destpicker.GetPath()
        try:
            self.__pdf_app_service.concat_pdf(sources, destination)
        except error.PDFError as e:
            self.__guierrorhandler.handle(e)

    def decrypt_clickfilldstbtn(self, _):
        source: str = self.decrypt_srcpicker.GetPath()
        if source.endswith('.pdf'):
            dstpath = source[:-4] + '_decrypt.pdf'
            self.decrypt_dstpicker.SetPath(dstpath)

    def decrypt_clickdecryptbtn(self, _):
        source = self.decrypt_srcpicker.GetPath()
        dest = self.decrypt_dstpicker.GetPath()
        password = self.decrypt_passwordtxt.GetValue()
        try:
            self.__pdf_app_service.decrypt_pdf(source, password, dest)
        except error.PDFError as e:
            self.__guierrorhandler.handle(e)

    def encrypt_chkreadpassbox(self, _):
        if self.encrypt_needpasschkbox.IsChecked():
            self.encrypt_passwordtxt_read.Enable(True)
        elif not self.encrypt_needpasschkbox.IsChecked():
            self.encrypt_passwordtxt_read.Enable(False)

    def encrypt_clickfilldstbtn(self, _):
        source: str = self.encrypt_srcpicker.GetPath()
        if source.endswith('.pdf'):
            dstpath = source[:-4] + '_encrypt.pdf'
            self.encrypt_dstpicker.SetPath(dstpath)

    def encrypt_clickencryptbtn(self, _):
        sources = self.encrypt_srcpicker.GetPath()
        destination = self.encrypt_dstpicker.GetPath()
        read_pass = self.encrypt_passwordtxt_read.GetValue()\
            if self.encrypt_needpasschkbox.IsChecked() else ''
        write_pass = self.encrypt_passwordtxt_write.GetValue()
        try:
            self.__pdf_app_service.encrypt_pdf(sources, destination,
                                               write_pass, read_pass)
        except error.PDFError as e:
            self.__guierrorhandler.handle(e)

    def listbox_onchar(self, event: wx.KeyEvent):
        KeyCode = event.GetKeyCode()
        listbox: wx.ListBox = event.GetEventObject()
        # ctrl+A -> select all
        if KeyCode == wx.WXK_CONTROL_A:
            wxListUtil.list_select_all(listbox)
        # del -> delete selections
        elif KeyCode == wx.WXK_DELETE:
            self.concat_clicksrcrmv(None)
        # alt+up -> move up
        elif KeyCode == wx.WXK_UP and event.AltDown():
            self.concat_clickmvup(None)
        # alt+down -> move down
        elif KeyCode == wx.WXK_DOWN and event.AltDown():
            self.concat_clickmvdn(None)
        # alt+home -> move top
        elif KeyCode == wx.WXK_HOME and event.AltDown():
            self.concat_clickmvtop(None)
        # alt+end -> move bottom
        elif KeyCode == wx.WXK_END and event.AltDown():
            self.concat_clickmvbtm(None)
        event.Skip()
