# Description: This code generates a checkerboard pattern using NumPy and Matplotlib.
# Use GUI 
"""
import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt # Importing Matplotlib for plotting

def plot_checkerboard(size=8):  # Function to plot a checkerboard pattern
    board = np.indices((size, size)).sum(axis=0) % 2    # Create a checkerboard pattern using NumPy

    plt.figure(figsize=(6, 6))  # Set the figure size
    plt.imshow(board, cmap='gray', interpolation='nearest') # Display the checkerboard pattern

    plt.xticks([])  # Remove x-ticks
    plt.yticks([])  # Remove y-ticks
    plt.title("Checkerboard Pattern", fontsize=14, fontweight='bold')   # Set the title of the plot

    plt.show()  # Show the plot

plot_checkerboard(8)    # Call the function to plot a checkerboard of size 8x8
"""

# Use matplotlib to create a simple plot'
"""
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend for image generation

import numpy as np
import matplotlib.pyplot as plt

def plot_checkerboard(size=8, filename='checkerboard.png'):
    board = np.indices((size, size)).sum(axis=0) % 2

    plt.figure(figsize=(6, 6))
    plt.imshow(board, cmap='gray', interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
    plt.title("Checkerboard Pattern", fontsize=14, fontweight='bold')

    plt.savefig(filename, bbox_inches='tight')
    plt.close()  # Free up memory

plot_checkerboard(8)
"""
# This code generates a chessboard pattern with chess pieces using Unicode symbols.
"""
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend for image generation

import numpy as np
import matplotlib.pyplot as plt

def plot_chessboard(filename='chessboard.png'):
    size = 8
    board = np.indices((size, size)).sum(axis=0) % 2

    # Unicode chess symbols
    white_pieces = {
        'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙'
    }
    black_pieces = {
        'K': '♚', 'Q': '♛', 'R': '♜', 'B': '♝', 'N': '♞', 'P': '♟'
    }

    # Create an empty 8x8 array for pieces
    pieces = [['' for _ in range(size)] for _ in range(size)]

    # Setup black pieces
    pieces[0] = [black_pieces['R'], black_pieces['N'], black_pieces['B'], black_pieces['Q'],
                 black_pieces['K'], black_pieces['B'], black_pieces['N'], black_pieces['R']]
    pieces[1] = [black_pieces['P']] * size

    # Setup white pieces
    pieces[6] = [white_pieces['P']] * size
    pieces[7] = [white_pieces['R'], white_pieces['N'], white_pieces['B'], white_pieces['Q'],
                 white_pieces['K'], white_pieces['B'], white_pieces['N'], white_pieces['R']]

    # Plot board
    plt.figure(figsize=(6, 6))
    plt.imshow(board, cmap='gray', interpolation='nearest')

    # Add pieces to the board
    for row in range(size):
        for col in range(size):
            if pieces[row][col] != '':
                plt.text(col, row, pieces[row][col],
                         ha='center', va='center', fontsize=28, color='black' if board[row, col] else 'white')

    # Clean up axes
    plt.xticks([])
    plt.yticks([])
    plt.title("Chessboard with Pieces", fontsize=14, fontweight='bold')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

plot_chessboard()
"""
# This code generates a chessboard animation using Matplotlib and imageio.
"""
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

def pos_to_index(pos):
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    return row, col

def create_chess_frame(pieces, frame_name):
    board = np.indices((8, 8)).sum(axis=0) % 2
    plt.figure(figsize=(5, 5))
    plt.imshow(board, cmap='gray')

    for row in range(8):
        for col in range(8):
            piece = pieces[row][col]
            if piece:
                plt.text(col, row, piece, fontsize=26, ha='center', va='center',
                         color='black' if board[row, col] else 'white')

    # Coordinates
    for i in range(8):
        plt.text(i, 8 - 0.5, chr(ord('a') + i), ha='center', va='center', fontsize=10, color='red')
        plt.text(-0.5, i, str(8 - i), ha='center', va='center', fontsize=10, color='red')

    plt.xticks([]), plt.yticks([])
    plt.xlim(-0.5, 7.5), plt.ylim(7.5, -0.5)
    plt.savefig(frame_name, bbox_inches='tight')
    plt.close()

def animate_chess_moves(moves, filename='chess_animation.gif'):
    # Initial setup
    board = [['' for _ in range(8)] for _ in range(8)]
    board[6] = ['♙'] * 8
    board[1] = ['♟'] * 8
    board[7][4] = '♔'
    board[0][4] = '♚'
    board[0][6] = '♞'
    board[7][6] = '♘'

    frame_files = []
    frame_count = 0

    # Initial frame
    frame_name = f"frame_{frame_count:02d}.png"
    create_chess_frame(board, frame_name)
    frame_files.append(frame_name)
    frame_count += 1

    # Execute each move and capture frame
    for move in moves:
        start, end = move
        r1, c1 = pos_to_index(start)
        r2, c2 = pos_to_index(end)
        board[r2][c2] = board[r1][c1]
        board[r1][c1] = ''
        frame_name = f"frame_{frame_count:02d}.png"
        create_chess_frame(board, frame_name)
        frame_files.append(frame_name)
        frame_count += 1

    # Create GIF
    with imageio.get_writer(filename, mode='I', duration=1.0) as writer:
        for f in frame_files:
            image = imageio.imread(f)
            writer.append_data(image)

    # Cleanup
    for f in frame_files:
        os.remove(f)

# Example move list: knight from g8 to f6, pawn e2 to e4
moves = [('g8', 'f6'), ('e2', 'e4'), ('d7', 'd5'), ('f1', 'c4')]
animate_chess_moves(moves)
"""
# combines FEN parsing and chess move animation:
"""
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

# Mapping for FEN to Unicode chess pieces
FEN_PIECE_UNICODE = {
    'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
    'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
}

def parse_fen(fen):
    # Converts a FEN string to a board array (8x8)
    board = []
    rows = fen.split()[0].split('/')
    for row in rows:
        row_data = []
        for char in row:
            if char.isdigit():
                row_data.extend([''] * int(char))
            else:
                row_data.append(FEN_PIECE_UNICODE.get(char, ''))
        board.append(row_data)
    return board

def pos_to_index(pos):
    col = ord(pos[0].lower()) - ord('a')
    row = 8 - int(pos[1])
    return row, col

def create_chess_frame(pieces, frame_name):
    board_pattern = np.indices((8, 8)).sum(axis=0) % 2
    plt.figure(figsize=(5, 5))
    plt.imshow(board_pattern, cmap='gray')

    for row in range(8):
        for col in range(8):
            piece = pieces[row][col]
            if piece:
                plt.text(col, row, piece, fontsize=26, ha='center', va='center',
                         color='black' if board_pattern[row, col] else 'white')

    # Coordinates
    for i in range(8):
        plt.text(i, 8 - 0.5, chr(ord('a') + i), ha='center', va='center', fontsize=10, color='red')
        plt.text(-0.5, i, str(8 - i), ha='center', va='center', fontsize=10, color='red')

    plt.xticks([]), plt.yticks([])
    plt.xlim(-0.5, 7.5), plt.ylim(7.5, -0.5)
    plt.savefig(frame_name, bbox_inches='tight')
    plt.close()

def animate_chess_moves(fen, moves, filename='chess_animation.gif'):
    board = parse_fen(fen)

    frame_files = []
    frame_count = 0

    # Initial frame
    frame_name = f"frame_{frame_count:02d}.png"
    create_chess_frame(board, frame_name)
    frame_files.append(frame_name)
    frame_count += 1

    # Apply moves one by one
    for move in moves:
        start, end = move
        r1, c1 = pos_to_index(start)
        r2, c2 = pos_to_index(end)
        board[r2][c2] = board[r1][c1]
        board[r1][c1] = ''
        frame_name = f"frame_{frame_count:02d}.png"
        create_chess_frame(board, frame_name)
        frame_files.append(frame_name)
        frame_count += 1

    # Create GIF
    with imageio.get_writer(filename, mode='I', duration=0.8) as writer:
        for f in frame_files:
            image = imageio.imread(f)
            writer.append_data(image)

    # Cleanup
    for f in frame_files:
        os.remove(f)

# === Example Usage ===
fen_string = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 1"
moves_list = [('e2', 'e4'), ('g8', 'f6'), ('d2', 'd4'), ('f6', 'e4')]

animate_chess_moves(fen_string, moves_list, filename='game_from_fen.gif')
"""