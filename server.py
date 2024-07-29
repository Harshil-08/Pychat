import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

chat_rooms = {}

lock = threading.Lock()

def send_message(client, message):
    client.send(message.encode())

def handle_client(client):
    send_message(client, "Welcome! Enter your name: ")
    name = client.recv(1024).decode().strip()
    while True:
        send_message(client, "Enter chat room (create/join): ")
        room_choice = client.recv(1024).decode().strip().lower()
        if room_choice not in ('create', 'join'):
            send_message(client, 'Invalid choice. Please enter "create" or "join".\n')
            continue
        if room_choice == 'create':
            send_message(client, "Enter chat room name: ")
            room_name = client.recv(1024).decode().strip()
            send_message(client, "Enter password for the chat room: ")
            password = client.recv(1024).decode().strip()
            with lock:
                if room_name in chat_rooms:
                    send_message(client, "Chat room already exists. Try another name.\n")
                else:
                    chat_rooms[room_name] = {'password': password, 'members': []}
                    chat_rooms[room_name]['members'].append((client, name))
                    send_message(client, f'Chat room "{room_name}" created and joined.\n')
                    break
        elif room_choice == 'join':
            with lock:
                if not chat_rooms:
                    send_message(client, "No chat rooms available.\n")
                    continue
                available_rooms = '\n'.join(chat_rooms.keys())
                send_message(client, f"Available chat rooms:\n{available_rooms}\nEnter chat room name to join: ")
                room_name = client.recv(1024).decode().strip()
                if room_name not in chat_rooms:
                    send_message(client, 'Invalid room name. Try again.\n')
                    continue
                send_message(client, 'Enter password for the chat room: ')
                password = client.recv(1024).decode().strip()
                if password != chat_rooms[room_name]['password']:
                    send_message(client, 'Incorrect password. Try again.\n')
                    continue
                chat_rooms[room_name]['members'].append((client, name))
                send_message(client, f'Joined chat room "{room_name}".\n')
                break

    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(room_name, f'{name}: {message.decode()}', client)
        except:
            break

    with lock:
        chat_rooms[room_name]['members'].remove((client, name))
        if not chat_rooms[room_name]['members']:
            del chat_rooms[room_name]

    client.close()

def broadcast(room_name, message, sender_socket):
    with lock:
        for client, _ in chat_rooms[room_name]['members']:
            if client != sender_socket:
                try:
                    send_message(client, message)
                except:
                    pass

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f'Server listening on {HOST}:{PORT}')

    while True:
        client, client_address = server_socket.accept()
        print(f'Accepted connection from {client_address}')
        threading.Thread(target=handle_client, args=(client,)).start()

if __name__ == '__main__':
    start_server()
