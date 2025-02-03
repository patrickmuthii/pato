from django.db import models

# Create your models here.
import getpass
#password = input('Enter password: ')
password = 'pato'
password = getpass.getpass( "Enter password: " )
if password == password:
    print('corret')
#else:
 #   for i in range(10):
  #      i = 'fuck you men'
   #     print('this is not the password ' ,i )

