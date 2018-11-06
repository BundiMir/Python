def my_find(sequence,item):
    for i, obj in enumerate(sequence):
        if obj == item:
            return i
    return -1

# test
find1 = my_find([1,2,4,15,6],4)
print(find1)


