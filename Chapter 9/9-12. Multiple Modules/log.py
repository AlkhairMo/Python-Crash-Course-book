from user import User
from admin import Admin


admin = Admin('Alkhair', 'mohamed', 3,
              'can delete post', 'can ban user',
              age=19, username='theboss'
              )
admin.show_privileges()

user = User('Mohamed', 'Ali', username='theonetheonly')
user.describe_user()
user.greet_user()
