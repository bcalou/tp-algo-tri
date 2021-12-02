import random
import time

# Start the timer
start: float = time.time()

# Generate a big array of random numbers
array = [random.randint(0, 100) for i in range(1_000_000)]

# Stop the timer
end: float = time.time()

# Show the ellapsed time
print("Temps écoulé :", end - start)
