class IPLPlayer:
    total_players = 0  
    def __init__(self, name, team): 
        self.name = name  
        self.team = team  
        IPLPlayer.total_players += 1

    def player_info(self): 
        return f"{self.name} plays for {self.team}."

name = input("Enter player name: ")
team = input("Enter team name: ")

player = IPLPlayer(name, team)
print(player.player_info())  # Output example: Virat Kohli plays for RCB.

