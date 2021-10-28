guesses=0
print("you are playing the number game")
print("enter your name ")
Name=str(input())
print ("hello, ",Name, "welcome to the number game")
import random
for x in range (1):
   num1=random.randint(1,10)
a = int(input("enter a number between 1 to 10: ", ))
while a != num1 and guesses<2:
   try:
     if a > num1:
        print("your guess was bit high, pleas select a lower number")
     elif a < num1:
         print("your guess is a bit low, please select a higher number")
   finally:
    a = int(input("enter your guess again:", ))
    guesses=guesses+1
    if guesses == 2:
           print("you have lost,", Name, ", better luck next time.")
           print("the correct number to be guessed was: ",num1)
if num1 == a:
     print ("congrats,you guessed the correct number", Name, ", you are the winner!!!")
z=input("press enter to exit")


