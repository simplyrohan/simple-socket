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

# Set handler for incoming data, which is also not neccessary if you only need to send data to sockets
@sock.set_on_recv
def on_recv(data):
    print(data)

# Program loop has different contents depending on whether or not script is server-side or client-side.
# Server-side programs call the method to accept incoming connections and create a thread for them
while True:
    sock.accept()

# Close main socket and all other connections when program loop is interrupted
sock.close()