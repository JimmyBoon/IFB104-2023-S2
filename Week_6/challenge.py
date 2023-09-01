# write a program to take number inputs from the command line
# the numbers should be between 1 and 10 inclusive
# if the letter x is entered, then the program should stop taking inputs
# and then print out all the numbers entered.

inputValue = ''
inputs = []

while inputValue != 'x':

    inputValue = input('Type in a number between 1 and 10 or x to stop: ')

    if inputValue.isnumeric() == True:
        if eval(inputValue) <= 10 and eval(inputValue) > 0:
            inputs.append(eval(inputValue))
        else:
            print('The number must be between 1 and 10.')
    elif inputValue.lower() == 'x':
        for item in inputs:
            print(str(item))
    else:
        print('Please enter a number between 1 and 10 or x to stop.')

print("Enter numbers between 1 and 10 inclusive or x to stop")

numbers = []
number = input("Enter a number: ")

while number.lower() != "x":
    
    number = int(number)

    if number >= 1 and number <= 10:
        numbers.append(number)
    
    else:
        print("Invalid number")

    number = input("Enter a number: ")

print("Numbers entered:")

for number in numbers:
    print(number)