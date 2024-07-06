#Module 5: Creating Python Programs

#Part 1:
print('Part 1:\nCalculate the average rainfall over a period of years\n')

num_years = int(input('  Enter the number of years:\n  '))
num_months = num_years * 12
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
total_rainfall = 0

for i in range(num_years):
  for month in months:
    rainfall = float(input(f'  Inches of rainfall for {month} of year {i+1}:\n  '))
    total_rainfall += rainfall

print('\n')
print(f'Number of Months:         {num_months}')
print(f'Total inches of rainfall: {total_rainfall} inches')
print(f'Average rainfall:         {total_rainfall / num_months} in/month')

print('\n\n---------------------------------------------------------------------------\n\n')

#Part 2:
print('Part 2:\nCSU Global Bookstore book club awards points\n')

num_books = int(input('Enter the number of books purchased this month:\n'))
points = 0

if num_books >= 8:
  points = 60
elif num_books >= 6:
  points = 30
elif num_books >= 4:
  points = 15
elif num_books >= 2:
  points = 5
else:
  points = 0

print('\n')
if points > 0:
  print(f'{points} points awarded this month!')
else:
  print(f'{points} points awarded this month.')
