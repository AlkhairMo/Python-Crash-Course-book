prompt = 'This programme tell you is the number multiple of 10 or not:'
prompt += '\nType a number: '
number = input(prompt)
number = int(number)
if number % 10 == 0:
    print('\nIt is multiple of 10.')
else:
    print('\nIt is not multiple of 10.')