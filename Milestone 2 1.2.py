# -*- coding: utf-8 -*-
"""
Milestone 1: Black Jack game
"""
import random
import os
import time

palos = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
nums = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


#maybe get rid of this class, maybe this should just be tuple
class Card:
    # '''
    # Card takes a tuple and prints the card num and palo. It also checks the
    # num's value
    # '''
    
    # def __init__(self, cartopol):
    #     '''
    #     Parameters
    #     ----------
    #     cartopol : TYPE is tuple with two variables: palo and num
    #         DESCRIPTION.

    #     Returns
    #     -------
    #     None.

    #     '''
    #     self.num = cartopol[0] #the instance attribute suit = the parameter suit
    #     self.palo = cartopol[1]
   
    # def __str__(self):
    #     '''
    #     Returns
    #     -------
    #     str
    #         human readable text of the número y palo de la carta.

    #     '''
    #     return f"{self.num} of {self.palo}"
    
    # def value(self):
    #     return values[self.num]
    
    pass
        
    
class Deck:
    
    def __init__(self):
        '''
        Creates a deck of 52 cards, type is list with tuples: num,palo

        Returns
        -------
        None.

        '''
        self.deck = []  # start with an empty list
        for palo in palos:
            for num in nums:
                cartopol = (num,palo)
                #print(cartopol)
                self.deck.append(cartopol)
    
    def __str__(self):
        '''
        

        Returns
        -------
        str
            just prints the list of 52 tuples .

        '''
        return f"{self.deck}"

    def shuffle(self):
        '''
        shuffles the deck in place

        Returns
        -------
        None.

        '''
        random.shuffle(self.deck)
        
    def print_index(self,index):
        '''
        prints the nth tuple in the deck as indicated by index

        Parameters
        ----------
        index : integer
            accesses a specific tuple in the deck.

        Returns
        -------
        str
            prints the tuple.

        '''
        return f"{self.deck[index]}"
        
    def deal(self):
        '''
        pops the last tuple of the deck and returns it
        usage: cartita = Card(deck.deal())
 

        Returns
        -------
        TYPE tuple
            DESCRIPTION.

        '''
        return self.deck.pop()
    
    def cuantas(self):
        '''
        returns the number of cards left in the deck
        '''
        return f"quedan {len(self.deck)} cartas"


class Account():
    def __init__(self,owner,initial_balance=0):
        self.owner=owner
        self.balance=initial_balance
            
    def __str__(self):
        return f"Account Balance: ${self.balance}"
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"New balance = {self.balance}")
        
    def withdraw(self,amount):
        if self.balance-amount>=0:
            self.balance-=amount
            print(f"Bet accepted, new balance = ${self.balance}")
            return True
        else:
            print("Funds unavailable")
            return False
            
            
def ask_for_bet():
    result = input("What is your bet? (press enter for $100): ") or 100
    
    while True:
        try:
            result = int(result)
        except:
            print("Please enter a whole number")
            result = input("What is your bet? (press <Enter> for $100, 0 to exit): ") or 100
            continue
        else: #meaning there is no exception
            #print("You have enough balance, your bet is valid.")
            return result
            break

class MiniDeck():
    
    def __init__(self):
        self.minideck = []
        
    def __str__(self):
        return f"{self.minideck}"
    
    def anexa(self,cartopol):
        self.minideck.append(cartopol)

    def sumnum(self):
        total=0
        lista=[]
        for cartopol in self.minideck:
            num = cartopol[0]
            value = int(values[num])
            lista.append(value)
        total = sum(lista) 
        if total < 22:
            return total
        elif 11 in lista:
            #print('11 in lista')
            lista = []
            for cartopol in self.minideck:
                num = cartopol[0]
                value = int(values[num])
                #print(value)
                if value == 11:
                    value = 1
                lista.append(value)
            total = sum(lista)
            if total < 22:
                return total
            else:
                return -1
        else:
            return -1
        
    
    def printdeck(self,quien):
        self.quien = quien
        print(f"\n{self.quien} cards:")
        for cartopol in self.minideck:
            num = cartopol[0]
            palo = cartopol[1]
            print(f"- {num} of {palo}")
            
    def printcard(self,index):
        cartopol = self.minideck[index]
        num = cartopol[0]
        palo = cartopol[1]
        return f"{num} of {palo}"

if __name__ == "__main__":
    #%clear
    
    account = Account("player",1000) #create user 
    
    # print(account)
    # rico = False #ask for bet, check if player has enough money
    # while rico == False:
    #     bet = ask_for_bet()
    #     rico = account.withdraw(bet)
    # compudeck = MiniDeck()  #create computer's hand
    # playerdeck = MiniDeck()   #create player's hand
    # compudeck.anexa(deck.deal())  #deal comp one card
    # playerdeck.anexa(deck.deal())   #deal player one card
    # compudeck.anexa(deck.deal())   #deal compu one card
    # playerdeck.anexa(deck.deal())  #deal player one card
    # print(f"\nComputer cards:\n- [Covered]\n- {compudeck.printcard(1)}")  #print comp's 2nd card
    # playerdeck.printdeck("Player")
    bust = False
    flagint = False
    againb = True
    while againb == True:
        deck = Deck() #create deck
        deck.shuffle() #shuffle deck    
        print(account)
        rico = False #ask for bet, check if player has enough money
        while rico == False:
            bet = ask_for_bet()
            rico = account.withdraw(bet)
        compudeck = MiniDeck()  #create computer's hand
        playerdeck = MiniDeck()   #create player's hand
        compudeck.anexa(deck.deal())  #deal comp one card
        playerdeck.anexa(deck.deal())   #deal player one card
        compudeck.anexa(deck.deal())   #deal compu one card
        playerdeck.anexa(deck.deal())  #deal player one card
        print(f"\nComputer cards:\n- [Covered]\n- {compudeck.printcard(1)}")  #print comp's 2nd card
        playerdeck.printdeck("Player")
        bust = False
        flagint = False
        againb = True
        
        while bust == False:    
            while flagint == False:
                hors = input("Hit (h) or Stand (s)? ")
                hors = hors.capitalize()
                if hors == "H" or hors == "S":
                    break
            totalplayer = 0
            if hors == "H":
                playerdeck.anexa(deck.deal())
                playerdeck.printdeck("Player")
                totalplayer = playerdeck.sumnum()
                if totalplayer == -1:
                    print("BUST!")
                    bust = True
                    #break
            if hors == "S":
                totalplayer = playerdeck.sumnum()
                if totalplayer == -1:
                    print("BUST!")
                    print(account)
                    bust = True
                print("stand")
                break
        if bust == False:
            compubust = False
            while compubust == False:
                time.sleep(1)
                compudeck.printdeck("Computer")    
                print(totalplayer)
                totalcompu = compudeck.sumnum()
                if totalcompu == totalplayer:
                    print("Push")
                    account.deposit(bet)
                    break
                elif totalcompu == -1:
                    print("Player wins!")
                    account.deposit(bet+bet)
                    compubust = True
                elif totalcompu > totalplayer:
                    print("Computer wins")
                    print(account)
                    break
                else:
                    compudeck.anexa(deck.deal())
        if account.balance == 0:
            print("Your balance is zero, you've been kicked out of the casino")
            break
        again = input("Enter 'y' to play again: ")
        if again == "y":
            againb = True
            bust = False
        else: 
            print("Thank you, come again!")
            print(account)
            againb = False
                
                

                
        
        
            
            

    
    