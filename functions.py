import re
import patterns


# Function to find a block of text for each game
def find_games(text):
    games_start_at = []
    games_list = []
    for match in re.finditer(patterns.game_start,text):
        games_start_at.append(match.start())
    games_start_at.append(len(text))
    for x in range(((len(games_start_at)-1))):
        games_list.append(text[games_start_at[x]:games_start_at[x + 1]])
    return games_list

 # Funciton to find the longest game   
def find_longest_game(games_list):
    longest_game = 0
    for game in games_list:
        game_length = len(re.findall(patterns.Move,game))
        if game_length > longest_game:
            longest_game = game_length
    return (longest_game)

# function to create our CSV headers
def create_headers(longest_game):
    headers = ['Site','Date', 'Round', 'White', 'Black', 'Result', 'ECO', 'ECOUrl', 'WhiteElo', 'BlackElo', 'TimeControl', 'Termination', 'StartTime', 'EndDate', 'EndTime', 'Link']
    #max_game = find_longest_game(games_list)
    max_game = longest_game
    for i in range(max_game):
        headers.append('Move_ply_' + str(i + 1))
    for i in range(max_game + 1):
        headers.append('Clock_ply_' + str(i + 1))
    return headers


# function to look through each game and add each item to a list
def game_parser(games_list,longest_game):
    max_game = longest_game
    parsed_games = []
    for index, game in enumerate(games_list):
        game_items = []
        # Find all the data for Date
        if re.search(patterns.Site,game):
            game_items.append(re.search(patterns.Site,game).group())
        else:
            game_items.append('NA')
        # Find all the data for Date
        if re.search(patterns.Date,game):
            game_items.append(re.search(patterns.Date,game).group())
        else:
            game_items.append('NA')
        # Find all the data for Rounds
        if re.search(patterns.Round,game):
            game_items.append(re.search(patterns.Round,game).group())
        else:
            game_items.append('NA')
        # Find all the data for White
        if re.search(patterns.White,game):
            White = re.search(patterns.White,game).group()
            game_items.append(White)
        else:
            game_items.append('NA')
        # Find all the data for Black
        if re.search(patterns.Black,game):
            Black = re.search(patterns.Black,game).group()
            game_items.append(Black)
        else:
            game_items.append('NA')
        # Find all the data for Result
        if re.search(patterns.Result,game):
            game_items.append(re.search(patterns.Result,game).group())
        else:
            game_items.append('NA')
        # Find all the data for ECO
        if re.search(patterns.Eco,game):
            game_items.append(re.search(patterns.Eco,game).group())
        else:
            game_items.append('NA')
        # Find all the data for ECOUrl
        if re.search(patterns.ECOUrl,game):
            game_items.append(re.search(patterns.ECOUrl,game).group())
        else:
            game_items.append('NA')
        # Find all the data for WhiteElo
        if re.search(patterns.WhiteElo,game):
            game_items.append(re.search(patterns.WhiteElo,game).group())
        else:
            game_items.append('NA')
        # Find all the data for BlackElo
        if re.search(patterns.BlackElo,game):
            game_items.append(re.search(patterns.BlackElo,game).group())
        else:
            game_items.append('NA')
        # Find all the data for TimeControl
        if re.search(patterns.TimeControl,game):
            game_items.append(re.search(patterns.TimeControl,game).group())
        else:
            game_items.append('NA')
        # Find all the data for Termination
        if re.search(patterns.Termination,game):
            game_items.append(re.search(patterns.Termination,game).group())
        else:
            game_items.append('NA')
        # Find all the data for StartTime
        if re.search(patterns.StartTime,game):
            game_items.append(re.search(patterns.StartTime,game).group())
        else:
            game_items.append('NA')
        # Find all the data for EndDate
        if re.search(patterns.EndDate,game):
            game_items.append(re.search(patterns.EndDate,game).group())
        else:
            game_items.append('NA')
        # Find all the data for EndTime
        if re.search(patterns.EndTime,game):
            game_items.append(re.search(patterns.EndTime,game).group())
        else:
            game_items.append('NA')
        # Find all the data for Link
        if re.search(patterns.Link,game):
            game_items.append(re.search(patterns.Link,game).group())
        else:
            game_items.append('NA')
        # Find all the data for Moves
        for match in re.finditer(patterns.Move,game):
                game_items.append(match.group())
        #Fill all the empty spaces for missing moves
        num_empty_spaces = (max_game + 16)-len(game_items)
        game_items.extend(['NA']*num_empty_spaces)
        #Find all the data for Time move was made at
        for match in re.finditer(patterns.move_Time,game):
            game_items.append(match.group())
        #Fill all the empty spaces for move_times
        num_empty_spaces = (2*max_game + 17)-len(game_items)
        game_items.extend(['NA']*num_empty_spaces)

        # Add all the game items as a single game to my list called parsed_games
        parsed_games.append(game_items)

    return parsed_games

