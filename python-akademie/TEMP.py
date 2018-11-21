values = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]

def modus(values):
    counts = {}
    for value in values:
        counts[value] = counts.setdefault(value,0) + 1
 
    result = None
    nums = []
    for k,v in counts.items():
        if not result or result[1] < v:
            result = (k,v) 
        elif result[1] == v:
            nums.append(k)
            result = (k,v)
        elif result[1] > v:
            nums = [k]
            result = (k,v)
            
    return result[0]

result = modus(values)
print(result)




