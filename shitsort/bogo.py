"""
classic bogo sort algorithm
"""
import random
from shitsort.peripherals import check_if_ordered

def bogosort(arr):
    """
    returns new bogosorted array
    without modifying passed in one
    """
    result = list(arr)
    is_sorted = False
    while not is_sorted:
        shuffle(result)
        is_sorted = check_if_ordered(result)
    return result

def shuffle(arr):
    """
    modifies passed in array to
    return a random permutation
    """
    for i in range(len(arr)-1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
    bogosort(sys.argv[1])
