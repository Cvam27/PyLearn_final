def two_input():
    a, b = input("Enter number of Boys and Girls separated with a space : ").split()
    print("Number of boys: " + a)
    print("Number of girs: " + b)

def three_input():
    a, b, c = input("Enter number of Boys, Girls and kids separated with a space : ").split()
    print("Number of boys: " + a)
    print("Number of girs: " + b)
    print("Number of kids: " + c)

def two_inp_at_same_time():
    a, b = input("Enter number of Boys and Girls separated with a space : ").split()
    print("Boys are {} and Girls are {}".format(a,b))



def main():
    #two_input()
    #three_input()
    two_inp_at_same_time()

if __name__ == '__main__':
    main()




