# Checkers2
assem &amp; i 


# Set Up 
In the beginning, be sure to have everything regarding the neural network model commented out 
set nn_endgame to False 

the following code block resets both q tables:

with open("Q_Table.csv", mode="w", newline="") as file:
writer = csv.writer(file)
writer.writerow(["Piece", "Board", "Current State", "Current Action", "Value"])

with open("State_Q_Table.csv", mode="w", newline="") as file:
writer = csv.writer(file)
writer.writerow(["Piece", "Current State", "Current Action", "Value"])

the following code block resets the win rates:

with open("winrate.csv", mode="w", newline="") as file:
writer = csv.writer(file)
writer.writerow(["Game Number","AI Total Victories","Bot Total Victories","Win Rate","Bot Won"])