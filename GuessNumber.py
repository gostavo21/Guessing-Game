#defeind random function
import random 
#creat a random number frome 1 to 10
computerNumber = random.randint(0,10)
#start the game
print("You Now Start The Guessing Number game \n Guess The Computer Number \n You Have 5 Chance \n Good Luck ")
# get a number from user
userNumber = int(input("Enter a Number Between 1 and 10:"))

#check if the user guess the computer number 
if computerNumber == userNumber :
    #if the user guess the computer number 
    print("You Guessed!")
#other way if the user didnt guess the computer number
elif computerNumber != userNumber :
	#creat and give (a) a value
	a = 4
        #make a loop 4 time                                                                                                           
	while a > 0 :
            #tell the user the number of attempts rest
            print("You Have " + str(a) + " Attempts") 
            #get a number from user again
            userNumber21 = int(input("Enter a Number Between 1 and 10:"))
            #check again if the user guess the computer number
            if computerNumber == userNumber21 :
                #if the user guess the random number:
                print("Yoo Hoo ,You Guessed!")
                break
         
            a = a - 1
            
            if a == 0 :
                print("Sorry You  Run Out of Attempts.")
                
                
                
                
