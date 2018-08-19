# compute the factorial
def factorial(n):
    if n == 0:
        return 0
    return n * factorial(n-1)


def main():
    # This program should compute the factorial of 5 (1 * 2 * 3 * 4 * 5 = 120)
    factorial_of_5 = factorial(5)
    # should print "120"
    print(factorial_of_5)


if __name__ == "__main__":
    main()
