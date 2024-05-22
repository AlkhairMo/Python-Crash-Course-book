def show_pet_names(pet_type_file):
    try:
        with open(pet_type_file) as f:
            content = f.read()
    except FileNotFoundError:
        print(f'the file {pet_type_file} not founded')  # it will be 'pass' for 10-10. silent cats and dogs
    else:
        print(content.rstrip())


pet_type = input('Want to see dogs or cats names? ')
pet_type_file = f'text_files/{pet_type}.txt'
show_pet_names(pet_type_file)
