import re
import sys

def parse_input(input_string):
    numbers = re.findall(r'[-+]?\d*\.\d+|\d+|\d+e[-+]?\d+', input_string.replace(',', ' '))
    return [float(num) for num in numbers]

def format_number(number):
    if number.is_integer():
        return str(int(number))
    elif abs(number) >= 1000 or abs(number) < 0.001:
        return "{:.2e}".format(number)
    else:
        return "{:.2f}".format(number)

def insert_numbers(numbers, all_numbers):
    all_numbers.extend(numbers)

def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            numbers = parse_input(content)
            return numbers
    except FileNotFoundError:
        print("File not found.")
        return []
    except IOError:
        print("Error reading the file.")
        return []

def find_minimum_number(numbers):
    return min(numbers)

def find_maximum_number(numbers):
    return max(numbers)

def print_menu():
    print("----- Menu -----")
    print("1. Enter numbers manually")
    print("2. Load numbers from a file")
    print("3. Find the minimum number")
    print("4. Find the maximum number")
    print("5. Exit")
    print("----------------")

def get_input():
    return input("Enter your choice: ")

def process_choice(choice, all_numbers):
    if choice == '1':
        input_numbers = input("Enter numbers (separated by commas or spaces): ")
        numbers = parse_input(input_numbers)
        insert_numbers(numbers, all_numbers)
    elif choice == '2':
        filename = input("Enter filename: ")
        numbers = read_numbers_from_file(filename)
        insert_numbers(numbers, all_numbers)
    elif choice == '3':
        if all_numbers:
            min_number = find_minimum_number(all_numbers)
            print("Minimum number: ", format_number(min_number))
        else:
            print("No numbers found.")
    elif choice == '4':
        if all_numbers:
            max_number = find_maximum_number(all_numbers)
            print("Maximum number: ", format_number(max_number))
        else:
            print("No numbers found.")
    elif choice == '5':
        sys.exit()
    else:
        print("Invalid choice. Please try again.")

def main():
    all_numbers = []

    while True:
        print_menu()
        choice = get_input()
        process_choice(choice, all_numbers)

if __name__ == '__main__':
    main()
