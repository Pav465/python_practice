from random import randint, random
import  random;
secret = random.randint(0,10)
guess= int(input("Enter your secret number between 1 to 10: "))
if guess == secret:
 print("guess is correct")
elif guess > secret:
 print("The guess number is higher than your secret number")
else:
  print("The guess number is lower than your secret number")