import random
import time




array = [random.randint(0, 100) for i in range(5000)]
start: float = time.time()
sorted(array)
end: float = time.time()
print("Temps écoulé :", end - start)