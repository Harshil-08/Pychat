# Pychat

Pychat is a simple Python-based command-line interface (CLI) chat application that allows users to communicate with each other in a text-based environment. This project is ideal for learning about socket programming, multithreading, and building basic networking applications.

## Features

- Real-time Messaging: Exchange messages in real-time with other users in the same chatroom.
- Chatroom Identification: Users can join or create chatrooms with unique names.
- Password Protection: Each chatroom is protected by a password to ensure privacy.
- Multi-user Support: Supports multiple users in each chatroom, though usernames are not unique.

## Prerequisites

- Python 3.6 or later

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Harshil-08/Pychat.git
   cd Pychat
   ```
2. **Install Dependencies:**   
   This project uses standard Python libraries (socket and threading), which come with Python and require no additional installation.

## Usage
1. **Start the Server:**   
   Open a terminal and navigate to the project directory. Run:
   ```bash
    python server.py   
    ```   
   This command starts the chat server.   
2. **Connect as a Client:**   
   Open a new terminal window and navigate to the project directory. Run:  
    ```bash
    python client.py
    ```   
   Follow the prompts to enter your name and either create a new chatroom or join an existing one by providing the chatroom name and password.   
