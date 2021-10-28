from test.utilities import verify_error

import pytest
from src.pdf.domain.pages import PageList
from src.pdf.event import error


def test_pages_single():
    test1 = '1-3'
    pl1 = PageList(test1)
    assert list(pl1.iter()) == [(1, 3)]

    test2 = '1 - 10'
    pl2 = PageList(test2)
    assert list(pl2.iter()) == [(1, 10)]

    test3 = ' 5  -    end '
    pl3 = PageList(test3)
    assert list(pl3.iter()) == [(5, 'end')]

    test10 = '1 -  3, 5 -  6, 7   ,   10 -13, 20-end'
    pl10 = PageList(test10)
    assert list(pl10.iter()) == [(1, 3), (5, 6), (7, 7), (10, 13), (20, 'end')]


def test_page_error():
    # minus page number
    test1 = '-1-end'
    with pytest.raises(error.InvalidPatternError) as e:
        PageList(test1)
    assert verify_error(e.value, error.InvalidPatternError())

    # invalid charadters
    test2 = 'a-6'
    with pytest.raises(error.InvalidPatternError) as e:
        PageList(test2)
    assert verify_error(e.value, error.InvalidPatternError())
