from leapyear import is_leap_year
import pytest

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (1980, True),
                             (2022, False),
                             (2020, True),
                             (1999, False),
                             (2011, False),
                             (1996, True),
                             (2016, True)
                         ]
                         )
def test_is_leap_year(test_input, expected_output):
    result = is_leap_year(test_input)
    assert result == expected_output