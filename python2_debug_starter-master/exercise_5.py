def main():
    # this function should print out the largest number in the list but something is not quite right...
    nums = [4, 32, 41, 23, 10, 4, 36, 24, 29, 35, 38, 40, 12, 33, 42, 26, 27, 19, 20, 2, 43, 41, 34, 38, 39, 45, 42, 41,
            34, 23, 26, 40]
    max_num = 0
    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
    # should print: "45"
    print(max(nums))


if __name__ == "__main__":
    main()
