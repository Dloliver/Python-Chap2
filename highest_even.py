#function that takes  random numbers and returns the highest even number in the kwargs

def highest_even(li):
    even = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even([10, 2, 3, 4, 8, 11]))
