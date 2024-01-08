# Othello Game in Python Tkinter

This project is a Python implementation of the classic board game Othello (also known as Reversi) using the Tkinter GUI library. The game features a simple interface where players can play against a basic computer AI.

## Features

- Graphical user interface using Tkinter.
- Basic computer opponent logic.
- Board setup and legal move calculation.
- Game end detection with a score count.

## Requirements

- Python 3.x
- Tkinter library (usually comes pre-installed with Python).

## Installation

No additional installation is required if Python 3.x is already installed.

## Usage

Run the script using Python:

```bash
python reversi_product.py
```
### Using the Executable File

Alternatively, you can use the standalone executable file:

1. Download the `OthelloGame.exe` file from the repository.
2. Double-click on the downloaded file to run the game.

## Game Rules

- Each turn, you must place a disk on the board with your assigned color facing up.
- You can only place a disk if it brackets one or several of your opponent's disks between the disk played and another disk of your color.
- All bracketed disks of the opponent's color are flipped to become your color.
- The game ends when neither player can move, usually when the board is full.
- The player with the most disks of their color on the board at the end of the game wins.


