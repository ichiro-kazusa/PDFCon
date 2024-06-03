import sys
import os
import wx
from .frames.mainframe import MainFrame


def icon_path(filename):
    dirname = os.path.dirname(sys.argv[0])
    return os.path.join(os.path.abspath(dirname), filename)


class MainApp:
    def __init__(self, title: str):
        self.app = wx.App()

        frame = MainFrame(None)
        frame.SetTitle(title)

        frame.SetIcon(wx.Icon(icon_path('appicon.ico')))
        frame.Show()

    def start_main_loop(self):

        self.app.MainLoop()
