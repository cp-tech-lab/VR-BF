from clients import UnityClient

class UnityService:
    
    def __init__(self, host: str, port: int):
        self.client = UnityClient()
        self.client.connect(host=host, port=port)

    def send_height(self, h: float):
        pos = [h, 0, 0]
        self.client.send(','.join([str(x) for x in pos]))


