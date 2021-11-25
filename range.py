import random
import time

start: float = time.time()

#Create a random list with a given number of index
array : list = [random.randint(0, 100) for i in range(10_000_000)]

end: float = time.time()
print("Temps écoulé :", end - start)
