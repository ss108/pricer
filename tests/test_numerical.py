import pytest
from utils import to_number

@pytest.mark.parametrize("string_repr","expected",[
    ("$56", 56.0),
    ("$6", 6.0),
    ("$76.45", 76.45)
])
def test_to_number(string_repr, expected):
    assert to_number(string_repr) == expected
