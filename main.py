#importing the time module
import time
import random

#welcoming the user
name = input("What is your name? ")

print (  name + "!!!" " Get Ready...")

print ("")

#waiting time
time.sleep(1)

print (" Let's get started. Shall we!!")
time.sleep(0.5)
# ---------------------Randon line display start--------------------
read_file = open("hangman.txt","r")

file_output= read_file.read()
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

# print(file_output)

# read_file.close()
# --------------------------Random line display finish---------------

# #hewe set the secret
word = random_line('hangman.txt')
# print(word)

# creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char,end="")    

        else:
    
        # if not found, print a dash
            print ("__","",end="")     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("Yay!! Yon Won")


    # exit the script
        break              

    print
    print()
    print()

    # ask the user go guess a character
    guess = input("Start Guessing...") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Wrong")    
 
    # how many turns are left
        print ("You have", + turns, 'more guesses') 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose!!")  
            print ("Word was " + word + ".")