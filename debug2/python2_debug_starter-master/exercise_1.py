def main():
    s = ''
    for i in range(1, 11):
        s = s + str(i) + ", "
    s = s[:-2]
    # should print: "1 2 3 4 5 6 7 8 9 10"
    print(s)


if __name__ == "__main__":
    main()
