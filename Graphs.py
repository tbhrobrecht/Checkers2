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
show_all_graphs = True
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

plt.plot(game_number, win_rate, label="Win Rate")
# plt.plot([0, max(game_number)], [95, 95])
plt.scatter(bot_win_game_number, bot_wins, marker=".", alpha=0.5, label="Bot Victory")

# polynomial_regression = numpy.linspace(1, (q_learning_wins + random_bot_wins) * 1.01, 10)
polynomial_regression_model = numpy.poly1d(numpy.polyfit(game_number, win_rate, 1)) #deg 10
polynomial_regression = numpy.linspace(1, ai_total_victories + bot_total_victories, 10)
plt.plot(polynomial_regression, polynomial_regression_model(polynomial_regression), label="Linear Regression")
plt.title("Win Rate")
plt.xlabel("Game Number")
plt.ylabel("Win Rate")
plt.grid(True)
plt.savefig("winrate.png")
# plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

if show_all_graphs:
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
if show_all_graphs:
    plt.show()

qtable = pd.read_csv("5reset/Q_Table.csv")
# qtable_mean = qtable["Value"].mean()
# qtable_median = qtable["Value"].median()

#
# state_qtable = pd.read_csv("State_Q_Table.csv")
# state_qtable_mean = state_qtable["Value"].mean()
# state_qtable_median = state_qtable["Value"].median()
# # print(state_qtable_mean, state_qtable_median)
#
# # would be fun to create a graph that captures the relation between length of game and bot win
plt.scatter(game_number, number_of_moves, marker='.', alpha=0.1)
plt.title("Number of Moves")
# plt.hist2d(game_number, number_of_moves, bins=10)
if show_all_graphs:
    plt.show()
#
# print(np.average(number_of_moves))
# print(np.median(number_of_moves))

# long_game_and_bot_win = []
# for i in range(len(game_number)):
#     if list(number_of_moves)[i] >= 80 and list(bot_win)[i] == 100:
#         long_game_and_bot_win.append((game_number[i], number_of_moves[i]))
# long_game_and_bot_win = [178, 195, 250, 589, 812, 1567, 1654, 2132, 2235, 2518, 2779, 3401, 3755, 4133, 4138, 4506, 4916, 5013, 5146, 5388, 5388, 5517, 5638, 5915, 6431, 6440, 6440, 6691, 7453, 7907, 8626, 8659, 8738, 8805, 9400, 10047, 10596, 10923, 11699, 11877, 12528, 12712, 12712, 13006, 13024, 13462, 14720, 14891, 15229, 15229, 15301, 15320, 15770, 15772, 15772, 16643, 17028, 17486, 18412, 18463, 18705, 18894, 18894, 18993, 19152, 19250, 19332, 19350, 19471, 19591, 20478]
# long_game_and_bot_win = [(178, 201), (195, 87), (250, 96), (589, 132), (812, 201), (1567, 201), (1654, 201), (2132, 87), (2235, 124), (2518, 112), (2779, 105), (3401, 111), (3755, 102), (4133, 126), (4138, 121), (4506, 130), (4916, 201), (5013, 88), (5146, 201), (5388, 128), (5388, 201), (5517, 92), (5638, 201), (5915, 113), (6431, 98), (6440, 95), (6440, 201), (6691, 116), (7453, 84), (7907, 86), (8626, 80), (8659, 89), (8738, 92), (8805, 95), (9400, 201), (10047, 115), (10596, 113), (10923, 86), (11699, 101), (11877, 90), (12528, 84), (12712, 201), (12712, 201), (13006, 201), (13024, 201), (13462, 201), (14720, 201), (14891, 99), (15229, 99), (15229, 201), (15301, 86), (15320, 159), (15770, 101), (15772, 88), (15772, 201), (16643, 108), (17028, 81), (17486, 105), (18412, 201), (18463, 100), (18705, 87), (18894, 201), (18894, 201), (18993, 201), (19152, 106), (19250, 92), (19332, 82), (19350, 131), (19471, 201), (19591, 201), (20478, 201)]
# new_long_list = []
# for i in range(len(long_game_and_bot_win)):
#     if long_game_and_bot_win[i][1] != 201:
#         new_long_list.append(long_game_and_bot_win[i][1])
# new_long_list = [(195, 87), (250, 96), (589, 132), (2132, 87), (2235, 124), (2518, 112), (2779, 105), (3401, 111), (3755, 102), (4133, 126), (4138, 121), (4506, 130), (5013, 88), (5388, 128), (5517, 92), (5915, 113), (6431, 98), (6440, 95), (6691, 116), (7453, 84), (7907, 86), (8626, 80), (8659, 89), (8738, 92), (8805, 95), (10047, 115), (10596, 113), (10923, 86), (11699, 101), (11877, 90), (12528, 84), (14891, 99), (15229, 99), (15301, 86), (15320, 159), (15770, 101), (15772, 88), (16643, 108), (17028, 81), (17486, 105), (18463, 100), (18705, 87), (19152, 106), (19250, 92), (19332, 82), (19350, 131)]
# print(new_long_list)
# new_long_list = [87, 96, 132, 87, 124, 112, 105, 111, 102, 126, 121, 130, 88, 128, 92, 113, 98, 95, 116, 84, 86, 80, 89, 92, 95, 115, 113, 86, 101, 90, 84, 99, 99, 86, 159, 101, 88, 108, 81, 105, 100, 87, 106, 92, 82, 131]
# new_long_list_x = np.linspace(0, len(new_long_list), len(new_long_list))
# plt.scatter(new_long_list_x, new_long_list)
# plt.show()
# print(bot_total_victories)
bot_victory_list = []
bot_victory_list_x = []
ai_victory_list = []
ai_victory_list_x = []
# print(len(game_number))
# print(len(bot_total_victories))
# print(bot_total_victories)
# print(bot_victory_list)

