from pytest import
def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test Fail"
	assert x != y,"test fail"
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed"
def test_3():
	x=5
	assert x !=7, "failed"


test_file1_method2()
test_file1_method2()
test_3()