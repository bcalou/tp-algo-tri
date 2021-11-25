import random
import time
from plot import plot_graph

entries = []
time_per_entry = []

# Generates the table, sorts it, and mesure time with several data sizes
for i in range(1, 11):
    number_of_entries = 1000 * i
    table = [random.randint(0, 10000) for i in range(number_of_entries)]
    start: float = time.time()
    table.sort()
    end: float = time.time()
    time_elpased = end - start
    entries.append(number_of_entries)
    time_per_entry.append(time_elpased)
    print(str(number_of_entries) + " entries sorted.")

# Print the previous results
plot_graph(entries, time_per_entry, "sort.png")