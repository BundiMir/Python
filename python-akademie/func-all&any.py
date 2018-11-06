def all(seq):
    for i in seq:
        if not bool(i):
            return False
    return True
            
def any(seq):
    for i in seq:
        if bool(i):
            return True
    return False




