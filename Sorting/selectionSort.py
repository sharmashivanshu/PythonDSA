def selection_sort(my_list):
    for i in range(len(my_list)):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
        my_list[min_index], my_list[i] = my_list[i], my_list[min_index]
    print(my_list)


if __name__ == "__main__":
    my_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
    selection_sort(my_list)