while True:
    reason = input('Write quit to end.\n'
                   'Why do you like python? ')
    if reason != 'quit':
        with open('text_files/python_lovers', 'a') as file_object:
            file_object.write(reason + '\n')
    else:
        break

