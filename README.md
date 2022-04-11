# **How to use**

`pip install shitsort`

example usage:
```
import shitsort

myarray = [1, 5, 12, 6, 6, 11]
print(shitsort.bogosort(myarray))
print(shitsort.multibogosort(myarray, 4)) # uses 4 processes
print(shitsort.bozosort(myarray))
print(shitsort.slowsort(myarray))

>>> [1, 5, 6, 6, 11, 12]
>>> [1, 5, 6, 6, 11, 12]
>>> [1, 5, 6, 6, 11, 12]
>>> [1, 5, 6, 6, 11, 12]
```

## **functions:**

### `bogosort(array)`

returns a new sorted array of `array` using the bogosort algorithm without modifying the passed in array ([pseudocode](https://en.wikipedia.org/wiki/Bogosort#Description_of_the_algorithm))

### `multibogosort(array, numthreads)`

returns a new sorted array of `array` using the bogosort algorithm without modifying the passed in array, but on multiple processes simultaneously. The number of processes can be specified with `numthreads`

### `bozosort(array)`

returns a new sorted `array` using the bozosort algorithm, without modifying the passed in array ([paper includes pseudocode somewhere](https://link.springer.com/chapter/10.1007/978-3-540-72914-3_17))

### `slowsort(array)`

returns a new sorted `array` using the slowsort algorithm, without modifying the passed in array([pseudocode](https://en.wikipedia.org/wiki/Slowsort#Algorithm))

<sub>**contributors**: sh6heer, jas-dzied</sub>

<sub>Licensed under GPL GNUv3</sub>
