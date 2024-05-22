def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
my_profile = build_profile('Alkhair', 'mohamed',
                           age=19,
                           city='khartoum',
                           birtday='13th august',
                           )
print(my_profile)