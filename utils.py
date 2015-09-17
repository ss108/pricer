def to_number(dollar_repr):
    return float(dollar_repr.strip('$'))

def test_to_number():
    s = "$56"
    r = to_number(s)
    assert r == 56.0

    s = "$6"
    r = to_number(s)
    assert r == 6

    s = "$76.45"
    r = to_number(s)
    assert r == 76.45

test_to_number()
