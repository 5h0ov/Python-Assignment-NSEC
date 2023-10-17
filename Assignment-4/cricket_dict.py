team = {}

n = int(input("Enter the number of players: "))

for i in range(n):
    name = input("Enter player's name: ")
    runs = int(input("Enter runs scored by {}: ".format(name)))
    team[name] = runs

player = input("Enter the player's name to get runs scored: ")

if player in team:
    print("\nPlayer {} has scored {} runs.".format(player, team[player]))
else:
    print("\nPlayer {} is not found in the team.".format(player))
