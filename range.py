import random
import time

# start: float = time.time()
# tab: list[int] = [random.randint(0, 100) for _ in range(1_000_000)]
# end: float = time.time()
# print("Temps écoulé pour n = 1 000 000:", end - start)

# start: float = time.time()
# tab: list[int] = [random.randint(0, 100) for _ in range(5_000_000)]
# end: float = time.time()
# print("Temps écoulé pour n = 5 000 000:", end - start)

start: float = time.time()
tab: list[int] = [random.randint(0, 100) for _ in range(10_000_000)]
end: float = time.time()
print("Temps écoulé pour n = 10 000 000:", end - start)

# start: float = time.time()
# tab: list[int] = [random.randint(0, 100) for _ in range(20_000_000)]
# end: float = time.time()
# print("Temps écoulé pour n = 20 000 000:", end - start)

# start: float = time.time()
# tab: list[int] = [random.randint(0, 100) for _ in range(40_000_000)]
# end: float = time.time()
# print("Temps écoulé pour n = 40 000 000:", end - start)