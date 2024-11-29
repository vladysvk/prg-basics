computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]


n = 1
computer_games = sorted(computer_games)

while n <= len(computer_games):
    print(f"{n}.{computer_games[n - 1]}")
    n += 1