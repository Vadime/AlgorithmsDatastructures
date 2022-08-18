import random

def is_sorted(l):
    for i in range(len(l)- 1):
        if l[i]>l[i+1]:
            return False
    return True

def stupid_sort(l):
    while not is_sorted(l):
        random.shuffle(l)
    return l