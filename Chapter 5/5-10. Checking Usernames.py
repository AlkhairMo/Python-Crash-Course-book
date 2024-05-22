current_users = ['ali', 'ahmed', 'osman', 'khalid', 'yousif', 'admin']
new_users = ['isa', 'mohamed', 'ALI', 'saleh', 'admin', 'omar']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('This username is used! enter a new one')
    else:
        print('Available username')
