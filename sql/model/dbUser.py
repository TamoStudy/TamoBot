class DBUser():
    def __init__(self, id: int, drole: str, tokens: int, stime: int, zoneid: str, hex: str, feat: str, trivia: int):
        self.id = id
        self.drole = drole
        self.tokens = tokens
        self.stime = stime
        self.zoneid = zoneid
        self.hex = hex
        self.feat = feat
        self.trivia = trivia