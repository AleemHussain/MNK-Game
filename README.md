# MNK-Game

## Overview  
MNK is a flexible strategy game similar to Tic-Tac-Toe, where players can define the board size (M × N) and the number of consecutive marks (K) needed to win. The game supports human players and AI-controlled bots with different difficulty levels.

## Project Structure  
The project is structured for clarity, modularity, and testability:

```
├── .github/workflows/
│   └── basic_ci.yml              # CI/CD workflow configuration
│
├── Code/
│   ├── Board.py                  # Game board logic and win condition checks
│   ├── Game.py                   # Main game loop and controller
│   ├── MyBot.py                  # AI bot implementation using Minimax
│   └── Player.py                 # Base Player class for humans and bots
│
├── Tests/
│   ├── test_Board.py             # Unit tests for Board
│   ├── test_Game.py              # Unit tests for Game
│   ├── test_MyBot.py             # Unit tests for MyBot (AI logic)
│   └── test_Player.py            # Unit tests for Player
│
├── .gitignore
├── .pre-commit-config.yml       # Linting and formatting automation
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md
├── environment.yml              # Conda environment dependencies
└── pyproject.toml               # Project metadata and dependencies
```

## Class Descriptions  

### Board  
- Represents the game board using a NumPy matrix (`np.zeros`).  
- `has_won` method checks for win conditions (horizontal, vertical, diagonal).  
- Diagonal detection required custom logic and was one of the trickiest parts.

### Player  
- Represents a human player.  
- `make_move` checks move validity and applies it to the board.

### Game  
- Main orchestrator of the gameplay.  
- Imports and connects all other components.  
- Contains the `game_loop` that manages turn-taking and game flow.

### MyBot  
- Inherits from `Player` and implements AI logic using different strategies:  

| Difficulty | Strategy |
|------------|----------|
| Easy       | Random move selection |
| Medium     | Simulates own winning moves |
| Hard       | Simulates both own and opponent moves using Minimax |

## Minimax Algorithm  
- Recursive algorithm for optimal decision-making in two-player games.  
- Evaluates all possible game states up to a depth limit.  
- Alpha-Beta pruning is used to optimize performance.  
- Difficulty level affects how deep the search goes and how defensive/offensive the bot plays.

## Requirements  
- Python 3.x  
- NumPy (install with `pip install numpy`)  
- Optional: Use `environment.yml` with Conda to install all dependencies

## How to Run  
1. Navigate to the root of the project directory.  
2. Run the game from the terminal:  
   ```bash
   python Code/Game.py
   ```  
3. Follow the command-line prompts to select:  
   - Human vs. Human  
   - Human vs. Bot  
   - Bot vs. Bot

## Testing  
Run unit tests using:

```bash
pytest Tests/
```

---