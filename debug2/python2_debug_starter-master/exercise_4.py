def main():
    # This function should sort the list, but something is not quite right...
    nums = [3, 6, 5, 4, 2, 8, 1, 10, 7, 9]
    switched = 0
    while True:
        switched = 0
        for j in range(0, len(nums) - 1):
            if nums[j] > nums[j+1]:

                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                switched = 1

        if switched == 0:
            break
    # should print: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
    print(nums)


if __name__ == "__main__":
    main()
