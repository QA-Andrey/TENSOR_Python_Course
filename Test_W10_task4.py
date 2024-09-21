import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


class TestMy:

    def test_1(self, start_end_time):
        assert all_division(3, 3, 6, 11) == 0.01515151515151515

    @pytest.mark.smoke
    def test_division_by_zero(self, start_end_time):
        with pytest.raises(ZeroDivisionError):
            all_division(2, 0, 4)


    def test_str(self, start_end_time):
        with pytest.raises(TypeError):
            all_division('4', 8, 20)


    def test_long_num(self, start_end_time, test_exec_time):
        assert all_division(123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890) == 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890


    def test_many_numbers(self, start_end_time):
        assert all_division(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27) == 9.183689863795547e-29