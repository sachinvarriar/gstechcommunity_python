operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
! for factorial
''')

def factorial(x):
  factorial = 1
  if x < 0:
    print("Sorry, factorial does not exist for negative numbers")
  elif x == 0:
    print("The factorial of 0 is 1")
  else:
     for i in range(1,x + 1):
         factorial = factorial*i
     print(x,"! = ",factorial)
      

if operation == '+':
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

elif operation == '!':
    number_1 = int(input('Enter your first number: '))
    print(factorial(number_1))

else:
    print('You have not typed a valid operator, please run the program again.')