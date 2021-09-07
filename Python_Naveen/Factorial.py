def factorial(numb):
    if (numb > 1):
        numb = numb * factorial(numb -1)
    return numb

print(factorial(5))