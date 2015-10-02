import pytest
from utils import to_number, average

@pytest.mark.parametrize("string,expected",[
    ("$56", 56.0),
    ("$6", 6.0),
    ("$76.45", 76.45)
])
def test_to_number(string, expected):
    assert to_number(string) == expected

@pytest.mark.parametrize("array,expected",[
    ([6.7, 4, 2, 0], 3.2)
])
def test_average(array, expected):
    assert average(array) == expected 
    
