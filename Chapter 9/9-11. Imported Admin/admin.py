from user import Admin

admin = Admin('Alkhair', 'mohamed', 3,
              'can delete post', 'can ban user',
              age=19, username='theboss'
              )
admin.show_privileges()