import socket, threading

class Socket:
    def __init__(self, host, port, max_connections=5, is_host=None):
        self.socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.max_connections = max_connections

        self.host = host
        self.port = port

        self.type = None

        if is_host == None:
            try:
                self.socket.bind((host, port))
                self.socket.listen(self.max_connections)
                self.type = "host"

            except OSError:
                self.type = "client"


        elif is_host is True:
            self.socket.bind((host, port))
            self.socket.listen(self.max_connections)
            self.type = "host"

        elif is_host is False:
            self.type = "client"

        self.connections = []
        
        self.on_recv = self.default_on_recv
        self.on_connect = self.default_on_connect


    def accept(self):
        if self.type == "host":
            conn, addr = self.socket.accept()
            connthread = threading.Thread(target=self._listen, args=[conn])
            connthread.start()
            self.connections.append(conn)

    
    def _listen(self, conn=None):
        if conn is None:
            conn = self.socket
        running = True
        self.on_connect(conn)
        while running:
            data = conn.recv(1024)
            if data == 0:
                self.connections.pop(self.connections.index(conn))
                conn.close()
                break
                
            self.on_recv(data.decode("utf-8"))



    def default_on_recv(self, data):
        pass

    def default_on_connect(self, conn):
        pass

    def set_on_recv(self, wrapper):
        self.on_recv = wrapper
    
    def set_on_connect(self, wrapper):
        self.on_connect = wrapper

    def close(self):
        for conn in self.connections:
            conn.close()
        self.socket.close()
    
    def run(self):
        if self.type == "client":
            self.socket.connect((self.host, self.port))
            self._listen()
