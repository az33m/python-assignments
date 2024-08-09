A = float(input('Enter the first number: '))
B = float(input('Enter the second number: '))
operator = input('Enter the operator like +, -, *, /: ')

print(A)
print(B)

if operator == '+':
    output = A + B
    print('The output of A + B is:',output)

if operator == '-':
    output = A - B
    print('The output of A - B is:',output)

if operator == '*':
    output = A * B
    print('The output of A * B is:',output)

if operator == '/':
    output = A / B
    print('The output of A / B is:',output)