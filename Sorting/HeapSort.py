def Heapify(my_list, n, start_idx):
    smallest = start_idx
    l = 2 * start_idx + 1
    r = 2 * start_idx + 2

    if l < n and my_list[l] < my_list[smallest]:
        smallest = l
    if r < n and my_list[r] < my_list[smallest]:
        smallest = r

    if smallest != start_idx:
        my_list[start_idx], my_list[smallest] = my_list[smallest], my_list[start_idx]
        Heapify(my_list, n, smallest)


def heap_sort(arr):
    n = len(arr)
    # Create Heao Binary and store in array
    for i in range(n // 2 - 1, -1, -1):
        print(i)
        Heapify(arr, n, i)
    # Sort Hwapify array by extracting root node after swaping with last node
    for i in range(n-1, 0, -1):
        my_list[i], my_list[0] = my_list[0], my_list[i]
        Heapify(my_list, i, 0)
    my_list.reverse()


if __name__ == "__main__":
    my_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
    heap_sort(my_list)
    print(my_list)
