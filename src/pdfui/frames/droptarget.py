import wx


class ListFileDropTarget(wx.FileDropTarget):
    def __init__(self, list: wx.ListBox, ext_filter: str = ''):
        super(ListFileDropTarget, self).__init__()
        self.__list = list
        self.__ext_filter = ext_filter

    def OnDropFiles(self, x, y, filenames: list[str]):
        filtered_filenames = [x for x in filenames
                              if x.endswith(self.__ext_filter)]
        self.__list.AppendItems(filtered_filenames)
        return True


class PickerFileDropTarget(wx.FileDropTarget):
    def __init__(self, picker: wx.FilePickerCtrl, ext_filter: str = ''):
        super(PickerFileDropTarget, self).__init__()
        self.__picker = picker
        self.__ext_filter = ext_filter

    def OnDropFiles(self, x, y, filenames):
        filtered_filenames = [x for x in filenames
                              if x.endswith(self.__ext_filter)]
        if len(filtered_filenames) > 0:
            self.__picker.SetPath(filtered_filenames[0])
        return True
