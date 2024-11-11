import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import ast
import random
from collections import deque
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


file_path = "Q_Table.csv"
df = pd.read_csv(file_path)


def board_to_tensor(board_str):
    return torch.tensor(ast.literal_eval(board_str), dtype=torch.float32).flatten()


def position_to_tensor(position_str):
    return torch.tensor(ast.literal_eval(position_str), dtype=torch.float32)


df['Piece'] = df['Piece'].apply(lambda x: torch.tensor([x], dtype=torch.float32))
df['Board'] = df['Board'].apply(board_to_tensor)
df['Current State'] = df['Current State'].apply(position_to_tensor)
df['Current Action'] = df['Current Action'].apply(position_to_tensor)
X = torch.cat([torch.stack(df['Piece'].values.tolist()), torch.stack(df['Board'].values.tolist()), torch.stack(df['Current State'].values.tolist()), torch.stack(df['Current Action'].values.tolist())], dim=1)
y = torch.tensor(df['Value'].values, dtype=torch.float32).view(-1, 1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


class QNetwork(nn.Module):
    def __init__(self):
        super(QNetwork, self).__init__()

        input_size = X.shape[1]
        hidden_size = 128
        output_size = 1

        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

        self.criterion = nn.MSELoss()
        self.optimiser = optim.Adam(self.parameters(), lr=0.001)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

    def predict_q_value(self, piece, board, current_state, current_action):
        self.eval()
        with torch.no_grad():
            input_tensor = torch.cat([torch.tensor([piece], dtype=torch.float32), board_to_tensor(board), position_to_tensor(current_state), position_to_tensor(current_action)]).unsqueeze(0)
            q_value = self(input_tensor).item()
        return q_value

    def save_model(self):
        torch.save(self.state_dict(), 'DQN.pth')


model = QNetwork()
epochs = 1000
for epoch in range(epochs):
    model.train()
    outputs = model(X_train)
    loss = model.criterion(outputs, y_train)

    model.optimiser.zero_grad()
    loss.backward()
    model.optimiser.step()

    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

model.eval()
with torch.no_grad():
    y_pred = model(X_test)
    test_loss = mean_squared_error(y_test.numpy(), y_pred.numpy())
    print(f'Test Loss: {test_loss:.4f}')


class ReplayMemory:
    def __init__(self, capacity):
        self.memory = deque(maxlen=capacity)

    def push(self, piece, board, current_state, current_action, reward, next_state, action_space):
        self.memory.append((piece, board, current_state, current_action, reward, next_state, action_space))

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)

# model.save_model()
