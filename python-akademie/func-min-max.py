def my_min(sequence):
    minval = sequence[0]
    for item in sequence[1:]:
        if  item < minval:
            minval = item
    return minval

def my_max(sequence):
    maxval = sequence[0]
    for item in sequence[1:]:
        if  item > maxval:
            maxval = item
    return maxval

# Test
lst = [8,2,3,1,4,5,15,6]
resultmin = my_min(lst)
print(resultmin)

resultmax = my_max(lst)
print(resultmax)