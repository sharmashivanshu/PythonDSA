def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list)-1-i):
            if my_list[j] > my_list[j + 1]:
                my_list[j + 1], my_list[j] = my_list[j], my_list[j+1]

    print(my_list)


if __name__=="__main__":
    my_list = [2,1,7,6,5,3,4,9,8]
    bubble_sort(my_list)