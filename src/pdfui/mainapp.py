import sys
import os
import wx
from .frames.mainframe import MainFrame


def icon_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath('.'), filename)


class MainApp:
    def __init__(self, title: str):
        self.app = wx.App()

        frame = MainFrame(None)
        frame.SetTitle(title)

        frame.SetIcon(wx.Icon(icon_path('appicon.ico')))
        frame.Show()

    def start_main_loop(self):

        self.app.MainLoop()
