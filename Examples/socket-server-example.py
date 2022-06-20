import simple_socket


sock = simple_socket.Socket("localhost", 5000)
@sock.set_on_connect
def on_connect(conn):
    conn.send(b"Hello!")

@sock.set_on_recv
def on_recv(data):
    print(data)


while True:
    sock.accept()

sock.close()
