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

g.setPlayer(g.PlayerList[0], "defense", True)
print(f"{g.PlayerList[0]["name"]} activate Defense")

time.sleep(1)
print()

g.setPlayer(g.PlayerList[2], "defense", True)
print(f"{g.PlayerList[2]["name"]} activate Defense")

time.sleep(1)
print()

print(f"{g.PlayerList[1]["name"]} attacks {g.PlayerList[0]["name"]}")
print(f"{g.PlayerList[0]["name"]} recieves {g.PlayerList[1]["damage"] if g.PlayerList[0]["defense"] == False else (g.PlayerList[1]["damage"]-g.PlayerList[0]["defensePower"])} damage")
g.attackPlayer(g.PlayerList[1], g.PlayerList[0])

time.sleep(1)
print()

print(f"{g.PlayerList[0]["name"]} attacks {g.PlayerList[3]["name"]}")
print(f"{g.PlayerList[3]["name"]} recieves {g.PlayerList[0]["damage"] if g.PlayerList[3]["defense"] == False else g.PlayerList[0]["damage"]-g.PlayerList[3]["defensePower"]} damage")
g.attackPlayer(g.PlayerList[0], g.PlayerList[3])

time.sleep(1)
print()

print(f"{g.PlayerList[2]["name"]} has disconnected...")
g.removePlayer(g.PlayerList[2]["name"])

time.sleep(1)
print()

print(f"{g.PlayerList[1]["name"]} attacks {g.PlayerList[0]["name"]}")
print(f"{g.PlayerList[0]["name"]} recieves {g.PlayerList[1]["damage"] if g.PlayerList[0]["defense"] == False else g.PlayerList[1]["damage"]-g.PlayerList[0]["defensePower"]} damage")
g.attackPlayer(g.PlayerList[1], g.PlayerList[0])

time.sleep(1)
print()

print(f"{g.PlayerList[0]["name"]} attacks {g.PlayerList[1]["name"]}")
print(f"{g.PlayerList[1]["name"]} recieves {g.PlayerList[0]["damage"] if g.PlayerList[1]["defense"] == False else g.PlayerList[0]["damage"]-g.PlayerList[1]["defensePower"]} damage")
g.attackPlayer(g.PlayerList[0], g.PlayerList[1])

time.sleep(1)
print()

g.setPlayer(g.PlayerList[0], "defense", True)
print(f"{g.PlayerList[0]["name"]} activate Defense")

time.sleep(1)
print()

print(f"{g.PlayerList[0]["name"]} attacks {g.PlayerList[2]["name"]}")
print(f"{g.PlayerList[2]["name"]} recieves {g.PlayerList[0]["damage"] if g.PlayerList[2]["defense"] == True else g.PlayerList[0]["damage"]-g.PlayerList[2]["defensePower"]} damage")
g.attackPlayer(g.PlayerList[0], g.PlayerList[2])

time.sleep(1)
print()

print("Game Ended!")
g.displayMatchResult()