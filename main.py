import sys
import re

def get_numbers():
    numbers = []
    choice = input("Enter numbers (comma-separated): ")
    if choice.lower() == "file":
        filename = input("Enter file name: ")
        try:
            with open(filename, "r") as file:
                content = file.read()
                numbers = re.findall(r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?", content)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            sys.exit(1)
    else:
        numbers = re.findall(r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?", choice)
    
    return [float(num[0]) if num[2] else int(num[0]) for num in numbers]

def find_min(numbers):
    return min(numbers)

def find_max(numbers):
    return max(numbers)

def remove_decimal(number):
    formatted_number = f"{number:g}"
    if "." in formatted_number:
        formatted_number = formatted_number.rstrip("0").rstrip(".")
    return formatted_number

def print_menu():
    print("============== MENU ==============")
    print("1. Enter numbers")
    print("2. Load numbers from a file")
    print("3. Find minimum value")
    print("4. Find maximum value")
    print("5. Exit")
    print("==================================")

def main():
    numbers = []
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            numbers = get_numbers()
            print("Numbers updated successfully.")
        elif choice == "2":
            numbers = get_numbers()
            print("Numbers loaded from file successfully.")
        elif choice == "3":
            if numbers:
                minimum = find_min(numbers)
                print(f"Minimum value: {remove_decimal(minimum)}")
            else:
                print("No numbers found. Please enter or load numbers.")
        elif choice == "4":
            if numbers:
                maximum = find_max(numbers)
                print(f"Maximum value: {remove_decimal(maximum)}")
            else:
                print("No numbers found. Please enter or load numbers.")
        elif choice == "5":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()