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
