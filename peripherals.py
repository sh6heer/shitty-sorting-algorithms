"""peripheral methods that are unrelated to bogosort algorithm"""
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
