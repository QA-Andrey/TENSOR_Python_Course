import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, c, result', [
    pytest.param(2, -3, 4.15, -0.16064257028112447, marks=pytest.mark.smoke),
    pytest.param(140, 14, 2, 5, marks=pytest.mark.skip('Bad params')),
    (0, 2346, -12345.33, 0)],
                         ids=('smoke', 'acceptance', 'First is zero'))
def test(a, b, c, result):
    assert all_division(a, b, c) == result
