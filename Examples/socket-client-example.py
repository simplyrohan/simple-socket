import simple_socket

sock = simple_socket.Socket("localhost", 5000)
@sock.set_on_recv
def on_recv(data):
    print(data)
    sock.socket.send(b"Hi!")

sock.run()

while True:
    pass
sock.close()