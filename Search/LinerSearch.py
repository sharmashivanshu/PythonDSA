def linear_search(my_list , item):
    i=0
    while len(my_list) > i:
        if my_list[i] == item:
            print(f"Item {item} found")
            break
        i+=1
    else:
        print("Not found")


if __name__ == "__main__":
    my_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
    linear_search(my_list, 9)