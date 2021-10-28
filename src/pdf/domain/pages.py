import re
from typing import Iterator, Tuple, Union
from functools import reduce

from ..event import error


TPage = Union[int, str]  # type alias


class PageList:
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
    * every number must apperar as ascending order
    * THIS RULE ASSUMED THE PAGE NUMBER STARTS FROM 1
    """

    __block_pattern = re.compile(r'^(\d+|end) *- *(\d+|end)$|^(\d+|end)$')

    def __init__(self, pagesstr: str):

        pageslist = pagesstr.split(',')

        self.__pagelist = []
        for block in pageslist:
            result = self.__parse_block(block)  # raises InvalidPatternError
            self.__pagelist.append(result)

    def __parse_block(self, block: str) -> Tuple[TPage, TPage]:

        def __int_or_end(page: str) -> TPage:
            return 'end' if page == 'end' else int(page)

        block = block.strip()  # delete leading and trailing spaces

        match = self.__block_pattern.match(block)
        if match is None:
            raise error.InvalidPatternError(f'{block}')

        res = match.groups()
        if res[0] is None:
            page = __int_or_end(res[2])
            return (page, page)
        else:
            page0 = __int_or_end(res[0])
            page1 = __int_or_end(res[1])
            return (page0, page1)

    def __verify_order(self):
        """rule: 
        * every int must be ascending order
        * 'end' can appear at the end of list
        """
        # flatten
        flatten = reduce(lambda x, y: list(x)+list(y), self.__pagelist)
        # 'end' does not exist or exist at the end of the list
        if flatten.count('end') > 1 or flatten.index('end') != len(flatten)-1:
            raise Exception()
        # every integer sorted in ascending order
        filtered_flatten = [x for x in flatten if type(x) == int]

    def iter(self) -> Iterator[Tuple[TPage, TPage]]:
        return (e for e in self.__pagelist)
