import random

array = [random.randint(0, 100) for i in range(10)]

print(array)

def tri_insertion(t) :
    newArray=t
    for i in range(0, len(t)) :
        initial=newArray[i]
        permut_index=i
        for j in range(i, -1, -1) :
            if (initial < newArray[j]) :
                permut_index=j
        del newArray[i]
        newArray.insert(permut_index, initial)  
    return newArray

print(tri_insertion(array))