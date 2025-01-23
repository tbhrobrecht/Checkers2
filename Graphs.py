import random

import matplotlib.pyplot as plt
import numpy
import numpy as np
import pandas as pd
#
# df = pd.read_csv("winrate.csv")
#
# game_number = df["Game Number"]
# win_rate = df["Win Rate"]
# bot_win = df["Bot Won"]
# bot_win_indices = df["Bot Won"] > 0
# bot_win_game_number = game_number[bot_win_indices]
# bot_wins = df["Bot Won"][bot_win_indices]
#
# plt.plot(game_number, win_rate)
# plt.scatter(bot_win_game_number, bot_wins)
#
# # mymodel = numpy.poly1d(numpy.polyfit(game_number, win_rate, 10))
# # myline = numpy.linspace(1, 542, 10)
# # plt.plot(myline, mymodel(myline))
#
# df = pd.read_csv("winrate.csv")
#
# game_number = df["Game Number"]
# win_rate = df["Win Rate"]
# bot_win = df["Bot Won"]
# bot_win_indices = df["Bot Won"] > 0
# bot_win_game_number = game_number[bot_win_indices]
# bot_wins = df["Bot Won"][bot_win_indices]
#
# plt.plot(game_number, win_rate)
# plt.scatter(bot_win_game_number, bot_wins)
#
# polynomial_regression_model = numpy.poly1d(numpy.polyfit(game_number, win_rate, 1))
# polynomial_regression = numpy.linspace(1, 20, 10)
# plt.plot(polynomial_regression, polynomial_regression_model(polynomial_regression))
#
#
# plt.show()
#

import os
import csv

# print(os.path.getsize("Q_Table.csv"))
# print(os.path.getsize("State_Q_Table.csv"))
#
# with open("Q_Table.csv", mode="w", newline="") as file:
#     writer = csv.writer(file)
#     # Piece,Board,Current State,Current Action,Value
#     writer.writerow(["Piece", "Board", "Current State", "Current Action", "Value"])
#
# with open("State_Q_Table.csv", mode="w", newline="") as file:
#     writer = csv.writer(file)
#     # Piece,Current State,Current Action,Value
#     writer.writerow(["Piece", "Current State", "Current Action", "Value"])
#
# print(os.path.getsize("Q_Table.csv"))
# print(os.path.getsize("State_Q_Table.csv"))
#
# print(os.path.getsize("winrate.csv"))
#
# for i in range(0, 100):
#     if i % 10 == 0:
#         print(i)


# def get_last():
#     if os.path.getsize("winrate.csv") < 30:
#         return 0  # File doesn't exist, start from game 0
#     with open("winrate.csv", mode="r", newline="") as file:
#         reader = csv.reader(file)
#         next(reader, None)  # Skip the header row
#         rows = list(reader)  # Read all rows
#         if not rows:
#             return 0  # No data rows, start from game 0
#         # return int(rows[-1][0])
#         return (rows[-1][0], rows[-1][1], rows[-1][2])
#
# print(get_last())

# print(os.path.getsize("winrate.csv"))


# df = pd.read_csv("winrate.csv")
#
# game_number = df["Game Number"]
# win_rate = df["Win Rate"]
# bot_win = df["Bot Won"]
# bot_win_indices = df["Bot Won"] > 0
# bot_win_game_number = game_number[bot_win_indices]
# bot_wins = df["Bot Won"][bot_win_indices]
# ai_total_victories = df["AI Total Victories"]
# bot_total_victories = df["Bot Total Victories"]
#
# print(game_number)
# print(win_rate)
# print(bot_win)
#
# plt.plot(game_number, win_rate)
# plt.show()

# polynomial_regression_model = numpy.poly1d(numpy.polyfit(game_number, win_rate, 1)) #deg 10
# polynomial_regression = numpy.linspace(1, (ai_total_victories + bot_total_victories) * 1.01, 10)
# plt.plot(polynomial_regression, polynomial_regression_model(polynomial_regression))

# plt.show()

df = pd.read_csv("winrate.csv")

game_number = df["Game Number"]
win_rate = df["Win Rate"]
bot_win = df["Bot Won"]
ai_total_victories = df["AI Total Victories"]
bot_total_victories = df["Bot Total Victories"]

number_of_moves = df["Moves"]

bot_win_indices = df["Bot Won"] > 0
bot_win_game_number = game_number[bot_win_indices]
bot_wins = df["Bot Won"][bot_win_indices]

plt.plot(game_number, win_rate)
# plt.plot([0, max(game_number)], [95, 95])
plt.scatter(bot_win_game_number, bot_wins, marker=".", alpha=0.5)

# polynomial_regression = numpy.linspace(1, (q_learning_wins + random_bot_wins) * 1.01, 10)
polynomial_regression_model = numpy.poly1d(numpy.polyfit(game_number, win_rate, 1)) #deg 10
polynomial_regression = numpy.linspace(1, ai_total_victories + bot_total_victories, 10)
plt.plot(polynomial_regression, polynomial_regression_model(polynomial_regression))
plt.title("Win Rate")
plt.grid(True)
plt.show()


win_streak = []
# print(len(bot_win_game_number))
# print(list(bot_win_game_number))
bot_win_game_number_list = list(bot_win_game_number)
# print(bot_win_game_number_list)
for i in range(len(bot_win_game_number_list)):
    if i + 1 < len(bot_win_game_number_list):
        if bot_win_game_number_list[i] == 1:
            win_streak.append(0)
        # print(bot_win_game_number_list[i])
        win_streak.append(bot_win_game_number_list[i + 1] - bot_win_game_number_list[i] - 1)
    else:
        # print(bot_win_game_number_list[i], "last")
        win_streak.append(max(game_number) - bot_win_game_number_list[i])
# print(win_streak)
if bot_win_game_number_list[0] == 1:
    bot_win_game_number_x = np.linspace(1, len(bot_win_game_number_list) + 1, len(bot_win_game_number_list) + 1)
else:
    bot_win_game_number_x = np.linspace(1, len(bot_win_game_number_list), len(bot_win_game_number_list))

plt.plot(bot_win_game_number_x, win_streak, alpha=0.2)
plt.scatter(bot_win_game_number_x, win_streak, color='orange', marker='.', alpha=0.5)
plt.title("win streak")
polynomial_regression_model = numpy.poly1d(numpy.polyfit(bot_win_game_number_x, win_streak, 1)) #deg 10
polynomial_regression = numpy.linspace(1, bot_win_game_number_x, 10)
plt.plot(polynomial_regression, polynomial_regression_model(polynomial_regression))

plt.grid(True)
plt.show()

qtable = pd.read_csv("Q_Table.csv")
qtable_mean = qtable["Value"].mean()
qtable_median = qtable["Value"].median()
print(qtable_mean, qtable_median)

state_qtable = pd.read_csv("State_Q_Table.csv")
state_qtable_mean = state_qtable["Value"].mean()
state_qtable_median = state_qtable["Value"].median()
# print(state_qtable_mean, state_qtable_median)

# would be fun to create a graph that captures the relation between length of game and bot win
plt.scatter(game_number, number_of_moves, marker='.', alpha=0.1)
plt.title("Number of Moves")
# plt.hist2d(game_number, number_of_moves, bins=10)
plt.show()

