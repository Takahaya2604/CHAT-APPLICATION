# CHAT-APPLICATION
💬 Live Chat Application (Python)

A real-time command-line chat application built using Python with a simple client-server architecture.

This project demonstrates socket programming and multi-threading to enable two or more users to exchange messages in real time.

🚀 Project Overview

The Live Chat Application allows:

🔗 Multiple clients to connect to a server

💬 Real-time message exchange

🧵 Multi-threaded communication

🖥️ Command-line interface interaction

🌐 TCP socket-based networking

This project focuses on understanding networking fundamentals and backend communication concepts.

🛠 Built With

Python 3

Built-in libraries:

socket

⚙️ How It Works

The server listens for incoming client connections.

Clients connect to the server using TCP sockets.

Each client runs two threads:

One for sending messages

One for receiving messages

The server broadcasts messages to connected clients.

threading

No external libraries required.
