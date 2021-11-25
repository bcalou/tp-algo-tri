import random

array = [random.randint(0, 100) for i in range(10)]

print(array)

def tri_selection(t) :
    newArray=t
    for i in range(0, len(t)) :
        initial=newArray[i]
        permut=newArray[i]
        permut_index=i
        for j in range(i, len(t)) :
            print(i, j, array[j])
            if (newArray[j] < permut) :
                permut=newArray[j]
                permut_index=j
        newArray[i]=permut
        newArray[permut_index]=initial
    return newArray

print(tri_selection(array))