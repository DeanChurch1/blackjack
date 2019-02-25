import random
import cards

#Could be important if you need to ask questions
def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

#You will ask a number and it will return it. Will be useful to ask how many players you want.
def ask_number(question,low,high):
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response

#Will switch turn when players have finished their own turn.
def switch_turn(num_players,turn):
    while True:
        turn + 1
        if turn == 4:
            turn = 1
            break
    return turn

#Could be helpful to decide the order players go in. Or players in a boardgame.
def roll(self):
        die1 = random.randint(1, 6)
        print("you rolled a",die1)
        roll = die1
        return roll

#Will welcome them to the game.
def welcome(title):
    print("\t\tWelcome to the game\n")
    print("\t\t",title,"\n")

#Will keep the score and help players add to their score.
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
    
















    
