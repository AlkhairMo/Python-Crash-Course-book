with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

""" printing line by line """
with open('text_files/pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

""" making a list of lines """
with open('text_files/pi_digits.txt') as file_object:
    lines = file_object.readlines()
print(lines)
print(lines[0])

""" working with file's content """
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(f'We have {len(pi_string) - 2} decimal place of pi.')
# or by using slicing
simple_pi_string = pi_string[:4]
print(simple_pi_string)
pi = float(simple_pi_string)
