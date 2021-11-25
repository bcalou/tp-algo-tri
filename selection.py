import random
import time

number_entry : int = 9000
array : list = [random.randint(0, number_entry) for i in range(number_entry)]

start: float = time.time()


for j in range(len(array)) :
    #min memorise the index/ the n(th) time we are fetching through the list until the end of the list
    min : int = j
    for i in range(len(array)) :
        #Comparing each number of the index i to the index min
        if array[i] >= array[min] :
            #the index min become the index of the inferiorest number (index i)
            min = i
        #If the inferiorest number with the index min isn't already at the right place (index j which is the n(th) number after those already sorted):
        if min != j :
            #Swap the two index to sort them
            array[j], array[min] = array[min], array[j]
            
end: float = time.time()
print("Temps écoulé :", end - start)
