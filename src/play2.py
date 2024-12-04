import game as g
import random

g.initPlayers()
print("Game Start!")

jmlh_player = int(input("How many player will play? : "))
for i in range(jmlh_player):
    player = g.createNewPlayer(input("Player name : "), int(input("Player damage : ")), int(input("Player defense power : ")))
    g.addPlayer(player)
    print(f"{player['name']} joined the game!")

#Pertandingan dimulai per jumlah ronde
jmlh_ronde = int(input("How many round will play? : "))
for i in range(jmlh_ronde):
    print(f"Round {i+1}")
    random.shuffle(g.PlayerList)
    for player in g.PlayerList:
        if player["health"] <= 0:  # Skip players who are out of health
            print(f"{player['name']} is out of health and will be eleminated.")
            g.removePlayer(player['name'])
            continue
        if len(g.PlayerList) > 1:
            print(f"\nNow it is {player['name']}'s turn!")
            action = input("What do you want to do? (attack (a) /defense (d)): ")

            if action == "attack" or action == "a":
                print("Choose your target:")
                # Display list of potential targets
                for idx, target in enumerate(g.PlayerList):
                    if target["name"] != player["name"] and target["health"] > 0:  # Exclude self and dead players
                        print(f"{idx}. {target['name']} (Health: {target['health']})")

                try:
                    # Input target index
                    target_idx = int(input("Enter the number of the target: "))
                    # Validate target index
                    if target_idx < 0 or target_idx >= len(g.PlayerList) or g.PlayerList[target_idx]["name"] == player["name"] or g.PlayerList[target_idx]["health"] <= 0:
                        print("Invalid target! You lose your turn.")
                    else:
                        target = g.PlayerList[target_idx]
                        print(f"{player['name']} attacks {target['name']}!")
                        g.attackPlayer(player, target)
                except ValueError:
                    print("Invalid input! You lose your turn.")

            elif action == "defense" or action == "d":
                print(f"{player['name']} goes into defense mode!")
                g.setPlayer(player, "defense", True)

            else:
                print("Invalid action! You lose your turn.")
        else:
            # End of game
            print("\n--- Game Over! ---")
            g.displayMatchResult()


 # End of game
print("\n--- Game Over! ---")
g.displayMatchResult()
