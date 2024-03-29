# Noughts and Crosses Game

This is a simple implementation of the classic game of Noughts and Crosses (also known as Tic Tac Toe) in Python. The game features a text-based interface, error handling, and a leaderboard system.

## Features

- **Draw Board:** The game board is a 3x3 grid, displayed in the console. Players take turns to place their marker ('X' or 'O') in an empty cell.

- **Error Handling:** The game checks for invalid inputs (such as out-of-range or non-numeric inputs) and prompts the user to try again.

- **Leaderboard:** The game keeps track of the number of wins for each player. The leaderboard is saved and loaded in JSON format.

- **Win Checking:** The game checks for a win after each move. A win is 3 of the same marker ('X' or 'O') in a row, column, or diagonal.

- **Computer Player:** The game includes a simple AI that randomly chooses an empty cell for its move.

## How to Run

1. Clone this repository to your local machine.
2. Run `python noughts_and_crosses.py` in your terminal.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
