import random  #the random module helps you make choices
import string
from urllib import response  #the string module lets you do useful things with strings, like splitting them apart otr changing the way they appear.

adjectives = ['sleepy', 'slow', 'smwlly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluppy', 'white', 'proud', 'brave']   #the  list is stored in the variable adjectives

nouns = ['apple', 'dinousaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda']

print('Welcome to Password Picker!') #this line shows a message to welcome the user

while True:
    adjective = random.choice(adjectives)  #this variable holds a word chosen randomly from the adjectives list
    noun = random.choice(nouns)    #one of the nouns from the list is chosen and stored in this variable
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)    #punctuation is a constant

    password  = adjective + noun + str(number) + special_char
    print("Your new password is: %s" % password)

    response = input('Would you like another password? Type y or n: ')
    if response =='n':
        break
