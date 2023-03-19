import chess
import socket

# Initialize the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)
print('Server listening on {}:{}'.format(*server_address))

# Wait for a connection
print('Waiting for a connection...')
connection, client_address = sock.accept()
print('Connection from', client_address)

# Create the chess board
board = chess.Board()

# Main game loop
while True:
    # Receive the client's move
    data = connection.recv(1024)
    if data:
        move_str = data.decode()
        move = chess.Move.from_uci(move_str)
        board.push(move)

    # Send the current board state to the client
    board_str = str(board) + '\n'
    connection.sendall(board_str.encode())
