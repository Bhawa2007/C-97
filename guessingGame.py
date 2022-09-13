import random
import random
guessnumber=input("Guess number between 1-9")
guessCount = 0
randum=random.randit(1,9)

if guessCount == 7:
   print("Congrats,You are fantastic")

for i in guessnumber:
   guessCount=guessCount+1
   if(guessCount == 5):
      print("You lost")
      
       


