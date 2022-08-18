def insertion_sort(unsorted_list):
    sorted_list = []
    while len(unsorted_list)> 0:
        smallest_index = 0
        smallest = unsorted_list[smallest_index]
        for index, elem in enumerate(unsorted_list):
            if elem<smallest:
                smallest = elem
                smallest_index = index
        unsorted_list.pop(smallest_index)
        sorted_list.append(smallest)
    return sorted_list