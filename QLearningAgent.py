import pandas as pd


class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2, q_table_csv='Q_Table.csv'):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table_csv = q_table_csv
        self.load_q_table_csv()

    def load_q_table_csv(self):
        try:
            q_table_df = pd.read_csv(self.q_table_csv)
            for _, row in q_table_df.iterrows():
                piece = row["Piece"]
                board = eval(row["Board"])
                current_state = eval(row["Current State"])
                current_action = eval(row["Current Action"])
                self.q_table[(piece, tuple(map(tuple, board)), current_state, current_action)] = row['Value']
        except FileNotFoundError:
            print("File not found")

    def save_q_table_csv(self):
        q_table_df = pd.DataFrame([
            {
                "Piece": key[0],
                "Board": str([list(row) for row in key[1]]),
                "Current State": str(key[2]),
                "Current Action": str(key[3]),
                "Value": value
            }
            for key, value in self.q_table.items()
        ])
        q_table_df.to_csv(self.q_table_csv, index=False)

    def get_q_value(self, piece, board, current_state, current_action):
        return self.q_table.get((piece, tuple(map(tuple, board)), current_state, current_action), 0.0)

    def update_q_table(self, piece, board, current_state, current_action, reward, next_state, action_space):
        max_future_q_value = max([self.get_q_value(piece, board, next_state, a) for a in action_space], default=0.0)
        current_q_value = self.get_q_value(piece, board, current_state, current_action)
        new_q_value = current_q_value + self.alpha * (reward + self.gamma * max_future_q_value - current_q_value)
        self.q_table[(piece, tuple(map(tuple, board)), current_state, current_action)] = new_q_value

    def update_neural_network(self, piece, board, current_state, current_action, reward, next_state, action_space):
        max_future_q_value = max([self.get_q_value(piece, board, next_state, a) for a in action_space], default=0.0)
        current_q_value = self.get_q_value(piece, board, current_state, current_action)
        new_q_value = current_q_value + self.alpha * (reward + self.gamma * max_future_q_value - current_q_value)
        return current_q_value, new_q_value