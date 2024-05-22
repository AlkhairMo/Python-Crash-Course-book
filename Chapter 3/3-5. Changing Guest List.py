guest = ['moneeb', 'mohanad', 'malik', 'gazali']
message1 = f'Dear {guest[0].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message2 = f'Dear {guest[1].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message3 = f'Dear {guest[2].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
message4 = f'Dear {guest[3].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
print(message1)
print(message2)
print(message3)
print(message4)
print(f"{guest[2].title()} couldn't come")
guest[2] = 'ali'
message3 = f'Dear {guest[2].title()}\n\tI hope you can join me for dinner tonight at my home.\n\t\t\t\t\t\t\t\t\tyours Alkhair'
print(message3)