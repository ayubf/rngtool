import sys
import random
import argparse


def main():

    def rollDice():
        n = random.randint(1,6)
        print('You rolled a',n)

    def coinToss():
        n = random.randint(1,2)
        if n  == 1:
            print('You flipped Heads!')
        elif n == 2:
            print('You flipped Tails!')

    def randOptions():
        if len(sys.argv) < 3:
            print('Error, incorrect syntax: Specify minimum and maximum after opt. See help for more')    
        else:
            if len(sys.argv) < 4:
                print('Error, incorrect syntax: Specify minimum and maximum after opt. See help for more')    
            else:
                if int(sys.argv[2]) > int(sys.argv[3]):
                   print('Error, invalid range: switch the numbers around')
                else: 
                     n = random.randint(int(sys.argv[2]), int(sys.argv[3]))
                     print('You got',n)
          
    def help():
        print(''' 
        / RNG Tool v1.0 /
        
        ~ Random number generator tool for Linux ~ 

        .Command Index:

            dice: gives number between 1 and 6(Rolling dice)
            
            coin: gives number between 1 and 2(Heads or Tails)

            opt [starting number] [ending number]: gives number between given starting number and ending numbers 

                Ex: opt 1 100(output  = number between 1 and 100)
                
        
        .About:

         Made by: Ayub Farah
         Version: 1.0
         Email: razortyphon@gmail.com
         Repo: https://github.com/ayubf/rngtool

        Thank you for installing!
        
        ''')
    if len(sys.argv) <= 1:
        help()
    elif sys.argv[1] == 'dice':
        rollDice()
    elif sys.argv[1] == 'coin':
        coinToss() 
    elif sys.argv[1] == 'opt':
        randOptions()
    elif sys.argv[1] == 'help':
        help()
