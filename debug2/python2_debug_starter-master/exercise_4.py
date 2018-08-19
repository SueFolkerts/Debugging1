def main():
    nums = [3, 6, 5, 4, 2, 8, 1, 10, 7, 9]
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            temp = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = temp
            j = j-1
# should print: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
    print(nums)
if __name__ == "__main__":
    main()