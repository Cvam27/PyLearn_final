def tLoop():
    num = int(input("Enter a number : "))

    if num > 35:
        print("You are passed")
    else:
        print("You are failed")

    ask = str(input("Repeat?"))

    while ask == "1":
        tLoop()
    else:
        exit()

tLoop()