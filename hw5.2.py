decision = True
while decision:
    number_1 = float(input('Enter first number:'))
    number_2 = float(input('Enter second number:'))
    action = input('Select an action:')
    if action == "+":
        print(number_1 + number_2)
    elif action == "-":
        print(number_1 - number_2)
    elif action == "/":
        if number_2 !=0:
            print(number_1 / number_2)
        elif number_2 == 0:
            print('Why are u trying to divide by zero?! Run script again and try with normal numbers.')
    elif action == "*":
        print(number_1 * number_2)
    else:
        print('Unknown action')
    decision = input('Continue? "y" for yes, any button for no:') == 'y' or 'Y'