import game as g
import time

g.initPlayers()
print("Game Start!")

time.sleep(1)

player = g.createNewPlayer("Fortwikszz", 7, 4)
g.addPlayer(player)
print(f"{player["name"]} joined the game!")

player = g.createNewPlayer("Lolimancer", 8, 2)
g.addPlayer(player)
print(f"{player["name"]} joined the game!")

player = g.createNewPlayer("MilfSlayer", 5, 7)
g.addPlayer(player)
print(f"{player["name"]} joined the game!")

player = g.createNewPlayer("FemboyMatingPress", 9, 1)
g.addPlayer(player)
print(f"{player["name"]} joined the game!")

time.sleep(3)
print()

g.setPlayer(g.PlayerList[0], "Defense", True)
print(f"{g.PlayerList[0]["name"]} activate Defense")

time.sleep(1)
print()

g.setPlayer(g.PlayerList[2], "Defense", True)
print(f"{g.PlayerList[2]["name"]} activate Defense")

time.sleep(1)
print()

g.attackPlayer(g.PlayerList[1], g.PlayerList[0])
print(f"{g.PlayerList[1]["name"]} attacks {g.PlayerList[0]["name"]}")
print(f"{g.PlayerList[0]["name"]} recieve {g.PlayerList[0]["damage"]} damage")

g.displayMatchResult()