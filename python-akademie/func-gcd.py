def gcd(a,b):
    while b > 1:
        reminder = a % b
        if not reminder:
            break
        a,b = b,reminder
    return b

