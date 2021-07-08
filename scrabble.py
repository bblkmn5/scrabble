#Process data from a group of friends playing scrabble, using dictionairies to organize players, words, and points.
letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
    "U", "V", "W", "X", "Y", "Z"
    ]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#combine two lists into dictionary
letter_to_points = {letter:point for letter, point in zip(letters, points)}
# print(letter_to_points)

#add blank tile to dictionary
letter_to_points[" "] = 0
# print(letter_to_points)

#function to determine score of a word by getting value of each letter in word and returning total value 
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")

#create test players with played words
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

#use score_word() to find how points each player has
player_to_points = {}

#create update_point_totals() for game continuation
def update_point_totals():
    for players, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
            player_to_points[players] = words
        print(str(players) + " has " + str(player_points) + " points.")

#create play_word() to update player-played words and point totals
def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        print("That player does not exist")
        quit
    update_point_totals()

play_word("player1", "CODE")
play_word("player2", "BOOKSHELF")
print(player_to_words)
