import re
from typing import Iterator, Tuple, Union, List
# from functools import reduce

from ..event import error


TPage = Union[int, str]  # type alias


class PageListWithEnd:
    """value object to store page information.
    it can contain number, '-', 'end', space.
    example) 1, 4-6, 7-end """

    """ page string rule
    * each group separated with comma.
    * each group is consisted by <number>, <number>-<number>
    * 'end' is regarded as number.
    * space separation for each character is allowed.
    * space separation in number is not allowed
      (these are NG) 42 -> 4 2, end -> e nd
    * THIS RULE ASSUMED THE PAGE NUMBER STARTS FROM 1
     """

    def __init__(self, pagelist: List[Tuple[TPage, TPage]]):
        self.__pagelist = pagelist
        self.__verify_pagelistrule()

    def __verify_pagelistrule(self):
        """checks page string rule
        * pagelist is a list of 2-elements tuple of {int or 'end'}
        * int must be > 0
        """
        if type(self.__pagelist) != list:
            raise error.InvalidPageList()
        for pair in self.__pagelist:
            if type(pair) != tuple or len(pair) != 2:
                raise error.InvalidPageList()
            for elem in pair:
                if type(elem) == int and not elem > 0:
                    raise error.InvalidPageList()
                if type(elem) != int and elem != 'end':
                    raise error.InvalidPageList()

    def iter(self) -> Iterator[Tuple[TPage, TPage]]:
        return (e for e in self.__pagelist)

    @staticmethod
    def __parse_block(block: str) -> Tuple[TPage, TPage]:

        __block_pattern = re.compile(r'^(\d+|end) *- *(\d+|end)$|^(\d+|end)$')

        def __int_or_end(page: str) -> TPage:
            return 'end' if page == 'end' else int(page)

        block = block.strip()  # delete leading and trailing spaces

        match = __block_pattern.match(block)
        if match is None:
            raise error.InvalidPageList(f'{block}')

        res = match.groups()
        if res[0] is None:
            page = __int_or_end(res[2])
            return (page, page)
        else:
            page0 = __int_or_end(res[0])
            page1 = __int_or_end(res[1])
            return (page0, page1)

    @staticmethod
    def create_pagelist_from_str(pagestring: str) -> 'PageListWithEnd':
        pagestrlist = pagestring.split(',')

        pagelist = []
        for block in pagestrlist:
            result = PageListWithEnd.__parse_block(
                block)  # raises InvalidPageString
            pagelist.append(result)

        return PageListWithEnd(pagelist)


class PageList:
    """PageList without 'end'"""

    def __init__(self, pagelistwithend: PageListWithEnd,
                 maxpagenum: int) -> None:
        self.__maxpagenum = maxpagenum
        self.__pagelist = self.__replace_end_with_maxpage(pagelistwithend,
                                                          maxpagenum)
        self.__check_pagenum_outofrange()

    def iter(self):
        return (e for e in self.__pagelist)

    def as_list(self) -> List[int]:
        ret: List[int] = []
        for pairs in self.__pagelist:
            (x, y) = pairs
            if x <= y:  # normal order
                ret += list(range(x, y+1))
            if x > y:  # reversed order
                ret += list(range(x, y-1, -1))
        return ret

    def as_zero_based_list(self):
        # note that 'as_list' starts from 1
        list_1start = self.as_list()
        return [x-1 for x in list_1start]

    def __replace_end_with_maxpage(self, pagelist: PageListWithEnd,
                                   maxpagenum: int) -> List[Tuple[int, int]]:
        replaced: List[Tuple[int, int]] = []
        for (x, y) in pagelist.iter():
            if type(x) == str and x == 'end':
                x_ = maxpagenum
            elif type(x) == int:
                x_ = x
            if type(y) == str and y == 'end':
                y_ = maxpagenum
            elif type(y) == int:
                y_ = y
            replaced.append((x_, y_))

        return replaced

    def __check_pagenum_outofrange(self) -> None:
        for pair in self.__pagelist:
            for elem in pair:
                if type(elem) == int and elem > self.__maxpagenum:
                    raise error.PageIndexOutOfRange()
