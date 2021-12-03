import time
import random


start: float = time.time()
array = [random.randint(0, 100) for i in range(1_000_000)]
end: float = time.time()
print("Temps écoulé pour créer un tableau a 1_000_000 entrées :", end - start)

start: float = time.time()
array = [random.randint(0, 100) for i in range(2_000_000)]
end: float = time.time()
print("Temps écoulé pour créer un tableau a 2_000_000 entrées :", end - start)

start: float = time.time()
array = [random.randint(0, 100) for i in range(3_000_000)]
end: float = time.time()
print("Temps écoulé pour créer un tableau a 3_000_000 entrées :", end - start)

start: float = time.time()
array = [random.randint(0, 100) for i in range(4_000_000)]
end: float = time.time()
print("Temps écoulé pour créer un tableau a 4_000_000 entrées :", end - start)

start: float = time.time()
array = [random.randint(0, 100) for i in range(5_000_000)]
end: float = time.time()
print("Temps écoulé pour créer un tableau a 5_000_000 entrées :", end - start)

start: float = time.time()
array = [random.randint(0, 100) for i in range(6_000_000)]
end: float = time.time()
print("Temps écoulé pour créer un tableau a 6_000_000 entrées :", end - start)

start: float = time.time()
array = [random.randint(0, 100) for i in range(7_000_000)]
end: float = time.time()
print("Temps écoulé pour créer un tableau a 7_000_000 entrées :", end - start)

start: float = time.time()
array = [random.randint(0, 100) for i in range(8_000_000)]
end: float = time.time()
print("Temps écoulé pour créer un tableau a 8_000_000 entrées :", end - start)

start: float = time.time()
array = [random.randint(0, 100) for i in range(9_000_000)]
end: float = time.time()
print("Temps écoulé pour créer un tableau a 9_000_000 entrées :", end - start)

start: float = time.time()
array = [random.randint(0, 100) for i in range(10_000_000)]
end: float = time.time()
print("Temps écoulé pour créer un tableau a 10_000_000 entrées :", end - start)
