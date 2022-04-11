"""
runs the bogosort algorithm except multithreaded
"""

import multiprocessing
import shitsort.peripherals
from shitsort.bogo import bogosort

def multibogosort(arr, numthreads):
    """
    multithreads the bogothread procedure
    without modifying the passed in array
    """
    processes = []

    queue = multiprocessing.Queue()
    for _ in range(numthreads):

        # pass array as tuple because pickles ?? idk
        process = multiprocessing.Process(target=bogothread, args=(arr,queue))
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


def bogothread(arr, queue):
    """
    sorts array and queueueues it
    without modifying the passed in array
    """
    result = bogosort(arr)
    queue.put(result) # place result in queueueue when it is found
