from names_function import get_formatted_name

print("Enter 'q' to quit program.")

while True:
    first = input("\nPlease enter your frist name: ")
    if first == 'q':
        break
    last = input("Please enter you last name:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")
    
