import pygame


class UserInterface:
    def __init__(self):
        width, height = 800, 800
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Checkers!")

        self.dimensions = {
            "ROWS": 6,
            "COLUMNS": 6,
            "checker_tile": 125
        }

        self.colors = {
            "BLACK": (0, 0, 0),
            "WHITE": (250, 250, 250),
            "GREY": (50, 50, 50),
            "RED": (250, 0, 0),
            "GREEN": (0, 250, 0),
            "YELLOW": (250, 250, 0),
        }

        self.surface = {
            "font": pygame.font.Font('freesansbold.ttf', 20),
            "transparent_surface": pygame.Surface((width, height), pygame.SRCALPHA)
        }

        self.board = [
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [-1, 0, -1, 0, -1, 0],
        [0, -1, 0, -1, 0, -1]
    ]

    def draw_board(self, selected_piece=None, valid_moves=None):
        ROWS, COLUMNS = self.dimensions["ROWS"], self.dimensions["COLUMNS"]
        checker_tile = self.dimensions["checker_tile"]
        for row_draw_board in range(ROWS):
            for column_draw_board in range(COLUMNS):
                colour = self.colors["RED"] if (row_draw_board + column_draw_board) % 2 == 0 else self.colors["BLACK"]
                single_tile_draw_board = (
                    column_draw_board * checker_tile, row_draw_board * checker_tile, checker_tile, checker_tile)
                crown = (
                    column_draw_board * checker_tile + (checker_tile / 3),
                    row_draw_board * checker_tile + (checker_tile / 3), checker_tile / 3, checker_tile / 3)
                pygame.draw.rect(self.screen, colour, single_tile_draw_board)
                pygame.draw.rect(self.screen, self.colors["WHITE"], single_tile_draw_board, 2)

                piece = self.board[row_draw_board][column_draw_board]
                piece_placement = (
                    column_draw_board * checker_tile + checker_tile // 2,
                    row_draw_board * checker_tile + checker_tile // 2)
                size = checker_tile // 2 - 10
                if piece == 1:
                    pygame.draw.circle(self.screen, self.colors["GREY"], piece_placement, size)
                    pygame.draw.circle(self.screen, self.colors["WHITE"], piece_placement, size, 1)  # outline
                if piece == 2:
                    pygame.draw.circle(self.screen, self.colors["GREY"], piece_placement, size)
                    pygame.draw.rect(self.screen, self.colors["YELLOW"], crown, 5)
                    pygame.draw.circle(self.screen, self.colors["WHITE"], piece_placement, size, 1)  # outline
                if piece == -1:
                    pygame.draw.circle(self.screen, self.colors["RED"], piece_placement, size)
                    pygame.draw.circle(self.screen, self.colors["WHITE"], piece_placement, size, 1)  # outline
                if piece == -2:
                    pygame.draw.circle(self.screen, self.colors["RED"], piece_placement, size)
                    pygame.draw.rect(self.screen, self.colors["YELLOW"], crown, 5)
                    pygame.draw.circle(self.screen, self.colors["WHITE"], piece_placement, size, 1)  # outline

                if selected_piece is not None and (row_draw_board, column_draw_board) == selected_piece:
                    single_tile_selected_piece = (
                        column_draw_board * checker_tile, row_draw_board * checker_tile, checker_tile, checker_tile)
                    pygame.draw.rect(self.screen, self.colors["GREEN"], single_tile_selected_piece, 5)

                if valid_moves is not None and (row_draw_board, column_draw_board) in valid_moves:
                    pygame.draw.circle(self.screen, self.colors["WHITE"],
                                       (column_draw_board * checker_tile + checker_tile // 2,
                                        row_draw_board * checker_tile + checker_tile // 2),
                                       checker_tile // 4, 5)

    def draw_game_over(self):
        board_pieces = []
        game_winner = None
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                board_pieces.append(self.board[i][j])
        board_pieces = set(board_pieces)
        board_pieces = list(board_pieces)

        if 1 not in board_pieces and 2 not in board_pieces and -1 in board_pieces and -2 in board_pieces:
            game_winner = "PLAYER 1"
        elif 1 in board_pieces and 2 in board_pieces and -1 not in board_pieces and -2 not in board_pieces:
            game_winner = "PLAYER 2"

        if game_winner is not None:
            self.screen.blit(self.surface["transparent_surface"], (0, 0))
            pygame.draw.rect(self.surface["transparent_surface"], (250, 250, 250, 230), [0, 0, 800, 800])
            self.screen.blit(self.surface["font"].render(f'{game_winner} won the game!', True, self.colors["BLACK"]),
                             (280, 370))
            self.screen.blit(self.surface["font"].render(f'Press ENTER to Restart!', True, self.colors["BLACK"]),
                             (280, 410))

    # def initialise(self):
    #     global selected_piece, valid_moves, new_selected_piece, new_valid_moves, selected_random_piece, new_selected_random_piece, new_state_actions_list, player_1_turn, player_2_turn, chain_eating, iterator
    #     selected_piece = None
    #     valid_moves = None
    #     new_selected_piece = None
    #     new_valid_moves = None
    #     selected_random_piece = None
    #     new_selected_random_piece = None
    #     new_state_actions_list = []
    #
    #     player_1_turn = True
    #     player_2_turn = False
    #     chain_eating = False
    #     iterator = False

    # def game_over(self):
    #     global board, graphics, selected_piece, valid_moves, new_selected_piece, new_valid_moves, new_selected_random_piece, player_1_turn, player_2_turn, moves_list, number_of_moves
    #     board = [
    #         [0, 2, 0, 2, 0, 2, 0, 2],
    #         [2, 0, 2, 0, 2, 0, 2, 0],
    #         [0, 2, 0, 2, 0, 2, 0, 2],
    #         [0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0],
    #         [1, 0, 1, 0, 1, 0, 1, 0],
    #         [0, 1, 0, 1, 0, 1, 0, 1],
    #         [1, 0, 1, 0, 1, 0, 1, 0]
    #     ]
    #     graphics = UserInterface()
    #
    #     selected_piece = None
    #     valid_moves = None
    #     new_selected_piece = None
    #     new_valid_moves = None
    #     new_selected_random_piece = None
    #
    #     player_1_turn = True
    #     player_2_turn = False
    #
    #     number_of_moves = 0
