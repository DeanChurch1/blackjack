import random
import cards

def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response


def ask_number(question,low,high):
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response


def switch_turn(num_players,turn):
    while True:
        turn + 1
        if turn == 4:
            turn = 1
            break
    return turn


def roll(self):
        die1 = random.randint(1, 6)
        print("you rolled a",die1)
        roll = die1
        return roll


def welcome(title):
    print("\t\tWelcome to the game\n")
    print("\t\t",title,"\n")

def add_to_score(score,points):
    new_score = score
    score += points
    return new_score

class Player(object):
    def __init__(self,name,score=0):
        self.name = name
        self.score = score
    
    def __str__(self):
        rep = self.name
        rep = rep +" "+str(self.score)
        return rep



if __name__=="__main__":
    print("You ran this module directly and did not import it")
    input("\n\npress enter key to exit")
    
















    
