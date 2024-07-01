# A Chess Question: Piece Capture Simulator

![Python version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Functions](#functions)
- [Manual Testing Scenarios](#manual-testing-scenarios)
- [Error Handling](#error-handling)
- [Possible Improvements in the Program](#possible-improvements-in-the-program)

## Overview

**Chess_Game.py** is a Python program that simulates a simple version of chess focusing on piece placement and capture possibilities. The program allows users to place a single white piece and up to 16 black pieces on a chessboard, then determines which black pieces the white piece can capture based on their respective positions, types, and standard chess movement rules.

## Features

- Allows the user to input a white piece and its position on the chessboard.
- Allows the user to input up to 16 black pieces and their positions on the chessboard (supports rook and knight piece types - easily extendable to other pieces).
- Validates the input positions to ensure they fall within the bounds of a standard chessboard (a1 to h8).
- Calculates possible moves for each piece type: displays which black pieces, if any, can be captured by the white piece.

## Requirements

- Python 3.7 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TuringCollegeSubmissions/iekosai-PYDA.1.4
   ```
2. Navigate to the project directory:
   ```bash
   cd "C:\Users\ievak\OneDrive\Stalinis kompiuteris\Turing_College\Python\Python Codes"
   ```

## Usage

1. Run the program using Python:
   ```bash
   python Chess_Game.py
   ```
2. Follow the prompts to place the white piece and black pieces.
3. Enter 'done' when you've finished placing black pieces.
4. The program will output which black pieces (if any) can be captured by the white piece.

Example output:

```plaintext
Enter white piece (rook or knight) and position (e.g., 'rook a1'): rook a1
rook added at a1.
Enter black piece (rook or knight) and position (or 'done' to finish): knight c3
knight added at c3.
Enter black piece (rook or knight) and position (or 'done' to finish): rook h1
rook added at h1.
Enter black piece (rook or knight) and position (or 'done' to finish): done
The white rook can capture: rook at h1
```

## How It Works

1. **User Input**:
   - The user is prompted to place a white piece (either a rook or a knight) and its position (e.g., "rook a1").
   - The user is then prompted to place up to 16 black pieces (rooks or knights) and their positions one by one (e.g., "knight b2"). The user can stop entering black pieces by typing "done".

2. **Validation**:
   - The program checks that the positions entered are valid chessboard coordinates.
   - The program ensures that no two pieces occupy the same position.

3. **Capture Calculation**:
   - The program calculates possible moves for the white piece based on its type and position.
   - The program determines which black pieces are in the capture range of the white piece.

4. **Output**:
   - The program outputs a list of black pieces that the white piece can capture.

## Functions

### `is_valid_position(position)`

Checks if a given position is valid on a chessboard.

- **Args**: `position (str)`: A string representing a position on the chessboard (e.g., 'a1', 'h8').
- **Returns**: `bool`: True if the position is valid, False otherwise.

### `get_piece_moves(piece, position)`

Returns a list of possible moves for a given piece at a given position.

- **Args**:
  - `piece (str)`: The type of piece (e.g., 'rook', 'knight').
  - `position (str)`: A string representing the position of the piece on the chessboard (e.g., 'a1', 'h8').
- **Returns**: `list`: A list of possible moves for the piece.

### `can_capture(white_piece, white_pos, black_piece, black_pos)`

Checks if a white piece can capture a black piece.

- **Args**:
  - `white_piece (str)`: The type of white piece (e.g., 'rook', 'knight').
  - `white_pos (str)`: The position of the white piece on the chessboard (e.g., 'a1', 'h8').
  - `black_piece (str)`: The type of black piece (e.g., 'rook', 'knight').
  - `black_pos (str)`: The position of the black piece on the chessboard (e.g., 'a1', 'h8').
- **Returns**: `bool`: True if the white piece can capture the black piece, False otherwise.

### `add_piece(board, piece, position)`

Adds a piece to the board at a given position.

- **Args**:
  - `board (dict)`: The chessboard represented as a dictionary.
  - `piece (str)`: The type of piece to add (e.g., 'rook', 'knight').
  - `position (str)`: The position to add the piece to (e.g., 'a1', 'h8').
- **Returns**: `tuple`: A tuple containing a boolean indicating success and a message.

###  `get_valid_input(prompt, valid_pieces, is_white_piece=False)`
    
Gets and validates user input.

 - **Args**:
     - `prompt (str)`: The prompt to display to the user.
     - `valid_pieces (list)`: List of valid pieces.
     - `is_white_piece (bool)`: Whether the input is for a white piece.
- **Returns**: `list`: A list containing the piece and its position or 'done' to finish.

### `visualize_board(board, highlighted_positions=None)`

Creates a visual representation of the chessboard.

- **Args**:
     - board (dict): The current state of the board.
     - highlighted_positions (list): Positions to highlight (e.g., possible moves).
- **Prints**: A visual representation of the chessboard with pieces and highlighted positions.

### `main()`

Main function to interact with the user and handle the game logic: to add pieces to the board and determine which black pieces can be captured by the white piece.

## Manual Testing Scenarios

### Here are various scenarios to test the program's functionality:

### Scenario 1: Valid Inputs

**Description**: User inputs a valid white piece and position, followed by valid black pieces and positions.

**Option 1 - Rook Captures**:
1. Run the program.
2. Enter `rook a1` when prompted for the white piece and position.
3. Enter `knight a3` for the 1st black piece.
4. Enter `knight a8` for the 2nd black piece.
5. Enter `knight h8` for the 3rd black piece.
6. Enter `rook h1` for the 4th black piece.
7. Enter `done` to finish adding black pieces.
   
**Expected Output**:
- The white rook can capture: `knight a3`, `knight a8`, `rook h1`

``` plaintext
Enter white piece (rook or knight) and position (e.g., 'rook a1'): rook a1
rook added at a1.
Enter black piece (rook or knight) and position (or 'done' to finish): knight a3
knight added at a3.
Enter black piece (rook or knight) and position (or 'done' to finish): knight a8
knight added at a8.
Enter black piece (rook or knight) and position (or 'done' to finish): rook h1
rook added at h1.
Enter black piece (rook or knight) and position (or 'done' to finish): knight h8
knight added at h8.
Enter black piece (rook or knight) and position (or 'done' to finish): done
The white rook can capture: knight at a3, knight at a8, rook at h1

```

**Option 2 White Piece Cannot Capture Any Black Pieces**:
1. Run the program.
2. Enter `knight b1` when prompted for the white piece and position.
3. Enter `knight h8` for the 1st black piece.
4. Enter `rook g8` for the 2nd black piece.
5. Enter `knight h7` for the 3rd black piece.
6. Enter `done` to finish adding black pieces.

**Expected Output**:
- The white knight cannot capture any black pieces.

``` plaintext
Enter white piece (rook or knight) and position (e.g., 'rook a1'): knight b1
knight added at b1.
Enter black piece (rook or knight) and position (or 'done' to finish): Knight   H8
knight added at h8.
Enter black piece (rook or knight) and position (or 'done' to finish): rOOK   G8
rook added at g8.
Enter black piece (rook or knight) and position (or 'done' to finish): knIgHT       h7
knight added at h7.
Enter black piece (rook or knight) and position (or 'done' to finish): done
The white knight cannot capture any black pieces.
```
### Scenario 2: Invalid Position Input

**Description**: User inputs an invalid position for the white piece.

**Option 1 - Invalid Position**:
1. Run the program.
2. Enter `rook j1` when prompted for the white piece and position.

**Expected Output**:
- Invalid position. Please use format `a1` to `h8`.
  
```
Enter white piece (rook or knight) and position (e.g., 'rook a1'): rook j1
Error: Invalid position. Please use format 'a1' to 'h8'. Please try again.
```
**Option 2 - Invalid Piece**:
1. Run the program.
2. Enter `queen a1` when prompted for the white piece and position.

**Expected Output**:
- Invalid piece. Please choose from: `rook, knight`.
  
``` plaintext
Enter white piece (rook or knight) and position (e.g., 'rook a1'): queen a1
Error: Invalid piece. Please choose from: rook, knight Please try again.
```

**Option 3 - Occupied Position**:

1. Run the program.
2. Enter `rook a1` when prompted for the white piece and position.
3. Enter `knight b2` for the 1st black piece.
4. Enter `rook b2` for the 2nd black piece.

**Expected Output**:
- Position `b2` is already occupied.

```
Enter white piece (rook or knight) and position (e.g., 'rook a1'): rook a1
rook added at a1.
Enter black piece (rook or knight) and position (or 'done' to finish): knight b2
knight added at b2.
Enter black piece (rook or knight) and position (or 'done' to finish): rook b2
Position b2 is already occupied.
```

### Scenario 3: Maximum Black Pieces

**Description**: User adds the maximum number of black pieces (16).

1. Run the program.
2. Enter `rook a1` when prompted for the white piece and position.
3. Enter 16 different black pieces and positions.
4. Enter `done` after adding 16 black pieces.

**Expected Output**:
- Program should end after the 16th black piece is placed

### Scenario 4: Typing `done` Before Adding Any Black Pieces

**Description**: User tries to type in `done` without adding any black pieces.

**Steps**:
1. Run the program.
2. Enter `rook a1` when prompted for the white piece and position.
3. Enter `done` when prompted for the black piece and position.

**Expected Output**:
- You must add at least one black piece.

``` plaintext
Enter white piece (rook or knight) and position (e.g., 'rook a1'): rook a1
rook added at a1.
Enter black piece (rook or knight) and position (or 'done' to finish): done
You must add at least one black piece.
```


## Error Handling

The program includes error handling for:
- Invalid piece types
- Invalid board positions
- Attempting to place pieces on occupied squares
- Trying to finish the game without placing any black pieces
- Typing the input in capital letters or making too many spaces between input components 

Examples of error messages and error handling:

```plaintext
Error: Invalid piece. Please choose from: rook, knight. Please try again.
Error: Invalid position. Please use format 'a1' to 'h8'. Please try again.
Position b2 is already occupied.
You must add at least one black piece.
The program converts the input to lowercase, strips leading and trailing spaces, and splits it into components, ensuring that extra spaces or capital letters do not cause issues. 
```

## Possible Improvements in the Program

- This program can be extended to include additional chess pieces.
- A graphical user interface may be added for easier interaction.
- Full chess game logic could be implemented.






