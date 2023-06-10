
class Packet():
    def __init__(self, s:str):
        self.original = s
        self.packet = None
        self.val = []
        self.decipher(s)
    
    def decipher(self, s:str):
        if s[0] == "[":
            self.packet = Packet(s[1:-1])
        else:
            

