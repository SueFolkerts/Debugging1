def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if val == target:
            return x
        elif val < target:
            if lower == x:
                break
            lower = x
        elif val > target:
            upper = x
    return "Hmmm... Looks like {} is not in the list".format(key)


def main():
    num_list = [10, 22, 30, 35, 39, 42, 49, 55, 68, 70, 99]
    print(binary_search(num_list, 68))


if __name__ == "__main__":
    main()
