import time
import range
import selection
import insertion
import fusion

def tris(list_size: int):
    print("--------------------------------------")
    print("Sorting list of", list_size, "elements")
    print("--------------------------------------")

    start: float = time.time()
    array: list[int] = range.create_list(list_size)
    end: float = time.time()

    print("Create List \t- " + '%.2f' % (end - start) + "s")

    selection_array: list[int] = array[:]
    start = time.time()
    selection.sort(selection_array)
    end = time.time()

    print("Selection sort \t- " + '%.2f' % (end - start) + "s")

    insertion_array: list[int] = array[:]
    start = time.time()
    insertion.sort(insertion_array)
    end = time.time()

    print("Insertion sort \t- " + '%.2f' % (end - start) + "s")

    fusion_array: list[int] = array[:]
    start = time.time()
    fusion.sort(fusion_array)
    end = time.time()

    print("Merge sort \t- " + '%.2f' % (end - start) + "s")

    python_array: list[int] = array[:]
    start = time.time()
    python_array.sort()
    end = time.time()

    print("Python sort \t- " + '%.2f' % (end - start) + "s")

tris(1000)
tris(3000)
tris(5000)
tris(10000)
tris(15000)