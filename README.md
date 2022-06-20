
# simple-socket
Python module for communicating with sockets


## About

When I first started with sockets in Python, I was looking all over the place for how to use them. This package is a high level version of the built-in socket package. It takes care of threads and binary encoding.  

My hopes for this project in the future are:
 - Image sharing
 - Sound sharing
 - File sharing
 - Automatic buffer size

 ## Installation

 ```bash
 git clone  https://github.com/simplyrohan/simple-socket.git
 ```  

## Usage
### Server Side
```python
import simple_socket


# Initilize Socket. This will do many things at once:
#  - Initilize low-level socket
#  - Automaticly connect as server or client (unless type is specified already)
#  - Defines threads and other socket dependencies
sock = simple_socket.Socket("localhost", 5000)

# Set handler for incoming connections. Is not neccesary if you only need to listen to sockets as connections will automatically be handled
@sock.set_on_connect
def on_connect(conn):
    print("Connected!")
    conn.send("Hello!")

# Set handler for incoming data, which is also not necessary if you only need to send data to sockets
@sock.set_on_recv
def on_recv(data):
    print(data)

# Program loop has different contents depending on whether or not the script is server-side or client-side.
# Server-side programs call the method to accept incoming connections and create a thread for them
while True:
    sock.accept()

# Close main socket and all other connections when program loop is interrupted
sock.close()

```
For more, go to [Examples](https://github.com/simplyrohan/simple-socket/tree/main/Examples)

## Contibutes
I'm open to contributes! If you know any features that can be implemented or simply found a bug, I'll gladly merge a pull request!

## Notes
I'm still relativley new to sockets and for that matter, the entire Python language. So if you are running into an issue, please report an issue, as this package is not nearly complete.

