def binary_search(list_to_search, key):
    left = 0
    right = len(list_to_search)-1
    while left <= right:
        mid = (left + right) // 2
        if list_to_search[mid] == key:
            return mid
        elif list_to_search[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return "Hmmm... Looks like {} is not in the list".format(key)


def main():
    num_list = [10, 22, 30, 35, 39, 42, 49, 55, 68, 70, 99]
    print(binary_search(num_list, 68))


if __name__ == "__main__":
    main()
