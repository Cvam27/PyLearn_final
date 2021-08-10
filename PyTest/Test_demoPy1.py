import pytest

@pytest.mark.compare
def test_p1():
    a=3
    b=4
    assert a+1 == b, "Failed"

def test_p2():
    assert True

@pytest.mark.compare
def test_p3():
    assert False, "Failed as intention"

@pytest.mark.compare
def test_p4():
    assert "selenium".upper() == "SELENIUM"