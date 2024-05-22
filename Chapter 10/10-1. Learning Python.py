with open('text_files/learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)
print('\n')
learning_python = 'text_files/learning_python.txt'
with open(learning_python) as file_object:
    for line in file_object:
        print(line)

print('\n')
with open(learning_python) as file_object:
    objects = file_object.readlines()

print(objects)
print('\n')
for one_object in objects:
    print(one_object.rstrip())
print('\n')
for one_object in objects:
    print(one_object.replace('remove', 'delete').rstrip())
