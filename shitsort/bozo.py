"""Runs the bozo sorting algorithm, which swaps elements randomly"""

import random
from shitsort.bogo import check_if_ordered

def bozosort(arr):
    """
    returns new bozosorted array
    without modifying passed in one
    """
    result = list(arr)
    is_sorted = False
    while not is_sorted:
        switch_random(result)
        is_sorted = check_if_ordered(result)
    return result

def switch_random(arr):
    """
    takes in an array and randomly switches two elements inside it
    """
    index_1 = random.randint(0, len(arr)-1)
    index_2 = index_1
    while index_2 == index_1:
        index_2 = random.randint(0, len(arr)-1)
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
