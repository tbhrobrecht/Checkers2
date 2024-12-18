import csv
import os
import random
import pygame
import torch
# from DQN import QNetwork, ReplayMemory
from GameLogic import CheckMove
from UserInterface import UserInterface
from QLearningAgent import QLearningAgent
from State_QLearningAgent import State_QLearningAgent

import matplotlib.pyplot as plt
import pandas as pd
import numpy

pygame.init()

with open("Q_Table.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    # Piece,Board,Current State,Current Action,Value
    writer.writerow(["Piece", "Board", "Current State", "Current Action", "Value"])

with open("State_Q_Table.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    # Piece,Current State,Current Action,Value
    writer.writerow(["Piece", "Current State", "Current Action", "Value"])

endgame_agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.2)
endgame_q_table = endgame_agent.q_table

agent = State_QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.2)
q_table = agent.q_table

capacity = 10000
batch_size = 64
# neural_network_model = QNetwork()
# replay_memory = ReplayMemory(capacity)

moves_list = []
number_of_moves = 0

learning_rate = 0.1
discount_factor = 0.9
greedy = 0.2

red_promotion = 5
black_promotion = 0

def game_over():
    global board, graphics, selected_piece, valid_moves, new_selected_piece, new_valid_moves, new_selected_random_piece, player_1_turn, player_2_turn, moves_list, number_of_moves
    board = [
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [-1, 0, -1, 0, -1, 0],
        [0, -1, 0, -1, 0, -1]
    ]
    graphics = UserInterface()
    selected_piece = None
    valid_moves = None
    new_selected_piece = None
    new_valid_moves = None
    new_selected_random_piece = None
    player_1_turn = True
    player_2_turn = False
    number_of_moves = 0
    # neural_network_model.save_model()
    update_winrate(q_learning_wins + random_bot_wins, q_learning_wins, random_bot_victory)


with open("winrate.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Game Number", "Win Rate", "Bot Won"])

