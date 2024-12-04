def initPlayers():
    global PlayerList
    PlayerList = []
    return

def createNewPlayer(name, damage=0, defensePower=0):
    player = dict(name = name,
                  score = 0,
                  damage = damage,
                  health = 100,
                  defensePower = defensePower,
                  defense = bool(False)
                  )
    return player

def addPlayer(player):
    global PlayerList
    PlayerList += [player]
    return

def removePlayer(name):
    global PlayerList
    for i in range(len(PlayerList)):
        if PlayerList[i]["name"] == name:
            PlayerList.pop(i)
            return
    print("There is no player with that name!")
    return

def setPlayer(player:dict, key:str, value:int):
    player[key] = value
    return
        
def attackPlayer(attacker:dict, target:dict):
    if target["defense"] == False:
        setPlayer(target, "health", target["health"]-attacker["damage"])
        setPlayer(attacker, "score", attacker["score"] + 1)
    else:
        setPlayer(target, "health", target["health"]-attacker["damage"]+target["defensePower"] if target["defensePower"] <= attacker["damage"] else target["health"])
        setPlayer(attacker, "score", attacker["score"] + 0.8)
        setPlayer(target, "defense", False)
    return
                    
def displayMatchResult():
    display = PlayerList
    for i in range(len(display)):
        for j in range(len(display)):
            if PlayerList[i]["score"] > PlayerList[j]["score"] or PlayerList[i]["health"] > PlayerList[j]["health"]:
                temp = display[i]
                display[i] = display[j]
                display[j] = temp
                
    for i in range(len(display)):
        print(f"Rank {i+1}: {display[i]['name']} | Score: {display[i]['score']} | Health: {display[i]['health']}")
    
    return