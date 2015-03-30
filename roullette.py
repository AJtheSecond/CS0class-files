# -*- coding: utf-8 -*-
#1) Take function input for numberGuessed, colorGuessed, and evenOrOdd.
#2) Create color list for red/black/green numbers
#3) Generate random integer between 0 – 37 (37 == “00”)
#4) Check to see if number is even or odd
# a) Check to see if user guess is correct
#5) Check to see if number is black or red or green
# a) Check to see if user guess is correct
#6) Check to see if random number == numberGuessed
#7) Return results to user. Let user know what guesses are correct, and which are not.


import random
 
 
 
def rouletteSimulatin(numberGuess, evenOrOdd, colorGuess):
    ''' First enter your number,
    Second enter even or odd
    Third enter black, red or green. '''
 
    #DECLARING NECESSARY VARIABLES
 
    numberChosen = random.randint(0, 37)
 
    print "You rolled a %s" %numberChosen
 
    def evenOrOdd(numberChosen):
        if numberChosen % 2 == 0:
            numberChosen = "even"
 
        elif numberChosen % 2 != 0:
            numberChosen = "odd"
 
 
        if evenOrOdd == numberChosen:
            print "Winner winner chicken dinner "
        else:
            print "Sorry, you did not guess even or odd right. Please try again"
 
    def checkColor(numberChosen):
        blackList = [2,4,6,8,10,11,13,15,17,20,22,24,26,29,31,33,35]
        redList = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,28,30,32,34,36]
        greenList = [0, 37] # 37 sunsitutes for "00"
 
        if numberChosen in blackList:
            numberChosen = "black"
            if numberChosen == colorGuess:
                print "Winner winner chicken dinner"
            else:
                print "Sorry it was black. Please try again"
 
 
        elif numberChosen in redList:
            numberChosen = "red"
            if numberChosen == colorGuess:
                print "Winner winner chicken dinner"
            else:
                print "Sorry it was red. Please try again"
 
 
        elif numberChosen in greenList:
            numberChosen = "green"
            if numberChosen == colorGuess:
                print "Winner winner chicken dinner"
            else:
                print "Sorry it was green. Please try again"
    
 
    def checkNumber(numberChosen):
        if numberChosen == numberGuess:
            print "Winner winner chicken dinner"
        else:
            print "You chose the wrong number. Please try again"
 
    checkNumber(numberChosen)
    evenOrOdd(numberChosen)
    checkColor(numberChosen)
 
rouletteSimulatin(1, 'even', 'black')