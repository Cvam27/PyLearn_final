import pytest
def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test Fail"
	assert x != y,"test fail"
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed"