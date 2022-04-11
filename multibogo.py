import sys
import peripherals
import bogo_components
import multiprocessing

def main(args):
    length = int(args[0])
    numthreads = int(args[1])
    oarray = peripherals.generate_array(length)

    print(multibogo(oarray, numthreads))


# multithreads the bogosort procedure
# without modifying the passed in array
def multibogo(arr, numthreads):
    processes = []

    q = multiprocessing.Queue()
    for n in range(numthreads):

        # pass array as tuple because pickles ?? idk
        p = multiprocessing.Process(target=bogosort, args=(arr,q))
        p.start()
        processes.append(p)

    # waits for one process to put a result in the queue
    result = q.get()

    # then kills all of them
    # idc how you're meant to do it
    for p in processes:
        p.terminate()
        p.join()

    return result


# """sorts""" array and queues it
# without modifying the passed in array
def bogosort(arr, q):
    result = [ x for x in arr ]
    is_sorted = False

    while not is_sorted:
        bogo_components.shuffle(result)
        is_sorted = bogo_components.check_if_ordered(result)
    # place result in queue when it is found
    q.put(result)


if __name__ == '__main__':
    main(sys.argv[1:])
    # length of array, number of threads
