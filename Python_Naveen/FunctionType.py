# def login(un,pw):
#     print(un,pw)
#
# login("This is un", "and this is pw")
#
# # *arg
# def getmarks(*args):
#     for x in args:
#         print(x)
#
# getmarks("hi", 1212, 224, 567)
#
# #keyword args

def getstudentinfo(**args):
    for key, value in args.items():
        print("%s ==%s" %(key,value))

getstudentinfo(Shivam = 10, Raj = 20, Yash = 30)

#Lambda function = A function w/o any name

cube = lambda x: x+x/x

print(cube(5))
