def demoFunction():
    print("This is simple function without parameter")

demoFunction()

def permFunction(a):
    print(a+10)

permFunction(20)

#Optional Parameter

def getCountryName(name="India"):
    print(name)

getCountryName()
getCountryName("US")

#Function with return

def funcWIthReturn(a,b):
    c = a + b
    return c

s1 =funcWIthReturn(10,20)
print("Returned value = " , s1)

number = 5
def factorial():
    newval = number -1
    return number
    

