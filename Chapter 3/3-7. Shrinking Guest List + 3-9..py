guest = ['moneeb', 'mohanad', 'malik', 'gazali']
'''
message1 = f'Dear {guest[0].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message2 = f'Dear {guest[1].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message3 = f'Dear {guest[2].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message4 = f'Dear {guest[3].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
print(message1)
print(message2)
print(message3)
print(message4)
'''
print('original guest num:-')
print(len(guest))
print(f"{guest[2].title()} couldn't come")
guest[2] = 'ali'
#message3 = f'Dear {guest[2].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
#print(message3)
print('I found a bigger dinner table!')
guest.insert(0,'ahmed')
guest.insert(3,'mohamed')
guest.append('fawaz')
print('second guests number = ', len(guest))
message1 = f'Dear {guest[0].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message2 = f'Dear {guest[1].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message3 = f'Dear {guest[2].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message4 = f'Dear {guest[3].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message5 = f'Dear {guest[4].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message6 = f'Dear {guest[5].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message7 = f'Dear {guest[6].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message7)
print('I can only invite 2 friend')
print(guest)
poped1 = guest.pop(0)
poped2 = guest.pop(3)
poped3 = guest.pop(4)
poped4 = guest.pop(-1)
poped5 = guest.pop(-2)
apolgy1 = f"Dear {poped1.title()}\n\tI am sorry to tell you that you can't come tonight because of table problem.\n\t\t\t\t\t\t\t\t\tyours Alkhair"
apolgy2 = f"Dear {poped2.title()}\n\tI am sorry to tell you that you can't come tonight because of table problem.\n\t\t\t\t\t\t\t\t\tyours Alkhair"
apolgy3 = f"Dear {poped3.title()}\n\tI am sorry to tell you that you can't come tonight because of table problem.\n\t\t\t\t\t\t\t\t\tyours Alkhair"
apolgy4 = f"Dear {poped4.title()}\n\tI am sorry to tell you that you can't come tonight because of table problem.\n\t\t\t\t\t\t\t\t\tyours Alkhair"
apolgy5 = f"Dear {poped5.title()}\n\tI am sorry to tell you that you can't come tonight because of table problem.\n\t\t\t\t\t\t\t\t\tyours Alkhair"
print('final guests number = ', len(guest))
print(apolgy1)
print(apolgy2)
print(apolgy3)
print(apolgy4)
print(apolgy5)
emphasize1 = f"Dear {guest[0].title()}\n\tI can't wait to see you tonight!\n\t\t\t\t\t\t\t\t\tyours Alkhair"
emphasize2 = f"Dear {guest[1].title()}\n\tI can't wait to see you tonight!\n\t\t\t\t\t\t\t\t\tyours Alkhair"
print(emphasize1)
print(emphasize2)
del guest[0]
del guest[-1]
print(guest)
