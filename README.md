# UDP-Ping-Pong

This project demonstrates basic client-server communication over UDP in Python.  
The client sends "PING" messages to the server, and the server responds with "PONG" or simulates packet loss. This assignment was built for CSCE 3530 (Computer Networks).

## Files
- **Client.py** – UDP client that sends 10 ping requests and prints responses or timeouts.  
- **Server.py** – UDP server that listens for pings, responds with "PONG," and randomly drops packets to simulate unreliable networks.  

## Features
- UDP socket programming in Python
- Client with timeout handling
- Server with random packet loss simulation
- Example of request-response protocol

## Requirements
- Python 3.6+
- Standard `socket` and `random` libraries

## How to Run
1. Start the server:
   ```bash
   python server.py
1. In another terminal, run the client:
   ```bash
   python client.py
