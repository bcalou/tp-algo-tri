# compute factorial of the number
def facto(num):
    return 1 if num == 1 or num == 0 else num * facto(num-1)
print (facto(9))