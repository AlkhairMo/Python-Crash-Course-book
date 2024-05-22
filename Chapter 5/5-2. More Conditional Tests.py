name = 'Alkhair'
print('Is the name "Alkhair"?')
print(name == "Alkhair")
print('Is the name "alkhair"?')
print(name == 'alkhair')

print('case dose not matter, answer will be:')
print(name.lower() == 'alkhair')

age = 19
print('Is my old greater than or equal to 20?')
print(age >= 20)
print('Is my old less than 15?')
print(age < 15)
print('Is my old equal to 16?')
print(age == 16)
print('Is my age less than or equal to 19?')
print(age <= 19)
print('Is my age not equal to 17?')
print(age != 17)
print('Is my age greatest than 18?')
print(age > 18)

print('my age is equal to 18 or 19')
print((age == 19) or (age == 18))
print('Well, my age greater than 15 and less than 19?')
print((age > 15) and (age < 19))
print(f'yes my age is {age}')

juices = ['mango', 'karkade', '3aradeab', 'gongolaiz']
print('Is karkade missed?!')
print('karkade' not in juices)
print('Is helomor existed?')
print('helomor' in juices)
juices.append('helomor')
print('Is it existed now?')
print('helomor' in juices)