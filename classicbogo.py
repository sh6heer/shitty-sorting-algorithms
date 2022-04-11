import sys
import peripherals
import bogo_components

def main(args):
    length = int(args[0])
    oarray = peripherals.generate_array(length)

    print(bogosort(oarray))


# returns new bogosorted array
# without modifying passed in one
def bogosort(arr):
    result = [ x for x in arr ]
    is_sorted = False
    while not is_sorted:
        bogo_components.shuffle(result)
        is_sorted = bogo_components.check_if_ordered(result)
    return result

if __name__ == '__main__':
    main(sys.argv[1:])
    # length of array