for i in range(len(game_number)):
    if bot_win[i] == 100 and number_of_moves[i] < 200:
        bot_victory_list.append(number_of_moves[i])
        bot_victory_list_x.append(game_number[i])
    if bot_win[i] != 100 and number_of_moves[i] < 200:
        ai_victory_list.append(number_of_moves[i])
        ai_victory_list_x.append(game_number[i])
# bot_victory_list_x = np.linspace(0, len(bot_victory_list), len(bot_victory_list))
# ai_victory_list_x = np.linspace(0, len(ai_victory_list), len(ai_victory_list))
plt.scatter(ai_victory_list_x, ai_victory_list, marker=".", alpha=0.1, label="AI Victory")
plt.scatter(bot_victory_list_x, bot_victory_list, marker=".", alpha=1, label="Bot Victory")
print(np.average(ai_victory_list))
print(np.average(bot_victory_list))
plt.ylabel("Moves")
plt.xlabel("Episode (Game) Number")
plt.title("Moves Taken Until A Win")
polynomial_regression_model = numpy.poly1d(numpy.polyfit(ai_victory_list_x, ai_victory_list, 1)) #deg 10
polynomial_regression = numpy.linspace(1, ai_victory_list_x, 10)
plt.plot(polynomial_regression, polynomial_regression_model(polynomial_regression), color='black', label="AI Linear Regression Model")
polynomial_regression_model = numpy.poly1d(numpy.polyfit(bot_victory_list_x, bot_victory_list, 1)) #deg 10
polynomial_regression = numpy.linspace(1, bot_victory_list_x, 10)
plt.plot(polynomial_regression, polynomial_regression_model(polynomial_regression), color='brown', label="Bot Linear Regression Model")
# plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.savefig("Moves Taken Until A Win")

if show_all_graphs:
    plt.show()
print()
print(np.average(ai_victory_list))
print(np.median(ai_victory_list))
print(np.average(bot_victory_list))
print(np.median(bot_victory_list))

plt.boxplot([ai_victory_list, bot_victory_list])
plt.plot([1,2], [25,25])
plt.show()


df = pd.read_csv("Bot_State_Q_Table.csv")
# Piece,Current State,Current Action,Value

# print(len(df))
keys = []
values = []
for i in range(len(df)):
    # key = str(df["Piece"][i]) + "," + str(df["Current State"][i]) + "," + str(df["Current Action"][i])
    key = i
    keys.append(key)
    values.append(df["Value"][i])
print(keys)
print(values)
plt.scatter(keys, values, marker=".", alpha=0.1)
plt.show()

