import time
start: float = time.time()
import random
array  = [random.randint(0, 100) for i in range(int('10_000'))]
array.sort()
print(array)

end: float = time.time()
print("Temps écoulé :", end - start)