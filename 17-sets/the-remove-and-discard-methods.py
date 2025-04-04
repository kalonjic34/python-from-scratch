agents  = {"Mulder","Scully","Doggett","Rayes"}

# agents.remove("Doggett")
# print(agents)

# agents.remove("Skinner") #KeyError: 'Skinner'

agents.discard("Doggett")
print(agents)

agents.discard("Skinner")
print(agents)