import socket
import threading

HOST = '127.0.0.1'
PORT = 3000


def receive_message(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            print(message.decode())
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    threading.Thread(target=receive_message, args=(client,)).start()
    
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client.send(message.encode())
    client.close()

if __name__ == '__main__':
    start_client()
