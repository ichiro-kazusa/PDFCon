import wx
from typing import Union
from ..error.error import SelectionNotContinuousException


class wxListUtil:
    @staticmethod
    def list_delete_selections(list: wx.ListBox) -> None:
        selections = list.GetSelections()
        for idx in range(len(selections)):
            list.Delete(selections[idx])
            selections = [x-1 for x in selections]  # index shift

    @staticmethod
    def list_select_all(list: wx.ListBox) -> None:
        for idx in range(list.GetCount()):
            list.Select(idx)

    @staticmethod
    def idxs_are_continuous(idxs: list[int]) -> bool:
        """check integer list is sorted and continuous."""
        if len(idxs) <= 1:
            return True  # empty or single array is continuous
        else:
            deltas = [y-x for (x, y) in zip(idxs[:-1], idxs[1:])]
            if(max(deltas) == 1 and min(deltas) == 1):
                return True
            else:
                return False

    @staticmethod
    def list_move_selections(list: wx.ListBox,
                             move_rel: Union[int, str]) -> None:
        """if 'move_to' is number, selections must be continuous
        else if 'move_to' is either 'head' or 'tail',
        selections must not be continuous.
        """
        selections = list.GetSelections()
        if len(selections) == 0:
            return  # abort if nothing selected

        # check 'move_to' and determine insertion index
        if type(move_rel) == int:
            if not wxListUtil.idxs_are_continuous(selections):
                raise SelectionNotContinuousException
            insertion_idx = min(max(selections[0] + move_rel, 0),
                                list.GetCount() - len(selections))
        elif move_rel == 'head':
            insertion_idx = 0
        elif move_rel == 'tail':
            insertion_idx = list.GetCount() - len(selections)
        else:
            return  # abort if 'move_to' is unexpected

        # checkout items and remove selections
        selections_str = []
        for sel in selections:
            selections_str.append(list.GetString(sel))
        wxListUtil.list_delete_selections(list)

        # insert & reselect selections
        list.InsertItems(selections_str, insertion_idx)
        for idx in range(len(selections_str)):
            list.SetSelection(insertion_idx+idx)
