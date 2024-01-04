print("Provide two numbers which will be added together.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")

    if first_number == 'q':
        break
    else:
        try:
            first_number = int(first_number)
        except ValueError:
            print("Please provide a numeric value.")
        else:
            second_number = input("Second number: ")

            if second_number == 'q':
                break
            else:
                try:
                    second_number = int(second_number)
                except ValueError:
                    print("Please provide a numeric value.")
                else:
                    result = first_number + second_number
                    print(result)
