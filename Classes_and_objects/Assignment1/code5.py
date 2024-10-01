class Cricket:
    def __init__(self, team_name,player_name,role):
        self.team_name = team_name
        self.player_name = player_name
        self.role = role
    
    def team_info(self):
        print("Team: ", self.team_name)
        print("player : ",self.player_name)
        print("role : ",self.role)

team = Cricket("India","virat","Batsman")
team.team_info()
