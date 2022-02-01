# All the Regex patterns to find the chess data

# Regex pattern to find the start of each game
game_start = "\[Event"
# Regex pattern to find all data for Site
Site = "(?<=\[Site \").*(?=\"\])"
# Regex pattern to find all data for Date
Date = "(?<=\[Date \").*(?=\"\])"
# Regex pattern to find all data for Round
Round = "(?<=\[Round \").*(?=\"\])"
# Regex pattern to find all data for White
White = "(?<=\[White \").*(?=\"\])"
# Regex pattern to find all data for Black
Black = "(?<=\[Black \").*(?=\"\])"
# Regex pattern to find all data for Result
Result = "(?<=\[Result \").*(?=\"\])"
# Regex pattern to find all data for ECO
Eco = "(?<=\[ECO \").*(?=\"\])"
# Regex pattern to find all data for ECOUrl
ECOUrl = "(?<=\[ECOUrl \").*(?=\"\])"
# Regex pattern to find all data for WhiteElo
WhiteElo = "(?<=\[WhiteElo \").*(?=\"\])"
# Regex pattern to find all data for BlackElo
BlackElo = "(?<=\[BlackElo \").*(?=\"\])"
# Regex pattern to find all data for TimeControl
TimeControl = "(?<=\[TimeControl \").*(?=\"\])"
# Regex pattern to find all data for Termination
Termination = "(?<=\[Termination \").*(?=\"\])"
# Regex pattern to find all data for StartTime
StartTime = "(?<=\[StartTime \").*(?=\"\])"
# Regex pattern to find all data for EndDate
EndDate = "(?<=\[EndDate \").*(?=\"\])"
# Regex pattern to find all data for EndTime
EndTime = "(?<=\[EndTime \").*(?=\"\])"
# Regex pattern to find all data for Link
Link = "(?<=\[Link \").*(?=\"\])"
# Regex pattern to find all data for Moves
Move ='(?<=\s)[a-hKQRBNP][a-hx1-8]{0,4}[1-8][#+=]?[KQRBNP]?[#+]?(?=\s)|(?<=\s)O-O-O[#+]?(?=\s)|(?<=\s)O-O[#+]?(?=\s)'
# Regex pattern to find all data for Times
move_Time = "(?<=\[%clk\s)\d\:\d\d\:\d\d"