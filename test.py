# guess number game
from random import randint

for x in range(1,8):
  guessnumber=int(input("enter guess number between 1to 10: "))
  randomnumber=randint (1,10)
  if guessnumber==randomnumber:
   print("You Have Won")
  else:
    print("You Have lose")
    print("Random number was: ",randomnumber)