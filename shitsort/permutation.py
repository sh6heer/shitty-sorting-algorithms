"""
generates ever permutation of an array and cycles through it until
a sorted permutation is found
"""
from itertools import permutations as generate
from shitsort.peripherals import check_if_ordered

def permutationlook(permutations):
    """
    looks each array in a 2D array
    and returns one which is in order
    """
    for permutation in permutations:
        if check_if_ordered(permutation):
            return list(permutation)

def permutationsort(arr):
    """
    generates all permutations and looks through them
    """
    permutations = generate(arr)
    return permutationlook(permutations)
