nintendo_games = ["Zelda", "Mario","Donkey Kong", "Zelda"]
print(nintendo_games)

nintendo_games.remove("Zelda")
print(nintendo_games)

nintendo_games.remove("Zelda")
print(nintendo_games)

# nintendo_games.remove("Wario")
# ValueError: list.remove(x): x not in list
# print(nintendo_games)

if "Mario" in nintendo_games:
    nintendo_games.remove("Mario")
    
print(nintendo_games)