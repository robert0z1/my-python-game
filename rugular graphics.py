import pygame
import chess
import math

# Set up the board
board = chess.Board()

# Set up the colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)

# Set up the size of the squares and the board
SIZE = 80
WIDTH = 8 * SIZE
HEIGHT = 8 * SIZE

turn = chess.WHITE

# Set up the display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Set up font for displaying text
FONT = pygame.font.SysFont('Arial', 30)
def start_menu():
    # Display some text
    screen.fill((255, 255, 255))
    title_text = FONT.render("Chess Game", True, (0, 0, 0))
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
    start_text = FONT.render("Press any key to start", True, (0, 0, 0))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))

    # Update the display
    pygame.display.update()

    # Wait for the player to press a key
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                return

def switch_turn():
    global turn
    turn = chess.WHITE if turn == chess.BLACK else chess.BLACK


def draw_move(start_square, end_square):
    # Get the starting and ending coordinates of the move
    start_x = chess.square_file(start_square) * SIZE + SIZE // 2
    start_y = (7 - chess.square_rank(start_square)) * SIZE + SIZE // 2
    end_x = chess.square_file(end_square) * SIZE + SIZE // 2
    end_y = (7 - chess.square_rank(end_square)) * SIZE + SIZE // 2

    # Compute the coordinates of the arrowhead
    arrow_len = SIZE // 4
    dx = end_x - start_x
    dy = end_y - start_y
    length = math.sqrt(dx**2 + dy**2)
    if length > 0:
        dx /= length
        dy /= length
    arrow_x = end_x - dx * arrow_len
    arrow_y = end_y - dy * arrow_len
    arrow_dx = dy * arrow_len
    arrow_dy = -dx * arrow_len

    # Draw the arrow
    pygame.draw.line(screen, (0, 0, 255), (start_x, start_y), (end_x, end_y), 3)
    pygame.draw.polygon(screen, (0, 0, 255), [(arrow_x, arrow_y), (arrow_x+arrow_dx, arrow_y+arrow_dy), (arrow_x-arrow_dx, arrow_y-arrow_dy)])

def draw_selection(square):
    x = chess.square_file(square) * SIZE
    y = (7 - chess.square_rank(square)) * SIZE
    rect = pygame.Rect(x, y, SIZE, SIZE)
    pygame.draw.rect(screen, (0, 255, 0), rect, 5)

# Define a function to draw the board
def draw_board():
    for row in range(8):
        for col in range(8):
            color = GRAY if (row+col)%2==0 else WHITE
            pygame.draw.rect(screen, color, (col*SIZE, row*SIZE, SIZE, SIZE))

# Define a function to draw the pieces
def draw_pieces():
    for row in range(8):
        for col in range(8):
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece is not None:
                font_color = BLUE if piece.color == chess.WHITE else RED
                piece_text = FONT.render(piece.symbol(), True, font_color)
                screen.blit(piece_text, (col*SIZE+(SIZE//2)-piece_text.get_width()//2,
                                         row*SIZE+(SIZE//2)-piece_text.get_height()//2))

# Define a function to update the display
def update_display():
    draw_board()
    draw_pieces()
    pygame.display.update()

def online_side(move):
    import socket
    import threading

    class ChatClient:
        def __init__(self):
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(("localhost", 5000))

        def receive_message(self):
            message = self.client_socket.recv(1024)
            return message.decode()

        def send_message(self):
            self.client_socket.send(move.encode())

        def run(self):
            receive_thread = threading.Thread(target=self.receive_message)
            receive_thread.start()

            send_thread = threading.Thread(target=self.send_message)
            send_thread.start()

    if __name__ == "__main__":
        client = ChatClient()
        client.run()
    ChatClient()

# Define a function to handle mouse events
def handle_mouse_event(event):
    global selected_piece, selected_piece_rect

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        col = x // SIZE
        row = y // SIZE
        square = chess.square(col, 7 - row)

        piece = board.piece_at(square)
        if piece is not None and piece.color == turn:
            selected_piece = square
            selected_piece_rect = pygame.Rect(col*SIZE, row*SIZE, SIZE, SIZE)

    elif event.type == pygame.MOUSEMOTION:
        if selected_piece is not None:
            selected_piece_rect.center = event.pos

    elif event.type == pygame.MOUSEBUTTONUP:
        if selected_piece is not None:
            x, y = event.pos
            col = x // SIZE
            row = y // SIZE
            square = chess.square(col, 7 - row)

            move = chess.Move(selected_piece, square)
            if move in board.legal_moves:
                board.push(move)
                draw_move(selected_piece, square)
                selected_piece = None
                switch_turn()
            else:
                selected_piece = None

    elif event.type == pygame.MOUSEWHEEL:
        # rotate the board if the mousewheel is used
        draw_board()
        draw_pieces()
        if event.y > 0:
            board.turn = chess.WHITE
        else:
            board.turn = chess.BLACK

    # Update the display
    draw_board()
    draw_pieces()
    if selected_piece is not None:
        screen.blit(FONT.render(board.piece_at(selected_piece).symbol(), True, BLUE if turn == chess.WHITE else RED), selected_piece_rect)
    pygame.display.update()




# Set up the main game loop
selected_piece = None
start_menu()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        handle_mouse_event(event)

    # Update the display
    update_display()
