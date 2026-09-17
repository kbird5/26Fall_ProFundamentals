import random

#random.randint(1,10)

#print(random.randint(1,10))

#print(random.random())

##answer = random.randint(1,3)
##
##if answer == 1:
##    print("Yes")
##
##if answer == 2:
##    print("No")
##
##if answer == 3:
##    print("Maybe")

lucky_number = random.randint(1, 100)

##print(f"You will have a great day! Your lucky number is {lucky_number}")

fortune_number = random.randint(1,3)
fortune_text = ""

fortune_prediction = random.randint(1,2)
fortune_pred = ""

if fortune_number == 1:
    fortune_text = "You will have a great day!"

if fortune_number == 2:
    fortune_text = "Today will be tough... but worth it."

if fortune_number == 3:
    fortune_text = "You will get married this year!"
#print(fortune_text)
#print(f"{fortune_text} Your lucky number is {lucky_number}")

if fortune_prediction == 1:
    fortune_pred = "You will have a baby this year!"

if fortune_prediction == 2:
    fortune_pred = " You will not have a baby this year!"

print(f"{fortune_text} Your lucky number is {lucky_number} and {fortune_pred}")
