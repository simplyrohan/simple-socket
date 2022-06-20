

# Initilize Socket. This will do many things at once:
#  - Initilize low-level socket
#  - Automaticly connect as server or client (unless type is specified already)
#  - Defines threads and other socket dependencies
sock = simple_socket.Socket("localhost", 5000)


# Set handler for incoming data, which is also not neccessary if you only need to send data to server
@sock.set_on_recv
def on_recv(data):
    print(data)
    sock.socket.send("Hi!")

sock.run()


# Program loop has different contents depending on whether or not script is server-side or client-side.
# Client-side programs don't need anything in the program loop as they don't handle incoming connections to the server
while True:
    pass

# Close main socket and all other connections when program loop is interrupted
sock.close()