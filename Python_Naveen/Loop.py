# #While Loops
#
# count = 0
# while(count < 5):
#     print("Hello Shivam")
#     count = count +1
#
# print("-----------")
#
# #While-else loop
#
# value=0
# while value < 5:
#     print("This is working")
#     value = value +1
#
# else:
#     print("Now stopped")
#
# print("-----------")
#
# #For Loop
# code = ["ASP", "Python", "Java", "Perl", "Ruby"]
# for i in code:
#     print(i)
#
# print("-------------")
#
# #For loop ffor string
#
# string  = "I love coding"
# for i in string:
#     print(i)
# print("-------------")
#
# # For loop with range

# values = ["This","is","Shivam"]
# for index in range(len(values)):
#     print(values[index])
from operator import index

print("-----------------")
countrylist = ["India", "US", "Japan", "Germany"]
for i in range(len(countrylist)):
    print(countrylist[i])
else:
    print("List is over")