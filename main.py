from calculator import calculator


def show_menu():
    print("\n=== Python Utilities ===")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            from converter import unit_converter
            unit_converter()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
