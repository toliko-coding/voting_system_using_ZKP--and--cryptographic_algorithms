class Verifier:

    total_packets = 27
    valid = 0
    confidence = 0

    def __init__(self,conf):
        self.confidence = int(conf)
        
    def getValid(self):
        return self.valid

    def approvePacket(self):
        self.valid = self.valid + 1
    
    def getConfidance(self):
        return self.confidence / 100

    def isProff(self):
        temp = self.valid / self.total_packets
        c = self.getConfidance()
        return temp >= c

    def getapprlvl(self):
        
        return self.valid / self.total_packets
        
