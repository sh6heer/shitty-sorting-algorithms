"""
runs permutation sort, but on multiple processes
"""
import sys
import numpy as np
import multiprocessing
from itertools import permutations as generate
import shitsort.peripherals as peripherals

def multipermutationsort(arr, numthreads):
    """
    multithreads the permutationthread procedure
    without modifying the passed in array
    """
    processes = []
    permutations = [ x.tolist() for x in np.array_split(list(generate(arr)), numthreads) ]

    queue = multiprocessing.Queue()
    for i in range(numthreads):

        # pass array as tuple because pickles ?? idk
        process = multiprocessing.Process(target=permutationthread, args=(permutations[i],queue))
        process.start()
        processes.append(process)

    # waits for one process to put a result in the queueueue
    result = queue.get()

    # then kills all of them
    # idc how you're meant to do it
    for process in processes:
        process.terminate()
        process.join()

    return result


def permutationthread(arr, queue):
    """
    finds sorted permutation and queueueues it
    without modifying the passed in array
    """
    for permutation in arr:
        if peripherals.check_if_ordered(permutation):
            queue.put(permutation)
