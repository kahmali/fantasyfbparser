import os
from string import digits

# Get the path to the file we want to parse
filename = input("Enter path to file to be parsed: ")
file = open(filename)
file_contents = file.read()
file.close()

# Get the name or path to the desired output file
output_filename = input("Enter name (or path) of output file: ")

# Create a list of players, their rank, and position
players = []
for line in file_contents.splitlines():
    words = line.split()
    player_name = " ".join(words[1:-4]).strip(",")
    # Remove the numbers from the position rank (so we're just left with the pos)
    player_position = words[-2].strip(digits)
    player_rank = words[0]
    players.append((player_rank, player_name, player_position))

# Create a csv file with Player Name, Player Position
csv_file = open(output_filename, "a+")
csv_file.write("Rank,Player Name,Position\n")
for rank, player, pos in players:
    csv_file.write(",".join([rank, player, pos]) + "\n")