def update_winrate(game_number, ai_wins, bot_won):
    with open("winrate.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        win_rate = round(ai_wins / game_number * 100, 2) if game_number > 0 else 0
        writer.writerow([game_number, win_rate, bot_won])

# starting the game
check_move = CheckMove()
graphics = UserInterface()

selected_piece = None
valid_moves = None
new_selected_piece = None
new_valid_moves = None
selected_random_piece = None
new_selected_random_piece = None
new_state_actions_list = []

player_1_turn = True
player_2_turn = False
chain_eating = False
iterator = False

random_bot_wins = 0
random_bot_victory = 0
q_learning_wins = 0
winrate_list = []

# def calculate_winrate(self, bot_wins, ai_wins):
#     winrate = random_bot_wins / q_learning_wins if q_learning_wins > 0 else 0
#     winrate_size = len(winrate_list)
#     winrate_list.append([winrate_size, winrate])

nn_endgame = False
wins_before_player_move = 10
run = True
while run:
    reward = 0
    new_board = []
    for i in range(len(graphics.board)):
        new_board += graphics.board[i]

    if (1 not in new_board and 2 not in new_board) or (-1 not in new_board and -2 not in new_board):
        if 1 not in new_board and 2 not in new_board:
            random_bot_wins += 1
            random_bot_victory = 100
            reward -= 100
        elif -1 not in new_board and -2 not in new_board:
            q_learning_wins += 1
            random_bot_victory = 0
            reward += 100

        print(f"random bot: {random_bot_wins}, q learning: {q_learning_wins}")
        game_over()

    # random bot
    elif player_1_turn and q_learning_wins < wins_before_player_move:
        state_actions_list = []

        for i in range(len(graphics.board)):
            for j in range(len(graphics.board[i])):
                if graphics.board[i][j] == -1:
                    state_actions_list.append((graphics.board[i][j], (i, j), check_move.check_moves_minus_1((i, j), graphics.board)))
                elif graphics.board[i][j] == -2:
                    state_actions_list.append((graphics.board[i][j], (i, j), check_move.king_check_moves_minus_2((i, j), graphics.board)))

        state_actions_list = [state_action for state_action in state_actions_list if len(state_action[-1]) > 0]
        state_actions_size = len(state_actions_list)

        # if True:
        # in case there are no more possible moves left; should be an easy fix
        if state_actions_size > 0:
            random_piece = random.randint(0, state_actions_size - 1)  # selects any piece within state_actions_list
            action_spaces = state_actions_list[random_piece][-1]
            # print(action_spaces) # its workingggg
            action_space_size = len(action_spaces) - 1
            random_move = random.randint(0, action_space_size)  # selects a move from the state actions list, the selected random piece and from there the available moves
            make_move = state_actions_list[random_piece][-1][random_move]  # coordinates within the state action list of the random piece, it's total actions and from its total actions one of them

            selected_random_piece = (state_actions_list[random_piece][0], state_actions_list[random_piece][1], make_move)
            # print(selected_random_piece)

            player_1_turn = False
            player_2_turn = True

            if iterator:
                make_move = random.choice(new_state_actions_list)
                selected_random_piece = new_selected_random_piece
                iterator = False

            row_event, column_event = make_move
            graphics.board[row_event][column_event] = selected_random_piece[0]

            if row_event == black_promotion:
                graphics.board[row_event][column_event] = -2
            graphics.board[selected_random_piece[1][0]][selected_random_piece[1][1]] = 0

            if abs(row_event - selected_random_piece[1][0]) == 2:
                row_capture = (row_event + selected_random_piece[1][0]) // 2
                column_capture = (column_event + selected_random_piece[1][1]) // 2
                graphics.board[row_capture][column_capture] = 0
                reward -= 30
                chain_eating = True

            following_state = (selected_random_piece[0], make_move)  # following state (1, (4, 1))
            # print(f"following state {following_state}")

            if chain_eating:
                chain_eating = False
                player_1_turn = True
                player_2_turn = False
                state_actions_list = []
                new_state_actions_list = []

                if following_state[0] == -1:
                    state_actions_list.append(check_move.eat_pieces_minus_1(following_state[1], graphics.board))
                elif following_state[0] == -2:
                    state_actions_list.append(check_move.king_eat_pieces_minus_2(following_state[1], graphics.board))

                for state_action in state_actions_list:
                    if len(state_action) > 0:
                        new_state_actions_list += state_action
                new_selected_random_piece = (following_state[0], following_state[1], new_state_actions_list)

                if len(new_state_actions_list) < 1:
                    player_1_turn = False
                    player_2_turn = True

                else:
                    iterator = True

        else:
            q_learning_wins += 1
            random_bot_victory = 0
            print(f"random bot: {random_bot_wins}, q learning: {q_learning_wins}")
            game_over()

        if number_of_moves > 500:
            q_learning_wins += 1
            random_bot_victory = 0
            print(f"random bot: {random_bot_wins}, q learning: {q_learning_wins}")
            game_over()
        # q learning bot

    elif player_2_turn:
        number_of_moves += 1
        q_values = []
        q_values_states = []
        state_actions_list = []

        player_2_pieces = []
        for i in range(len(graphics.board)):
            player_2_pieces += graphics.board[i]
        player_2_pieces = player_2_pieces.count(1) + player_2_pieces.count(2)


        if number_of_moves <= 30 or player_2_pieces > 3:
            for i in range(len(graphics.board)):
                for j in range(len(graphics.board[i])):
                    if graphics.board[i][j] == 1:
                        state_actions_list.append((graphics.board[i][j], (i, j), check_move.check_moves_1((i, j), graphics.board)))
                    elif graphics.board[i][j] == 2:
                        state_actions_list.append((graphics.board[i][j], (i, j), check_move.king_check_moves_2((i, j), graphics.board)))

            state_actions_list = [state_action for state_action in state_actions_list if len(state_action[-1]) > 0]
            state_actions_size = len(state_actions_list)
            # print(state_actions_list) # [((2, 1), [(3, 0), (3, 2)]), ((2, 3), [(3, 2), (3, 4)]), ((2, 5), [(3, 4), (3, 6)]), ((2, 7), [(3, 6)])]

            if random.random() < greedy:
                # if True:
                try:
                    random_piece = random.randint(0, state_actions_size - 1)  # selects any piece within state_actions_list
                    action_spaces = state_actions_list[random_piece][-1]
                    # print(action_spaces) # its workingggg [(6, 1), (6, 3)]
                    action_space_size = len(action_spaces) - 1
                    random_move = random.randint(0, action_space_size)  # selects a move from the state actions list, the selected random piece and from there the available moves
                    make_move = state_actions_list[random_piece][-1][random_move]  # coordinates within the state action list of the random piece, it's total actions and from its total actions one of them
                    selected_random_piece = (state_actions_list[random_piece][0], state_actions_list[random_piece][1], make_move)  # (2, (2, 1), (3, 0))
                except ValueError:
                    # random_bot_wins += 1
                    # print(f"random bot: {random_bot_wins}, q learning: {q_learning_wins}")
                    # game_over()
                    # break
                    print("oopsies")

            else:
                for state in state_actions_list:
                    for action in state[-1]:
                        # print(f"state, action {(state[0], state[1]), action}") # covers all cases: state, action ((2, (2, 1)), (3, 0))
                        q_values.append(agent.get_q_value(state[0], state[1], action))  # should be correct
                        q_values_states.append((state[1], action))  # added state[0] in the line above, do i need to do it here too?

                max_q_value = max(q_values, default=0)
                best_action = []  # list of the best actions
                for i in range(len(q_values)):
                    if q_values[i] == max_q_value:
                        best_action.append(q_values_states[i])

                if len(best_action) < 1:
                    game_over()
                else:
                    select_best_action = random.choice(best_action)  # should i add an if there is no best action?
                    # print(f"selected best action: {select_best_action}")
                    make_move = select_best_action[1]
                    selected_random_piece = (graphics.board[select_best_action[0][0]][select_best_action[0][1]], select_best_action[0], make_move)

            player_1_turn = True
            player_2_turn = False

            if iterator:
                make_move = random.choice(new_state_actions_list)
                selected_random_piece = new_selected_random_piece
                iterator = False

            row_event, column_event = make_move
            graphics.board[row_event][column_event] = selected_random_piece[0]

            if graphics.board[row_event][column_event] == 1:
                reward += 1
            elif graphics.board[row_event][column_event] == 2:
                reward += 2

            total_pieces = []
            for i in range(len(graphics.board)):
                total_pieces += graphics.board[i]
            pawns = total_pieces.count(1)
            kings = total_pieces.count(2)
            reward += (pawns + 3*kings)

            if row_event == red_promotion:
                reward += 10
                graphics.board[row_event][column_event] = 2
            graphics.board[selected_random_piece[1][0]][selected_random_piece[1][1]] = 0

            if abs(row_event - selected_random_piece[1][0]) == 2:
                reward += 30
                row_capture = (row_event + selected_random_piece[1][0]) // 2
                column_capture = (column_event + selected_random_piece[1][1]) // 2
                graphics.board[row_capture][column_capture] = 0
                chain_eating = True

            following_state = (selected_random_piece[0], make_move)  # following_state = graphics.board
            # print(f"next state {following_state}")

            agent.update_q_table(piece=selected_random_piece[0], current_state=selected_random_piece[1],
                                 current_action=make_move, reward=reward,
                                 next_state=following_state, action_space_size=action_spaces)

            if chain_eating:
                reward += reward
                chain_eating = False
                player_1_turn = False
                player_2_turn = True
                state_actions_list = []
                new_state_actions_list = []

                if following_state[0] == 1:  # check here for all the possible moves
                    state_actions_list.append(check_move.eat_pieces_1(following_state[1], graphics.board))
                elif following_state[0] == 2:
                    state_actions_list.append(check_move.king_eat_pieces_2(following_state[1], graphics.board))

                for state_action in state_actions_list:
                    if len(state_action) > 0:
                        new_state_actions_list += state_action
                new_selected_random_piece = (following_state[0], following_state[1], new_state_actions_list)

                if len(new_state_actions_list) < 1:
                    player_1_turn = True
                    player_2_turn = False

                else:
                    iterator = True

        # elif nn_endgame: # placeholder for nn endgame
        #     neural_network_model.load_state_dict(torch.load('DQN.pth'))
        #     neural_network_model.eval()
        #     for i in range(len(graphics.board)):
        #         for j in range(len(graphics.board[i])):
        #             if graphics.board[i][j] == 1:
        #                 state_actions_list.append((graphics.board[i][j], (i, j), check_move.check_moves_1((i, j), graphics.board)))
        #             elif graphics.board[i][j] == 2:
        #                 state_actions_list.append((graphics.board[i][j], (i, j), check_move.king_check_moves_2((i, j), graphics.board)))
        #
        #     state_actions_list = [state_action for state_action in state_actions_list if len(state_action[-1]) > 0]
        #     state_actions_size = len(state_actions_list)
        #
        #     for state in state_actions_list:
        #         for action in state[-1]:
        #             board_string = str(graphics.board)
        #             current_state_string = str(state[1])
        #             current_action_string = str(action)
        #             q_values.append(neural_network_model.predict_q_value(state[0], board_string, current_state_string, current_action_string))
        #             q_values_states.append((state[1], action))
        #
        #     max_q_value = max(q_values, default=0)
        #     best_action = []
        #     for i in range(len(q_values)):
        #         if q_values[i] == max_q_value:
        #             best_action.append(q_values_states[i])
        #
        #     if len(best_action) < 1:
        #         game_over()
        #     else:
        #         select_best_action = random.choice(best_action)
        #         make_move = select_best_action[1]
        #         selected_random_piece = (graphics.board[select_best_action[0][0]][select_best_action[0][1]], select_best_action[0], make_move)
        #
        #     player_1_turn = True
        #     player_2_turn = False
        #
        #     if iterator:
        #         make_move = random.choice(new_state_actions_list)
        #         selected_random_piece = new_selected_random_piece
        #         iterator = False
        #
        #     row_event, column_event = make_move
        #     graphics.board[row_event][column_event] = selected_random_piece[0]
        #
        #     if graphics.board[row_event][column_event] == 1:
        #         reward += 1
        #     elif graphics.board[row_event][column_event] == 2:
        #         reward += 2
        #
        #     total_pieces = []
        #     for i in range(len(graphics.board)):
        #         total_pieces += graphics.board[i]
        #     pawns = total_pieces.count(1)
        #     kings = total_pieces.count(2)
        #     reward += (pawns + 3*kings)
        #
        #
        #     if row_event == red_promotion:
        #         reward += 10
        #         graphics.board[row_event][column_event] = 2
        #     graphics.board[selected_random_piece[1][0]][selected_random_piece[1][1]] = 0
        #
        #     if abs(row_event - selected_random_piece[1][0]) == 2:
        #         reward += 30
        #         row_capture = (row_event + selected_random_piece[1][0]) // 2
        #         column_capture = (column_event + selected_random_piece[1][1]) // 2
        #         graphics.board[row_capture][column_capture] = 0
        #         chain_eating = True
        #
        #     following_state = (selected_random_piece[0], make_move)
        #
        #     replay_memory.push(piece=selected_random_piece[0], board=graphics.board, current_state=selected_random_piece[1], current_action=make_move, reward=reward, next_state=following_state, action_space=action_spaces)
        #
        #     if len(replay_memory) > batch_size:
        #         experience = replay_memory.sample(batch_size)
        #         piece, board, current_state, current_action, reward, next_state, action_space = zip(*experience)
        #         random_int = random.randint(0, len(piece) - 1)
        #
        #         piece = piece[random_int]
        #         board = board[random_int]
        #         current_state = current_state[random_int]
        #         current_action = current_action[random_int]
        #         reward = reward[random_int]
        #         next_state = next_state[random_int]
        #         action_space = action_space[random_int]
        #
        #         current_q_value, new_q_value = endgame_agent.update_neural_network(piece, board, current_state, current_action, reward, next_state, action_space)
        #         current_q_value = torch.tensor(current_q_value, dtype=torch.float32, requires_grad=True)
        #         new_q_value = torch.tensor(new_q_value, dtype=torch.float32, requires_grad=True)
        #         loss = neural_network_model.criterion(current_q_value, new_q_value)
        #         neural_network_model.optimiser.zero_grad()
        #         loss.backward()
        #         neural_network_model.optimiser.step()
        #
        #     if chain_eating:
        #         reward += reward
        #         chain_eating = False
        #         player_1_turn = False
        #         player_2_turn = True
        #         state_actions_list = []
        #         new_state_actions_list = []
        #
        #         if following_state[0] == 1:  # check here for all the possible moves
        #             state_actions_list.append(check_move.eat_pieces_1(following_state[1], graphics.board))
        #         elif following_state[0] == 2:
        #             state_actions_list.append(check_move.king_eat_pieces_2(following_state[1], graphics.board))
        #
        #         for state_action in state_actions_list:
        #             if len(state_action) > 0:
        #                 new_state_actions_list += state_action
        #         new_selected_random_piece = (following_state[0], following_state[1], new_state_actions_list)
        #
        #         if len(new_state_actions_list) < 1:
        #             player_1_turn = True
        #             player_2_turn = False
        #
        #         else:
        #             iterator = True

        else: # placeholder for endgame
            for i in range(len(graphics.board)):
                for j in range(len(graphics.board[i])):
                    if graphics.board[i][j] == 1:
                        state_actions_list.append((graphics.board[i][j], (i, j), check_move.check_moves_1((i, j), graphics.board)))
                    elif graphics.board[i][j] == 2:
                        state_actions_list.append((graphics.board[i][j], (i, j), check_move.king_check_moves_2((i, j), graphics.board)))

            state_actions_list = [state_action for state_action in state_actions_list if len(state_action[-1]) > 0]
            state_actions_size = len(state_actions_list)

            if random.random() < greedy:
                # if True:
                random_piece = random.randint(0, state_actions_size - 1)  # selects any piece within state_actions_list
                action_spaces = state_actions_list[random_piece][-1]
                # print(action_spaces) # its workingggg [(6, 1), (6, 3)]
                action_space_size = len(action_spaces) - 1
                random_move = random.randint(0, action_space_size)  # selects a move from the state actions list, the selected random piece and from there the available moves
                make_move = state_actions_list[random_piece][-1][random_move]  # coordinates within the state action list of the random piece, it's total actions and from its total actions one of them

                selected_random_piece = (state_actions_list[random_piece][0], state_actions_list[random_piece][1], make_move)  # (2, (2, 1), (3, 0))

            else:
                for state in state_actions_list:
                    for action in state[-1]:
                        # print(f"state, action {(state[0], state[1]), action}") # covers all cases: state, action ((2, (2, 1)), (3, 0))
                        q_values.append(endgame_agent.get_q_value(state[0], graphics.board, state[1], action))  # should be correct
                        q_values_states.append((state[1], action))  # added state[0] in the line above, do i need to do it here too?

                max_q_value = max(q_values, default=0)
                best_action = []  # list of the best actions
                for i in range(len(q_values)):
                    if q_values[i] == max_q_value:
                        best_action.append(q_values_states[i])

                if len(best_action) < 1:
                    game_over()
                else:
                    select_best_action = random.choice(best_action)  # should i add an if there is no best action?
                    # print(f"selected best action: {select_best_action}")
                    make_move = select_best_action[1]
                    selected_random_piece = (graphics.board[select_best_action[0][0]][select_best_action[0][1]], select_best_action[0], make_move)

            player_1_turn = True
            player_2_turn = False

            if iterator:
                make_move = random.choice(new_state_actions_list)
                selected_random_piece = new_selected_random_piece
                iterator = False

            row_event, column_event = make_move
            graphics.board[row_event][column_event] = selected_random_piece[0]

            if graphics.board[row_event][column_event] == 1:
                reward += 1
            elif graphics.board[row_event][column_event] == 2:
                reward += 2

            total_pieces = []
            for i in range(len(graphics.board)):
                total_pieces += graphics.board[i]
            pawns = total_pieces.count(1)
            kings = total_pieces.count(2)
            reward += (pawns + 3*kings)

            if row_event == red_promotion:
                reward += 10
                graphics.board[row_event][column_event] = 2
            graphics.board[selected_random_piece[1][0]][selected_random_piece[1][1]] = 0

            if abs(row_event - selected_random_piece[1][0]) == 2:
                reward += 30
                row_capture = (row_event + selected_random_piece[1][0]) // 2
                column_capture = (column_event + selected_random_piece[1][1]) // 2
                graphics.board[row_capture][column_capture] = 0
                chain_eating = True

            following_state = (selected_random_piece[0], make_move)  # following_state = graphics.board

            endgame_agent.update_q_table(piece=selected_random_piece[0], board=graphics.board, current_state=selected_random_piece[1],
                                         current_action=make_move, reward=reward,
                                         next_state=following_state, action_space=action_spaces)

            if chain_eating:
                reward += reward
                chain_eating = False
                player_1_turn = False
                player_2_turn = True
                state_actions_list = []
                new_state_actions_list = []

                if following_state[0] == 1:  # check here for all the possible moves
                    state_actions_list.append(check_move.eat_pieces_1(following_state[1], graphics.board))
                elif following_state[0] == 2:
                    state_actions_list.append(check_move.king_eat_pieces_2(following_state[1], graphics.board))

                for state_action in state_actions_list:
                    if len(state_action) > 0:
                        new_state_actions_list += state_action
                new_selected_random_piece = (following_state[0], following_state[1], new_state_actions_list)

                if len(new_state_actions_list) < 1:
                    player_1_turn = True
                    player_2_turn = False

                else:
                    iterator = True

        # agent.save_q_table_csv()
        # endgame_agent.save_q_table_csv()

    elif player_1_turn and q_learning_wins >= wins_before_player_move:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_over()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print((random_bot_wins / q_learning_wins) * 100, "%")
                mouseX, mouseY = event.pos
                row_event = mouseY // graphics.dimensions["checker_tile"]
                column_event = mouseX // graphics.dimensions["checker_tile"]

                if selected_piece is None and new_selected_piece is None:
                    if graphics.board[row_event][column_event] == -1:
                        selected_piece = (row_event, column_event)
                        valid_moves = check_move.check_moves_minus_1(selected_piece, graphics.board)
                    elif graphics.board[row_event][column_event] == -2:
                        selected_piece = (row_event, column_event)
                        valid_moves = check_move.king_check_moves_minus_2(selected_piece, graphics.board)
                    else:
                        selected_piece = None
                        valid_moves = None

                elif selected_piece is not None and graphics.board[row_event][column_event] == -1 and new_selected_piece is None:
                    selected_piece = (row_event, column_event)
                    valid_moves = check_move.check_moves_minus_1(selected_piece, graphics.board)

                elif selected_piece is not None and graphics.board[row_event][column_event] == -2 and new_selected_piece is None:
                    selected_piece = (row_event, column_event)
                    valid_moves = check_move.king_check_moves_minus_2(selected_piece, graphics.board)

                # check for king or regular
                elif new_selected_piece is not None and graphics.board[new_selected_piece[0]][new_selected_piece[1]] == -1:
                    if len(new_valid_moves) > 0:
                        selected_piece, valid_moves = new_selected_piece, new_valid_moves
                        new_selected_piece = None
                    else:
                        new_selected_piece, new_valid_moves = None, None
                        player_1_turn = False
                        player_2_turn = True

                elif new_selected_piece is not None and graphics.board[new_selected_piece[0]][new_selected_piece[1]] == -2:
                    if len(new_valid_moves) > 0:
                        selected_piece, valid_moves = new_selected_piece, new_valid_moves
                        new_selected_piece = None
                    else:
                        new_selected_piece, new_valid_moves = None, None
                        player_1_turn = False
                        player_2_turn = True

                else:
                    if (row_event, column_event) in valid_moves:
                        graphics.board[row_event][column_event] = graphics.board[selected_piece[0]][selected_piece[1]]
                        if row_event == black_promotion:
                            graphics.board[row_event][column_event] = -2
                        graphics.board[selected_piece[0]][selected_piece[1]] = 0
                        player_1_turn = False
                        player_2_turn = True

                        if abs(row_event - selected_piece[0]) == 2:
                            row_capture = (row_event + selected_piece[0]) // 2
                            column_capture = (column_event + selected_piece[1]) // 2
                            graphics.board[row_capture][column_capture] = 0
                            reward -= 30

                            new_selected_piece = (row_event, column_event)
                            if row_event == black_promotion or graphics.board[row_event][column_event] == -2:
                                new_valid_moves = check_move.king_eat_pieces_minus_2(new_selected_piece, graphics.board)
                            else:
                                new_valid_moves = check_move.eat_pieces_minus_1(new_selected_piece, graphics.board)
                            player_1_turn = True
                            player_2_turn = False

                        selected_piece, valid_moves = None, None

    graphics.draw_board(selected_piece, valid_moves)
    graphics.draw_game_over()

    agent.save_q_table_csv()
    endgame_agent.save_q_table_csv()
    # agent.load_q_table_csv()
    # endgame_agent.load_q_table_csv()

    # print("check1 ")
    if os.path.getsize("State_Q_Table.csv") > 5:
        agent.load_q_table_csv()
        # print("check2")
    else:
        print("fail")
    # print("check3")

    pygame.display.flip()


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
polynomial_regression = numpy.linspace(1, (q_learning_wins + random_bot_wins) * 1.01, 10)
plt.plot(polynomial_regression, polynomial_regression_model(polynomial_regression))

plt.show()
