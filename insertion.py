import random
import time

number_entry : int = 10000
array : list = [random.randint(0, number_entry) for i in range(number_entry)]

start: float = time.time()

for i in range(len(array)) :
    x = array[i]
    j = i
    while j > 0 and array[j - 1] > x :
        #Create an empty place between the numbers until finding the right place
        array[j] = array[j - 1]
        j = j - 1
    #Placing the sorted number into the empty space
    array[j] = x
        
end: float = time.time()
print("Temps écoulé :", end - start)