def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to miles")
    print("2. Miles to kilometers")

    choice = input("Choose a conversion: ")

    try:
        value = float(input("Enter the value: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    if choice == "1":
        converted = value * 0.621371
        print(f"{value} km = {converted:.2f} miles")
    elif choice == "2":
        converted = value / 0.621371
        print(f"{value} miles = {converted:.2f} km")
    else:
        print("Invalid choice. Please choose 1 or 2.")
