def fun():
    num = int(input("Enter number:"))
    return  num

def Main():
    print("Begin")
    from_fun = fun()
    print(from_fun)

if __name__ == '__main__':
    Main()


