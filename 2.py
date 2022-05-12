a = float(input('Enter first number: '))
operator = input('Enter operator\n1. add\t2. subtract\t3. multiply\t4. division\t5. floor division\t6. modulus\n')
b = float(input('Enter second number: '))

if operator == '1' or operator == '+':
    print('Result = ' + str(a + b))
elif operator == '2' or operator == '-':
    print('Result = ' + str(a - b))
elif operator == '3' or operator == '*':
    print('Result = ' + str(a * b))
elif operator == '4' or operator == '/':
    print('Result = ' + str(a / b))
elif operator == '5' or operator == '//':
    print('Result = ' + str(a // b))
else:
    print('Result = ' + str(a % b))