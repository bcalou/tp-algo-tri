import random
import time


number_entry : int = 10000
array : list = [random.randint(0, number_entry) for i in range(number_entry)]

start: float = time.time()

array.sort()

end: float = time.time()
print("Temps écoulé :", end - start)