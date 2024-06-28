# Part 1
print('Part 1:\n    Write a program that calculates the total amount of a meal purchased at a restaurant. \n\
    The program should ask the user to enter the charge for the food and then calculate the\n\
    amounts with an 18 percent tip and 7 percent sales tax. Display each of these amounts \n\
    and the total price.\n\n')

food_price = float(input('Enter the charge for food:\n$'))
print('__________')

tax = food_price * 0.07
tip = food_price * 0.18

print('Sales Tax: ${tax:.2f}\n18% Tip:   ${tip:.2f}\n==========\nTotal:     ${total:.2f}'.format(tax = tax, tip = tip, total = food_price+tax+tip))

print('\n\n---------------------------------------------------------------------------\n\n')

# Part 2
print('Part 2:\n    Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).\n\
    If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).\n\
    Write a Python program to solve the general version of the above problem. Ask the user \n\
    for the time now (in hours) and then ask for the number of hours to wait for the alarm.\n\
    Your program should output what the time will be on a 24-hour clock when the alarm goes off.\n\n')

current_tm = int(input('Enter the current time (in hours)\n(24-hr clock): '))
alarm_hrs = int(input('Enter a number of hours to wait for your alarm:\nAlarm Hours: '))
print('\r')

alarm_tm = (current_tm + alarm_hrs) % 24
print('Alarm set for {}:00'.format(alarm_tm))
