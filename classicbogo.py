"""runs the classic bogosort algorithm"""

import sys
import peripherals
from bogo import bogosort

def main(args):
    """
    passes in command line arguments if run as main
    """
    length = int(args[0])
    oarray = peripherals.generate_array(length)
    print(bogosort(oarray))

if __name__ == '__main__':
    main(sys.argv[1:])
