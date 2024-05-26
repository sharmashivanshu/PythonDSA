def merge(mylist, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    left = [0] * n1
    right = [0] * n2

    for i in range(0, n1):
        left[i] = mylist[l + i]

    for j in range(0, n2):
        right[j] = mylist[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] < right[j]:
            mylist[k] = left[i]
            i += 1
        else:
            mylist[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        mylist[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        mylist[k] = right[j]
        j += 1
        k += 1


def mergeSort(mylist, l, r):
    print(f"lef value:{l}")
    print(f"right value:{r}")
    if l < r:
        m = (l + r) // 2
        mergeSort(mylist, l, m)
        mergeSort(mylist, m + 1, r)
        merge(mylist, l, m, r)
    return mylist


if __name__ == "__main__":
    my_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
    print(mergeSort(my_list, 0, 8))
