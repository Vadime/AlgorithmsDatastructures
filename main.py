import random
import time

from merge_sort import merge_sort

def test_sorted_list(sorted_list): 
    for i in range(len(sorted_list) - 1):
        assert sorted_list[i] <= sorted_list[i+1]

if __name__ == "__main__":
    l = []
    for i in range(999):
        l.append(random.randint(0, 999))

    start = time.time()

    # print(binary_search(l, 42))
    # print(selection_sort(l))
    # print(insertion_sort(l))
    # print(bubble_sort(l))
    # print(stupid_sort(l))
    merge_sort(l)
    print(l)
    print(time.time() - start)

    test_sorted_list(l)



