from test.utilities import verify_error

import pytest
from src.pdf.domain.pages import PageListWithEnd, PageList
from src.pdf.event import error


def test_pages_single():
    test1 = '1-3'
    pl1 = PageListWithEnd.create_pagelist_from_str(test1)
    assert list(pl1.iter()) == [(1, 3)]

    test2 = '1 - 10'
    pl2 = PageListWithEnd.create_pagelist_from_str(test2)
    assert list(pl2.iter()) == [(1, 10)]

    test3 = ' 5  -    end '
    pl3 = PageListWithEnd.create_pagelist_from_str(test3)
    assert list(pl3.iter()) == [(5, 'end')]

    test10 = '1 -  3, 5 -  6, 7   ,   10 -13, 20-end'
    pl10 = PageListWithEnd.create_pagelist_from_str(test10)
    assert list(pl10.iter()) == [(1, 3), (5, 6), (7, 7), (10, 13), (20, 'end')]

    test11 = '10'
    pl11 = PageListWithEnd.create_pagelist_from_str(test11)
    assert list(pl11.iter()) == [(10, 10)]

    test12 = '10-10'
    pl12 = PageListWithEnd.create_pagelist_from_str(test12)
    assert list(pl12.iter()) == [(10, 10)]


def test_page_invalidpagelist():
    # zero page number
    test1 = '0-end'
    with pytest.raises(error.InvalidPageList) as e:
        PageListWithEnd.create_pagelist_from_str(test1)
    assert verify_error(e.value, error.InvalidPageList())

    # minus page number
    test1 = '-1-end'
    with pytest.raises(error.InvalidPageList) as e:
        PageListWithEnd.create_pagelist_from_str(test1)
    assert verify_error(e.value, error.InvalidPageList())

    # invalid charadters
    test2 = 'a-6'
    with pytest.raises(error.InvalidPageList) as e:
        PageListWithEnd.create_pagelist_from_str(test2)
    assert verify_error(e.value, error.InvalidPageList())


def test_page_normal():
    pagestring = '4-1'
    maxpagenum = 4
    pagelist = PageListWithEnd.create_pagelist_from_str(pagestring)
    pagelist_woend = PageList(pagelist, maxpagenum)

    assert pagelist_woend.as_list() == [4, 3, 2, 1]
    assert pagelist_woend.as_zero_based_list() == [3, 2, 1, 0]


def test_page_normal_withend():
    pagestring = 'end-2, 4-end'
    maxpagenum = 5
    pagelist = PageListWithEnd.create_pagelist_from_str(pagestring)
    pagelist_woend = PageList(pagelist, maxpagenum)

    assert pagelist_woend.as_list() == [5, 4, 3, 2, 4, 5]
    assert pagelist_woend.as_zero_based_list() == [4, 3, 2, 1, 3, 4]


def test_page_indexoutofrange():
    pagestring = '2-6'
    maxpagenum = 5
    pagelist = PageListWithEnd.create_pagelist_from_str(pagestring)

    with pytest.raises(error.PageIndexOutOfRange) as e:
        _ = PageList(pagelist, maxpagenum)

    assert verify_error(e.value, error.PageIndexOutOfRange())


def test_page_indexoutofrange_withend():
    pagestring = '7-end'
    maxpagenum = 5
    pagelist = PageListWithEnd.create_pagelist_from_str(pagestring)

    with pytest.raises(error.PageIndexOutOfRange) as e:
        _ = PageList(pagelist, maxpagenum)

    assert verify_error(e.value, error.PageIndexOutOfRange())
