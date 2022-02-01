# Script to parse PGN files from Chess.com or Lichess

import csv
import functions

# Enter the name of the pgn file to parse. Make sure it is in the same directory as the Parser.
file = 'file_name'
file = "chess_files/lichess_dorfys_2022-01-05.pgn"


# Reads the file and assigns to the varaible 'text'
with open(file) as f:
   text = f.read() 

# Functions that breaks the text into seperate games
all_games = functions.find_games(text)

# Function that finds the longest game
longest_game = functions.find_longest_game(all_games)

# Function that creates the CSV headers
full_headers = functions.create_headers(longest_game)

# Function that finds all the info for each game
all_parsed_games = functions.game_parser(all_games,longest_game)


# Takes the parsed games and creates a new file with each game on a new row
with open('parsed_chess_games.csv', 'w', newline='') as file:
    # Manually adds the headers
    writer = csv.writer(file)
    writer.writerow(full_headers)
    for x in range(len(all_parsed_games)):
        writer.writerow(all_parsed_games[x])
    print("The parsed file was downloaded successfully!")
