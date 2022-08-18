def binary_search(sorted_list, item):
    first = 0
    last = len(sorted_list) - 1
    found = False
    while ((not found) and first <= last):
        mid = (first + last) // 2
        if sorted_list[mid] == item:
            found = True
            return mid
        else: 
            if item<sorted_list[mid]:
                first = mid + 1
            else:
                last = mid - 1
    return found