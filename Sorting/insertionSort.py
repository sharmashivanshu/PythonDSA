def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        unsort_item = my_list[i]
        for j in range(0, i):
            if my_list[j] < unsort_item:
                my_list[j], my_list[i] = my_list[i], my_list[j]
    print(my_list)


if __name__ == "__main__":
    my_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
    insertion_sort(my_list)
