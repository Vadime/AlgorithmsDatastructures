def selection_sort(unsorted_list):
    for index in range(len(unsorted_list)):
        min_index = index
        for i in range(min_index + 1, len(unsorted_list)):
            if unsorted_list[min_index] > unsorted_list[i]:
                min_index = i
                
        cache = unsorted_list[index]
        unsorted_list[index] = unsorted_list[min_index]
        unsorted_list[min_index] = cache

    return unsorted_list
