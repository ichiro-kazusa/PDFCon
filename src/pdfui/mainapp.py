# import sys
import wx
from .frames.mainframe import MainFrame


class MainApp:
    def __init__(self, title: str):
        self.app = wx.App()

        frame = MainFrame(None)
        frame.SetTitle(title)
        frame.SetIcon(wx.Icon('rsc/appicon.ico'))
        frame.Show()

    def start_main_loop(self):

        self.app.MainLoop()
