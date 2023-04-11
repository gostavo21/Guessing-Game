#defeind random function
import random 
#creat a random number frome 1 to 10
computerNumber = random.randint(0,10)
#start the game
print("You Now Start The Guessing Number game \n Guess The Computer Number \n Good Luck ")
# get a number from user
userNumber = int(input("Enter a Number Between 1 and 10:"))
#creat and give (a) a value
a = 5
#check if the user guess the computer number 
if computerNumber == userNumber :
    #if the user guess the computer number 
    print("You Guessed!")
#other way if the user didnt guess the computer number
if computerNumber != userNumber :
        #make a loop 4 time
        while a > 1 :
            #tell the user the number of attempts rest
            print("You Have " + str(a-1) + " Attempts") 
            #get a number from user again
            userNumber21 = int(input("Enter a Number Between 1 and 10:"))
            #check again if the user guess the computer number
            if computerNumber == userNumber21 :
                #if the user guess the random number:
                print("Yoo Hoo ,You Guessed!")
                break
            
            a = a - 1
            
            if a == 1 :
                print("sorry you  run out of attempts.")
