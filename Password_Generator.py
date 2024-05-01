import random
import string

chars=string.ascii_letters+string.digits+string.punctuation
len=int(input("Enter the length of the password: "))
amount=int(input("Enter the amount of passwords you want: "))
for j in range(amount):
  # lib function method
   password="".join([random.choice(chars) for i in range(len)])
   # password=[random.choice(chars) for i in range(len)]
# for i in range(len):
#   password+=random.choice(chars)  
# print('Your password is: ',password)
   print('Your Random Password is: ',password)
