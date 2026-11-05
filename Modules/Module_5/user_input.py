# user_text = input("Enter some text: ")
# print(user_text)
# print(user_text.upper())

# user_number = input("What do you want to double? ")
# print(user_number*2)

# user_number = input("What number do you want to double? ")
# print(int(user_number) * 2)

user_text = input("Enter some text: ")
upper_or_lower = input("Type 1 for upper, 2 for lower: ")

## make usre not to have anything in the () after upper or lower 
#   it will give error 
if upper_or_lower == "1":
    print(user_text.upper())
else:
    print(user_text.lower())

