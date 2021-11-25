import random
import time

from plot import plot_graph

entries = []
time_per_entry = []

# Get execution time for generating a tab with a number of entries
# The number goes from 2 to 16 777 216
# Complexity is o(n)
for i in range(1, 25):
    number_of_entries = pow(2, i)
    start: float = time.time()
    [random.randint(0, 10000) for i in range(number_of_entries)]
    end: float = time.time()
    time_elpased = end - start
    entries.append(number_of_entries)
    time_per_entry.append(time_elpased)

# Print the previous results
plot_graph(entries, time_per_entry, "range.png")