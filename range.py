import time
start: float = time.time()
import random
array  = [random.randint(0, 100) for i in range(int('9_000_000'))]
print(array)

end: float = time.time()
print("Temps écoulé :", end - start)