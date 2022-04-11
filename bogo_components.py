import random

# returns a bool value
# of whether the passed in array is in order or not
def check_if_ordered(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

# modifies passed in array to
# return a random permutation
def shuffle(arr):
    for i in range(len(arr)-1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
