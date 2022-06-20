import simple_socket


sock = simple_socket.Socket("0.0.0", 5000)
@sock.set_on_connect
def on_connect(conn):
    print("conn!")
    conn.socket.send(b"Hello!")

@sock.set_on_recv
def on_recv(data):
    print(data.decode("utf-8"))

while True:
    pass
