import random
import time
from plot import plot_graph

# Sort a table by merging
# Complexity seems to be o(n*log(n))
def merge_sort(table: list[int]):
    if len(table) > 1:
        # Determines the center index of the table
        middle = len(table) // 2
        # Gets the first half of the table
        left = table[:middle]
        # Gets the second half of the table
        right = table[middle:]

        # Iterate recursively over each half of the table
        merge_sort(left)
        merge_sort(right)

        # The index of the first half of the table
        l = 0
        # The index of the second half of the table
        r = 0
        # The index of the returned table
        main = 0

        # Compares the first element of each half and add it to the main table
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
              table[main] = left[l]
              l += 1
            else:
                table[main] = right[r]
                r += 1
            main += 1

        # Input the rest of the half table into the returned table if the other half is already empty
        while l < len(left):
            table[main] = left[l]
            l += 1
            main += 1
        while r < len(right):
            table[main]=right[r]
            r += 1
            main += 1
    
    # Each half will be returned sorted, recursively, the full table will be sorted
    return table

entries = []
time_per_entry = []

# Generates the table, sorts it, and mesure time with several data sizes
for i in range(1, 11):
    number_of_entries = 1000 * i
    table = [random.randint(0, 10000) for i in range(number_of_entries)]
    start: float = time.time()
    merge_sort(table)
    end: float = time.time()
    time_elpased = end - start
    entries.append(number_of_entries)
    time_per_entry.append(time_elpased)
    print(str(number_of_entries) + " entries sorted.")

# Print the previous results
plot_graph(entries, time_per_entry, "fusion.png")