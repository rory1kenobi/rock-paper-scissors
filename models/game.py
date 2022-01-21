

class Game():

    def __init__(self):
        self.the_winner = {
            "scissors": "paper", 
            "paper": "rock",
            "rock": "scissors"
        }

    def play(self, player_1, player_2):

        winner = None

        if self.the_winner[player_1.choice.lower()] == player_2.choice.lower():
            
            winner = player_1
        elif self.the_winner[player_2.choice.lower()] == player_1.choice.lower():
            winner = player_2
        
        return winner

        # if player_1.choice == player_2.choice:
        #     return "both players are of equal power"
        # elif player_1.choice == "rock" and player_2.choice == "scissors":
        #     return f"{player_2.name}'s power is no match for the almighty {player_1.name.capitalize()}!"
        # elif player_1.choice == "scissors" and player_2.choice == "paper":
        #     return f"{player_2.name}'s power is no match for the almighty {player_1.name.capitalize()}!"
        # elif player_1.choice == "paper" and player_2.choice == "rock":
        #     return f"{player_2.name}'s power is no match for the almighty {player_1.name.capitalize()}!"
        # else:
        #     return f"{player_1.name}'s power is no match for the almighty {player_2.name.caitalize()}!"
        