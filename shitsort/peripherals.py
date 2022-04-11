"""
methods that are needed everywhere
"""
import random

def generate_array(length):
    """
    modifies passed in array to
    return a random permutation
    """
    result = []
    for _ in range(length):
        result.append(random.randint(0,64))
    return result

def check_if_ordered(arr):
    """
    returns a bool value
    of whether the passed in array is in order or not
    """
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
