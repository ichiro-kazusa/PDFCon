# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.0-4761b0c)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MyFrame
###########################################################################


class MyFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            600, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(-1, 600), wx.DefaultSize)
        self.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        main_sizer = wx.FlexGridSizer(2, 1, 0, 0)
        main_sizer.AddGrowableCol(0)
        main_sizer.AddGrowableRow(0)
        main_sizer.SetFlexibleDirection(wx.BOTH)
        main_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.main_notebook = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.concat_panel = wx.Panel(
            self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        concat_panelsizer = wx.FlexGridSizer(3, 1, 0, 0)
        concat_panelsizer.AddGrowableCol(0)
        concat_panelsizer.AddGrowableRow(0)
        concat_panelsizer.SetFlexibleDirection(wx.BOTH)
        concat_panelsizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        concat_srcsizer = wx.StaticBoxSizer(wx.StaticBox(
            self.concat_panel, wx.ID_ANY, u"source"), wx.VERTICAL)

        concat_srclayoutsizer = wx.FlexGridSizer(1, 2, 0, 0)
        concat_srclayoutsizer.AddGrowableCol(0)
        concat_srclayoutsizer.AddGrowableRow(0)
        concat_srclayoutsizer.SetFlexibleDirection(wx.BOTH)
        concat_srclayoutsizer.SetNonFlexibleGrowMode(
            wx.FLEX_GROWMODE_SPECIFIED)

        concat_srclistboxChoices = []
        self.concat_srclistbox = wx.ListBox(concat_srcsizer.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, concat_srclistboxChoices, wx.LB_EXTENDED | wx.LB_HSCROLL)
        self.concat_srclistbox.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        concat_srclayoutsizer.Add(
            self.concat_srclistbox, 0, wx.ALL | wx.EXPAND, 5)

        concat_srcbtnsizer = wx.BoxSizer(wx.VERTICAL)

        self.concat_srcaddbtn = wx.Button(concat_srcsizer.GetStaticBox(
        ), wx.ID_ANY, u"add", wx.DefaultPosition, wx.DefaultSize, 0)
        concat_srcbtnsizer.Add(self.concat_srcaddbtn, 0, wx.ALL, 5)

        self.concat_srcrmvbtn = wx.Button(concat_srcsizer.GetStaticBox(
        ), wx.ID_ANY, u"remove", wx.DefaultPosition, wx.DefaultSize, 0)
        concat_srcbtnsizer.Add(self.concat_srcrmvbtn, 0, wx.ALL, 5)

        self.concat_srcclrbtn = wx.Button(concat_srcsizer.GetStaticBox(
        ), wx.ID_ANY, u"clear", wx.DefaultPosition, wx.DefaultSize, 0)
        concat_srcbtnsizer.Add(self.concat_srcclrbtn, 0, wx.ALL, 5)

        self.m_staticline1 = wx.StaticLine(concat_srcsizer.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        concat_srcbtnsizer.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.concat_mvtopbtn = wx.Button(concat_srcsizer.GetStaticBox(
        ), wx.ID_ANY, u"top", wx.DefaultPosition, wx.DefaultSize, 0)
        concat_srcbtnsizer.Add(self.concat_mvtopbtn, 0, wx.ALL, 5)

        self.concat_mvupbtn = wx.Button(concat_srcsizer.GetStaticBox(
        ), wx.ID_ANY, u"up", wx.DefaultPosition, wx.DefaultSize, 0)
        concat_srcbtnsizer.Add(self.concat_mvupbtn, 0, wx.ALL, 5)

        self.concat_mvdnbtn = wx.Button(concat_srcsizer.GetStaticBox(
        ), wx.ID_ANY, u"down", wx.DefaultPosition, wx.DefaultSize, 0)
        concat_srcbtnsizer.Add(self.concat_mvdnbtn, 0, wx.ALL, 5)

        self.concat_mvbtmbtn = wx.Button(concat_srcsizer.GetStaticBox(
        ), wx.ID_ANY, u"bottom", wx.DefaultPosition, wx.DefaultSize, 0)
        concat_srcbtnsizer.Add(self.concat_mvbtmbtn, 0, wx.ALL, 5)

        concat_srclayoutsizer.Add(concat_srcbtnsizer, 1, wx.EXPAND, 5)

        concat_srcsizer.Add(concat_srclayoutsizer, 1, wx.EXPAND, 5)

        concat_panelsizer.Add(concat_srcsizer, 1, wx.EXPAND, 5)

        concat_dstsizer = wx.StaticBoxSizer(wx.StaticBox(
            self.concat_panel, wx.ID_ANY, u"destination"), wx.VERTICAL)

        concat_dstlayoutsizer = wx.FlexGridSizer(1, 3, 0, 0)
        concat_dstlayoutsizer.AddGrowableCol(0)
        concat_dstlayoutsizer.SetFlexibleDirection(wx.BOTH)
        concat_dstlayoutsizer.SetNonFlexibleGrowMode(
            wx.FLEX_GROWMODE_SPECIFIED)

        self.concat_destpicker = wx.FilePickerCtrl(concat_dstsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file",
                                                   u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT | wx.FLP_SAVE | wx.FLP_SMALL | wx.FLP_USE_TEXTCTRL)
        concat_dstlayoutsizer.Add(
            self.concat_destpicker, 0, wx.ALL | wx.EXPAND, 5)

        concat_dstsizer.Add(concat_dstlayoutsizer, 1, wx.EXPAND, 5)

        self.concat_concatbutton = wx.Button(concat_dstsizer.GetStaticBox(
        ), wx.ID_ANY, u"concat", wx.DefaultPosition, wx.DefaultSize, 0)
        concat_dstsizer.Add(self.concat_concatbutton, 0,
                            wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        concat_panelsizer.Add(concat_dstsizer, 1, wx.EXPAND, 5)

        self.concat_panel.SetSizer(concat_panelsizer)
        self.concat_panel.Layout()
        concat_panelsizer.Fit(self.concat_panel)
        self.main_notebook.AddPage(self.concat_panel, u"concat", False)
        self.encrypt_panel = wx.Panel(
            self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        encrypt_panelsizer = wx.FlexGridSizer(2, 1, 0, 0)
        encrypt_panelsizer.AddGrowableCol(0)
        encrypt_panelsizer.SetFlexibleDirection(wx.BOTH)
        encrypt_panelsizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        encrypt_srcsizer = wx.StaticBoxSizer(wx.StaticBox(
            self.encrypt_panel, wx.ID_ANY, u"source"), wx.VERTICAL)

        self.encrypt_srcpicker = wx.FilePickerCtrl(encrypt_srcsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file",
                                                   u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST | wx.FLP_OPEN | wx.FLP_SMALL | wx.FLP_USE_TEXTCTRL)
        encrypt_srcsizer.Add(self.encrypt_srcpicker, 0, wx.ALL | wx.EXPAND, 5)

        self.encrypt_needpasschkbox = wx.CheckBox(encrypt_srcsizer.GetStaticBox(
        ), wx.ID_ANY, u"needs password to read", wx.DefaultPosition, wx.DefaultSize, 0)
        encrypt_srcsizer.Add(self.encrypt_needpasschkbox, 0, wx.ALL, 5)

        fgSizer15 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer15.SetFlexibleDirection(wx.BOTH)
        fgSizer15.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText4 = wx.StaticText(encrypt_srcsizer.GetStaticBox(
        ), wx.ID_ANY, u"read password:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        fgSizer15.Add(self.m_staticText4, 0,
                      wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.encrypt_passwordtxt_read = wx.TextCtrl(encrypt_srcsizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), wx.TE_PASSWORD)
        self.encrypt_passwordtxt_read.Enable(False)

        fgSizer15.Add(self.encrypt_passwordtxt_read, 0,
                      wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        encrypt_srcsizer.Add(fgSizer15, 1, wx.EXPAND, 5)

        encrypt_panelsizer.Add(encrypt_srcsizer, 1, wx.EXPAND, 5)

        encrypt_dstsizer = wx.StaticBoxSizer(wx.StaticBox(
            self.encrypt_panel, wx.ID_ANY, u"destination"), wx.VERTICAL)

        fgSizer61 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer61.AddGrowableCol(0)
        fgSizer61.SetFlexibleDirection(wx.BOTH)
        fgSizer61.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.encrypt_dstpicker = wx.FilePickerCtrl(encrypt_dstsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file",
                                                   u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT | wx.FLP_SAVE | wx.FLP_SMALL | wx.FLP_USE_TEXTCTRL)
        fgSizer61.Add(self.encrypt_dstpicker, 0, wx.ALL | wx.EXPAND, 5)

        self.encrypt_filldstbtn = wx.Button(encrypt_dstsizer.GetStaticBox(
        ), wx.ID_ANY, u"auto fill", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer61.Add(self.encrypt_filldstbtn, 0, wx.ALL, 5)

        encrypt_dstsizer.Add(fgSizer61, 1, wx.EXPAND, 5)

        fgSizer17 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText41 = wx.StaticText(encrypt_dstsizer.GetStaticBox(
        ), wx.ID_ANY, u"encryption password:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText41.Wrap(-1)

        fgSizer17.Add(self.m_staticText41, 0,
                      wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.encrypt_passwordtxt_write = wx.TextCtrl(encrypt_dstsizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), wx.TE_PASSWORD)
        fgSizer17.Add(self.encrypt_passwordtxt_write, 0, wx.ALL, 5)

        encrypt_dstsizer.Add(fgSizer17, 1, wx.EXPAND, 5)

        self.encrypt_encryptbtn = wx.Button(encrypt_dstsizer.GetStaticBox(
        ), wx.ID_ANY, u"encrypt", wx.DefaultPosition, wx.DefaultSize, 0)
        encrypt_dstsizer.Add(self.encrypt_encryptbtn, 0,
                             wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        encrypt_panelsizer.Add(encrypt_dstsizer, 1, wx.EXPAND, 5)

        self.encrypt_panel.SetSizer(encrypt_panelsizer)
        self.encrypt_panel.Layout()
        encrypt_panelsizer.Fit(self.encrypt_panel)
        self.main_notebook.AddPage(self.encrypt_panel, u"encrypt", False)
        self.decrypt_panel = wx.Panel(
            self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        decrypt_panelsizer = wx.FlexGridSizer(2, 1, 0, 0)
        decrypt_panelsizer.AddGrowableCol(0)
        decrypt_panelsizer.SetFlexibleDirection(wx.BOTH)
        decrypt_panelsizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        decrypt_srcsizer = wx.StaticBoxSizer(wx.StaticBox(
            self.decrypt_panel, wx.ID_ANY, u"source"), wx.VERTICAL)

        self.decrypt_srcpicker = wx.FilePickerCtrl(decrypt_srcsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file",
                                                   u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST | wx.FLP_OPEN | wx.FLP_SMALL | wx.FLP_USE_TEXTCTRL)
        decrypt_srcsizer.Add(self.decrypt_srcpicker, 0, wx.ALL | wx.EXPAND, 5)

        fgSizer7 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer7.SetFlexibleDirection(wx.BOTH)
        fgSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(decrypt_srcsizer.GetStaticBox(
        ), wx.ID_ANY, u"password: ", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        self.m_staticText1.Wrap(-1)

        fgSizer7.Add(self.m_staticText1, 0,
                     wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.decrypt_passwordtxt = wx.TextCtrl(decrypt_srcsizer.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), wx.TE_PASSWORD)
        fgSizer7.Add(self.decrypt_passwordtxt, 0,
                     wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        decrypt_srcsizer.Add(fgSizer7, 1, wx.EXPAND, 5)

        decrypt_panelsizer.Add(decrypt_srcsizer, 1, wx.EXPAND, 5)

        decrypt_dstsizer = wx.StaticBoxSizer(wx.StaticBox(
            self.decrypt_panel, wx.ID_ANY, u"destination"), wx.VERTICAL)

        fgSizer6 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer6.AddGrowableCol(0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.decrypt_dstpicker = wx.FilePickerCtrl(decrypt_dstsizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file",
                                                   u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT | wx.FLP_SAVE | wx.FLP_SMALL | wx.FLP_USE_TEXTCTRL)
        fgSizer6.Add(self.decrypt_dstpicker, 0, wx.ALL | wx.EXPAND, 5)

        self.decrypt_filldstbtn = wx.Button(decrypt_dstsizer.GetStaticBox(
        ), wx.ID_ANY, u"auto fill", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.decrypt_filldstbtn, 0, wx.ALL, 5)

        decrypt_dstsizer.Add(fgSizer6, 1, wx.EXPAND, 5)

        self.decrypt_decryptbtn = wx.Button(decrypt_dstsizer.GetStaticBox(
        ), wx.ID_ANY, u"decrypt", wx.DefaultPosition, wx.DefaultSize, 0)
        decrypt_dstsizer.Add(self.decrypt_decryptbtn, 0,
                             wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        decrypt_panelsizer.Add(decrypt_dstsizer, 1, wx.EXPAND, 5)

        self.decrypt_panel.SetSizer(decrypt_panelsizer)
        self.decrypt_panel.Layout()
        decrypt_panelsizer.Fit(self.decrypt_panel)
        self.main_notebook.AddPage(self.decrypt_panel, u"decrypt", False)

        main_sizer.Add(self.main_notebook, 1, wx.EXPAND | wx.ALL, 5)

        self.log_panel = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        log_sizer = wx.StaticBoxSizer(wx.StaticBox(
            self.log_panel, wx.ID_ANY, u"log"), wx.VERTICAL)

        self.log_logtextbox = wx.TextCtrl(log_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(
            -1, 150), wx.TE_BESTWRAP | wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        log_sizer.Add(self.log_logtextbox, 0, wx.ALL | wx.EXPAND, 5)

        self.log_panel.SetSizer(log_sizer)
        self.log_panel.Layout()
        log_sizer.Fit(self.log_panel)
        main_sizer.Add(self.log_panel, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.concat_srclistbox.Bind(wx.EVT_CHAR, self.listbox_onchar)
        self.concat_srcaddbtn.Bind(wx.EVT_BUTTON, self.concat_click_srcadd)
        self.concat_srcrmvbtn.Bind(wx.EVT_BUTTON, self.concat_clicksrcrmv)
        self.concat_srcclrbtn.Bind(wx.EVT_BUTTON, self.concat_clicksrcclr)
        self.concat_mvtopbtn.Bind(wx.EVT_BUTTON, self.concat_clickmvtop)
        self.concat_mvupbtn.Bind(wx.EVT_BUTTON, self.concat_clickmvup)
        self.concat_mvdnbtn.Bind(wx.EVT_BUTTON, self.concat_clickmvdn)
        self.concat_mvbtmbtn.Bind(wx.EVT_BUTTON, self.concat_clickmvbtm)
        self.concat_concatbutton.Bind(wx.EVT_BUTTON, self.concat_clickconcat)
        self.encrypt_needpasschkbox.Bind(
            wx.EVT_CHECKBOX, self.encrypt_chkreadpassbox)
        self.encrypt_filldstbtn.Bind(
            wx.EVT_BUTTON, self.encrypt_clickfilldstbtn)
        self.encrypt_encryptbtn.Bind(
            wx.EVT_BUTTON, self.encrypt_clickencryptbtn)
        self.decrypt_filldstbtn.Bind(
            wx.EVT_BUTTON, self.decrypt_clickfilldstbtn)
        self.decrypt_decryptbtn.Bind(
            wx.EVT_BUTTON, self.decrypt_clickdecryptbtn)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def listbox_onchar(self, event):
        event.Skip()

    def concat_click_srcadd(self, event):
        event.Skip()

    def concat_clicksrcrmv(self, event):
        event.Skip()

    def concat_clicksrcclr(self, event):
        event.Skip()

    def concat_clickmvtop(self, event):
        event.Skip()

    def concat_clickmvup(self, event):
        event.Skip()

    def concat_clickmvdn(self, event):
        event.Skip()

    def concat_clickmvbtm(self, event):
        event.Skip()

    def concat_clickconcat(self, event):
        event.Skip()

    def encrypt_chkreadpassbox(self, event):
        event.Skip()

    def encrypt_clickfilldstbtn(self, event):
        event.Skip()

    def encrypt_clickencryptbtn(self, event):
        event.Skip()

    def decrypt_clickfilldstbtn(self, event):
        event.Skip()

    def decrypt_clickdecryptbtn(self, event):
        event.Skip()
