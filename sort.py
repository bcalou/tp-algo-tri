import random
import time

tableau: list[int] = [random.randint(0, 100) for _ in range(1000)]
start: float = time.time()
tableau.sort()
end: float = time.time()
print("Temps écoulé pour 1 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(5000)]
start: float = time.time()
tableau.sort()
end: float = time.time()
print("Temps écoulé pour 5 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(10_000)]
start: float = time.time()
tableau.sort()
end: float = time.time()
print("Temps écoulé pour 10 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(20_000)]
start: float = time.time()
tableau.sort()
end: float = time.time()
print("Temps écoulé pour 20 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(50_000)]
start: float = time.time()
tableau.sort()
end: float = time.time()
print("Temps écoulé pour 50 000 entrées:", end - start)