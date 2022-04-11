import random

# returns a randomised array of length "length"
def generate_array(length):
    result = []
    for i in range(length):
        result.append(random.randint(0,64))
    return result
