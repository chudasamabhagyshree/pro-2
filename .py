print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Right-Angled Triangle")
    print("2. Pyramid")
    print("3. Left-Angled Triangle")
    print("4. Analyze a Range of Numbers")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows = int(input("Enter the number of rows: "))

        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == 2:
        rows = int(input("Enter the number of rows: "))

        for i in range(1, rows + 1):
            print(" " * (rows - i) + "* " * i)

    elif choice == 3:
        rows = int(input("Enter the number of rows: "))

        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * i)

    elif choice == 4:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total = 0

        for num in range(start, end + 1):
            if num % 2 == 0:
                print("Number", num, "is Even")
            else:
                print("Number", num, "is Odd")

            total += num

        print("Sum of all numbers from", start, "to", end, "is:", total)

    elif choice == 5:
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")