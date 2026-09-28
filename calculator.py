def calculator():
    print("\n--- Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))

        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                print("Error: Cannot divide by zero.")
                return
            result = first_number / second_number
        else:
            print("Error: Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")
