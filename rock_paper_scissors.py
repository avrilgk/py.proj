import random 

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user==computer:
        return 'tie'
    

    if win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def win(player, opponent):
    # returns true if player wins 
    if (player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True