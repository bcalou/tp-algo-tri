import time
import random


start: float = time.time()
array = [random.randint(0, 100) for i in range(10_000_000)]
end: float = time.time()
print("Temps écoulé :", end - start)
