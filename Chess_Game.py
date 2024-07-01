import string

def is_valid_position(position):
    """
    Check if a given position is valid on a chessboard.

    Args:
        position (str): A string representing a position on the chessboard (e.g., 'a1', 'h8').

    Returns:
        bool: True if the position is valid, False otherwise.
    """
    return (
        len(position) == 2 and position[0] in "abcdefgh" and position[1] in "12345678"
    )

def get_piece_moves(piece, position):
    """
    Get all possible moves for a given piece at a given position.

    Args:
        piece (str): The type of piece (e.g., 'white_rook', 'black_knight').
        position (str): The current position of the piece (e.g., 'a1', 'h8').

    Returns:
        list: A list of all possible moves for the piece.
    """
    row, col = int(position[1]), ord(position[0]) - ord("a") + 1
    moves = []

    if piece.endswith("rook"):
        # Rook moves: horizontal and vertical
        for i in range(1, 9):
            moves.append(f"{chr(ord('a') + col - 1)}{i}")  # Vertical moves
            moves.append(f"{chr(ord('a') + i - 1)}{row}")  # Horizontal moves
    elif piece.endswith("knight"):
        # Knight moves: L-shaped
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2),
        ]
        for dx, dy in knight_moves:
            new_col, new_row = col + dx, row + dy
            if 1 <= new_col <= 8 and 1 <= new_row <= 8:
                moves.append(f"{chr(ord('a') + new_col - 1)}{new_row}")

    # Remove the original position from possible moves
    return list(set(moves) - {position})

def can_capture(white_piece, white_pos, black_piece, black_pos):
    """
    Check if a white piece can capture a black piece.

    Args:
        white_piece (str): The type of white piece.
        white_pos (str): The position of the white piece.
        black_piece (str): The type of black piece.
        black_pos (str): The position of the black piece.

    Returns:
        bool: True if the white piece can capture the black piece, False otherwise.
    """
    return black_pos in get_piece_moves(white_piece, white_pos)

def add_piece(board, piece, position):
    """
    Add a piece to the board at the specified position.

    Args:
        board (dict): The current state of the board.
        piece (str): The type of piece to add.
        position (str): The position to add the piece to.

    Returns:
        tuple: (bool, str) indicating success and a message.
    """
    if not is_valid_position(position):
        return False, "Invalid position. Please use format 'a1' to 'h8'."
    if board.get(position):
        return False, f"Position {position} is already occupied."
    board[position] = piece
    return True, f"{piece} added at {position}."

def get_valid_input(prompt, valid_pieces, is_white_piece=False):
    """
    Get and validate user input for piece placement.

    Args:
        prompt (str): The prompt to display to the user.
        valid_pieces (list): List of valid piece types.
        is_white_piece (bool): Whether the input is for a white piece.

    Returns:
        list: A list containing the piece type and position, or ['done'] to finish.
    """
    while True:
        try:
            user_input = input(prompt).lower().strip().split()
            if len(user_input) == 1 and user_input[0] == "done" and not is_white_piece:
                return user_input
            if len(user_input) != 2:
                raise ValueError("Input must contain two parts: piece and position.")
            piece, position = user_input
            if piece not in valid_pieces:
                raise ValueError(f"Invalid piece. Please choose from: {', '.join(valid_pieces)}")
            if not is_valid_position(position):
                raise ValueError("Invalid position. Please use format 'a1' to 'h8'.")
            return user_input
        except ValueError as e:
            print(f"Error: {e} Please try again.")

def visualize_board(board, highlighted_positions=None):
    """
    Create a visual representation of the chessboard.

    Args:
        board (dict): The current state of the board.
        highlighted_positions (list): Positions to highlight (e.g., possible moves).

    Prints:
        A visual representation of the chessboard with pieces and highlighted positions.
    """
    if highlighted_positions is None:
        highlighted_positions = []
    
    # Define piece symbols for visualization
    piece_symbols = {
        "white_rook": "WR", "white_knight": "WN",
        "black_rook": "BR", "black_knight": "BN"
    }
    
    # Print the top border of the board
    print("  ┌───┬───┬───┬───┬───┬───┬───┬───┐")
    
    # Print each row of the board
    for row in range(8, 0, -1):
        print(f"{row} │", end="")
        for col in string.ascii_lowercase[:8]:
            pos = f"{col}{row}"
            if pos in board:
                piece = piece_symbols[board[pos]]
            elif pos in highlighted_positions:
                piece = "· "
            else:
                piece = "  "
            print(f" {piece}│", end="")
        print()
        if row > 1:
            print("  ├───┼───┼───┼───┼───┼───┼───┼───┤")
    
    # Print the bottom border and column labels
    print("  └───┴───┴───┴───┴───┴───┴───┴───┘")
    print("    a   b   c   d   e   f   g   h  ")

def main():
    """
    Main function to run the chess game simulation.
    """
    board = {}
    valid_pieces = ["rook", "knight"]

    # Add white piece
    white_prompt = f"Enter white piece ({' or '.join(valid_pieces)}) and position (e.g., 'rook a1'): "
    while True:
        white_input = get_valid_input(white_prompt, valid_pieces, is_white_piece=True)
        success, message = add_piece(board, f"white_{white_input[0]}", white_input[1])
        print(message)
        if success:
            white_piece, white_pos = f"white_{white_input[0]}", white_input[1]
            break

    # Add black pieces
    black_pieces = []
    black_prompt = f"Enter black piece ({' or '.join(valid_pieces)}) and position (or 'done' to finish): "
    while len(black_pieces) < 16:
        black_input = get_valid_input(black_prompt, valid_pieces)
        if black_input[0] == "done":
            if not black_pieces:
                print("You must add at least one black piece.")
                continue
            break
        success, message = add_piece(board, f"black_{black_input[0]}", black_input[1])
        print(message)
        if success:
            black_pieces.append((f"black_{black_input[0]}", black_input[1]))

    # Check captures and visualize
    capturable_pieces = []
    for black_piece, black_pos in black_pieces:
        if can_capture(white_piece, white_pos, black_piece, black_pos):
            capturable_pieces.append(f"{black_piece} at {black_pos}")

    # Display the final board state
    print("\nFinal board state:")
    visualize_board(board, get_piece_moves(white_piece, white_pos))
    
    # Report capturable pieces
    if capturable_pieces:
        print(f"\nThe {white_piece} can capture: {', '.join(capturable_pieces)}")
    else:
        print(f"\nThe {white_piece} cannot capture any black pieces.")

if __name__ == "__main__":
    main()