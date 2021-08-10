import pytest

def test_t1():
    a=2
    b=3
    assert a!=b, "Failed"

def test_t2():
    a="shivam"
    assert a.lower()=="Shivam"