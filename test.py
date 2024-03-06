import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 300
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tic Tac Toe")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the board
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# Define the players
player1 = 'X'
player2 = 'O'
current_player = player1

# Define the font
font = pygame.font.Font(None, 100)

# Define the winner
winner = None

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Calculate the cell position based on the mouse click
            cell_x = mouse_x // (window_width // 3)
            cell_y = mouse_y // (window_height // 3)

            # Check if the cell is empty and there is no winner yet
            if board[cell_y][cell_x] == '' and not winner:
                # Update the board with the current player's symbol
                board[cell_y][cell_x] = current_player

                # Check for a winner
                if (board[0][0] == board[0][1] == board[0][2] == current_player or
                    board[1][0] == board[1][1] == board[1][2] == current_player or
                    board[2][0] == board[2][1] == board[2][2] == current_player or
                    board[0][0] == board[1][0] == board[2][0] == current_player or
                    board[0][1] == board[1][1] == board[2][1] == current_player or
                    board[0][2] == board[1][2] == board[2][2] == current_player or
                    board[0][0] == board[1][1] == board[2][2] == current_player or
                    board[0][2] == board[1][1] == board[2][0] == current_player):
                    winner = current_player

                # Switch to the next player
                if current_player == player1:
                    current_player = player2
                else:
                    current_player = player1

    # Clear the window
    window.fill(WHITE)

    # Draw the board
    for row in range(3):
        for col in range(3):
            # Calculate the cell position
            cell_x = col * (window_width // 3)
            cell_y = row * (window_height // 3)

            # Draw the cell
            pygame.draw.rect(window, BLACK, (cell_x, cell_y, window_width // 3, window_height // 3), 1)

            # Draw the symbol in the cell
            symbol = font.render(board[row][col], True, BLACK)
            symbol_rect = symbol.get_rect(center=(cell_x + window_width // 6, cell_y + window_height // 6))
            window.blit(symbol, symbol_rect)

    # Check if there is a winner
    if winner:

        # Display the winner
        winner_text = font.render(f"Player {winner} wins!", True, BLACK)
        winner_rect = winner_text.get_rect(center=(window_width // 2, window_height // 2))
        window.blit(winner_text, winner_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

