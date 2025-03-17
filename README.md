# MNK-Game

## Project Structure
The game is based on several classes that implement the core functions:

### 1. Board Class
- Represents the game board as a `numpy` matrix (`np.zeros`).
- Implements the `has_won` method for checking win conditions.
- A major challenge was verifying diagonal win conditions.

### 2. Player Class
- Implements player logic.
- Contains the `make_move` method to check for valid moves.

### 3. Game Class
- Controls the game flow (player vs. player).
- Imports and manages other classes.
- Uses `game_loop` to handle the game flow.

### 4. MyBot Class
This class extends `Player` and represents an AI-controlled player.
Depending on the difficulty level, the bot uses different strategies:
- **Easy AI**: Randomly selects a free position.
- **Medium AI**: Simulates moves to determine if a winning move is possible.
- **Hard AI**: Not only simulates its own winning moves but also considers the opponent’s potential winning moves.

## Minimax Algorithm
The **Minimax algorithm** is used in the AI implementation to determine the best possible move. It is a recursive algorithm commonly used in turn-based games like Tic-Tac-Toe, Chess, and MNK-Game. The key principles of Minimax are:
- The AI assumes that it is playing optimally and that the opponent is also making the best possible moves.
- The algorithm explores all possible moves, evaluates them, and assigns a score based on whether they lead to a win, loss, or draw.
- **Minimizing Player (Opponent)**: Tries to minimize the score (avoid losing moves).
- **Maximizing Player (AI)**: Tries to maximize the score (choose the best move leading to victory).
- The AI uses a depth-based approach to limit computation time, as deeper searches become increasingly complex.
- To optimize performance, **alpha-beta pruning** is implemented, which reduces unnecessary calculations by cutting off branches that won’t affect the final decision.

## Implementation
- The game was initially developed without strict OOP principles, which led to issues.
- It was then restructured with a clear separation of classes and responsibilities.
- `numpy` was primarily used for board logic, and AI algorithms like `Minimax` were implemented.

## Requirements
- Python 3.x
- `numpy`

## Usage
1. Start the game by running the `Game.py` file.
2. Choose a game mode (human vs. human or human vs. AI or AI vs. AI).
3. Follow the instructions in the console.

## Future Enhancements
- Improve AI with more efficient algorithms.
- Implement a graphical user interface.
- Expand to an online multiplayer mode.

---
