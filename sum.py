def main():
    n = int(input("Enter Number: "))
    i = 1
    sum = 0

    for i in range(1, n + 1):
        sum += i

    print("Sum is:", sum)

if __name__ == "__main__":
    main()

