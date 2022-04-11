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
    print(bogo_components.sort_array(oarray))

if __name__ == '__main__':
    main(sys.argv[1:])
