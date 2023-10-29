import socket
from typing import Any
from clients.iUnityClient import IUnityClient


class UnityClient(IUnityClient):

    def __init__(self) -> None:
        self.sock = None
        
    def connect(self, host: str, port: int):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        self.sock = sock
        return sock
    
    def send(self, data: Any):
        if not self.sock:
            raise Exception()
        self.sock.sendall(data.encode("UTF-8"))

    def get(self):
        if not self.sock:
            raise Exception()
        return self.sock.recv(1024).decode("UTF-8") 