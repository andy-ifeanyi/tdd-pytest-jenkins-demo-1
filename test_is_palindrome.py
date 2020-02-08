from palindrome import is_palindrome
import pytest

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             ("ciVic", True),
                             ("true", False),
                             ("madam", True),
                             ("renegade", False),
                             ("Guava", False),
                             ("tattat", True),
                             ("02022020", True)
                         ]
                         )
def test_is_palindrome(test_input, expected_output):
    result = is_palindrome(test_input)
    assert result == expected_output