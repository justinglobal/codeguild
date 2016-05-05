#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import randint

words = ["art", "Dali", "contrapposto", "rococo", "impressionism", "realism", "dadaism", "surrealism", "post-impressionism", "fauvism"]
numWrong = 0
listedWord = [None]


# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
   global listedWord

   # Greet the user
   print("Let's play a game of hangperson!")

   # Randomly select a word from the list of words
   numlist = len(words)

   aw = randint(0, numlist-1)
   rw = words[aw]

   # Make the randomly selected word into a list object
   #i casted so list(rw) is casting a random word into the list
   listedWord=list(rw)

   # Make another list the same length as the word, but with
   # '_' instead of letters. This will track the user's progress.
   # Use the variable name currentState
# for every chara in listed word add a _ to current state 
   currentState = []
   for x in listedWord: 
      currentState.append("_")
   # Initialize wrong guess
   incorrect = []

   # Print the initial state of the game
   printHangperson(currentState, incorrect)

   # Start the game! Loop until the user either wins or loses
   while currentState != listedWord and numWrong < 6:
      #ask user to guess
      guess = userGuess()
      bundledList = updateState(guess, currentState,incorrect)
      currentState = bundledList[0]
      incorrect = bundledList [1]
# see if the guess is in the word, update accordingly 

      printHangperson(currentState, incorrect)


   # Determine if the user won or lost, and then tell them accordingly
   if numWrong >= 6: 
      print("You Wienie! You Looooozzzz")
   elif listedWord ==currentState:
      print("You Win But you are still a Wienie!")



# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState





def updateState(guess, currentState, incorrect):
   global numWrong

   # First, determine if the letter guessed is in the word.
   numInWord = listedWord.count(guess)

   # If it isn't, tell the user and update the numWrong var
   if numInWord== 0:
      print ("You wrong sucka!")
      numWrong = numWrong + 1
      # adds wrong guess to end of wrong guesses 
      incorrect.append(guess)
      # numWrong +=1
   elif numInWord > 0:
      print(str(numInWord) + guess + "'s  are in the word. Yes! Smarty Pants!")

   # If it is, congratulate them and update the state of the game.
   #    To update the state, make sure to replace ALL the '_' with
   #    the guessed letter.
   #while we still have letters to find, keep looping 
      numFound = 0
      index = 0
      while numFound < numInWord and index < len(listedWord):
         if listedWord [index] == guess: 
            currentState [index] = guess
            numFound += 1

         index +=1 

         #see if letter is in word index


   return [currentState, incorrect]


# This helpful function prompts the user for a guess,
# accepting only single letters.
#
# returns a letter
def userGuess():
   guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")
   while len(guess) != 1:
      print()
      if guess == "exit":      
         exit()
      else: 
         guess = input("One letter only Homie!!! Try again." )
       #user has given too many letters 
       #chk if it is exit then exit if it is
       #otherwise ask them to guess again 
   
   return guess

################# DO NOT EDIT BELOW THIS LINE ##################

# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state, incorrect):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")
   print(incorrect)
   print()

# This line runs the program on import of the module
hangperson()
