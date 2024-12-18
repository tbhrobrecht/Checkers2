import matplotlib.pyplot as plt
import numpy
import pandas as pd

df = pd.read_csv("winrate.csv")

game_number = df["Game Number"]
win_rate = df["Win Rate"]
bot_win = df["Bot Won"]
bot_win_indices = df["Bot Won"] > 0
bot_win_game_number = game_number[bot_win_indices]
bot_wins = df["Bot Won"][bot_win_indices]

plt.plot(game_number, win_rate)
plt.scatter(bot_win_game_number, bot_wins)

# mymodel = numpy.poly1d(numpy.polyfit(game_number, win_rate, 10))
# myline = numpy.linspace(1, 542, 10)
# plt.plot(myline, mymodel(myline))

df = pd.read_csv("winrate.csv")

game_number = df["Game Number"]
win_rate = df["Win Rate"]
bot_win = df["Bot Won"]
bot_win_indices = df["Bot Won"] > 0
bot_win_game_number = game_number[bot_win_indices]
bot_wins = df["Bot Won"][bot_win_indices]

plt.plot(game_number, win_rate)
plt.scatter(bot_win_game_number, bot_wins)

polynomial_regression_model = numpy.poly1d(numpy.polyfit(game_number, win_rate, 10))
polynomial_regression = numpy.linspace(1, 130, 10)
plt.plot(polynomial_regression, polynomial_regression_model(polynomial_regression))


plt.show()

