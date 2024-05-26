def swap(my_list, pivot_index, swap_index):
    my_list[pivot_index], my_list[swap_index] = my_list[swap_index], my_list[pivot_index]


def get_swap_index(my_list, pivot_index, end_index):
    # Pivot index is first index of list
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, i, swap_index)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort(my_list, first_index, end_index):
    if first_index < end_index:
        swap_index = get_swap_index(my_list, first_index, end_index)
        quick_sort(my_list, first_index, swap_index-1)
        quick_sort(my_list,swap_index + 1, end_index)
    return my_list


if __name__ == "__main__":
    my_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
    print(quick_sort(my_list, 0, 8))