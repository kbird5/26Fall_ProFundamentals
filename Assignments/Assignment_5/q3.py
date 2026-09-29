def check_number(number):
    if (number & 1) == 0:
        return "even"
    else:
        return "odd"

number_input = int(input("Enter a whole number: "))

result = check_number(number_input)

print(f"The number {number_input} is {result}")