"""
Runs the slowsort algorithm
I have no idea what it is doing
"""
import math

def _slowsplit(arr, i, j):
    """
    calls recursively to slowsort
    """
    if i >= j:
        return arr
    mid = math.floor( (i+j)/2 )
    _slowsplit(arr, i, mid)
    _slowsplit(arr, mid+1, j)

    if arr[j] < arr[mid]:
        arr[j], arr[mid] = arr[mid], arr[j]
    _slowsplit(arr, i, j-1)
    return arr # unreachable but gets 10/10 on pylint

def slowsort(arr):
    """
    does the i,j bit for you because it's gross
    """
    result = list(arr)
    _slowsplit(result, 0, len(result)-1)
    return result
