"""runs the classic bogosort algorithm"""

import sys
import peripherals
import bogo_components

def main(args):
    """
    passes in command line arguments if run as main
    """
    length = int(args[0])
    oarray = peripherals.generate_array(length)

    print(bogosort(oarray))


def bogosort(arr):
    """
    returns new bogosorted array
    without modifying passed in one
    """
    result = list(arr)
    is_sorted = False
    while not is_sorted:
        bogo_components.shuffle(result)
        is_sorted = bogo_components.check_if_ordered(result)
    return result

if __name__ == '__main__':
    main(sys.argv[1:])
