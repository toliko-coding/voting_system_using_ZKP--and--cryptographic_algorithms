
import copy
from tinyec import registry
import secrets
from Voter import *
class VotingSystem:

    

    def __init__(self,curveid):
        self.curveID = curveid
        self.curve = registry.get_curve(curveid)
        self.R = 0
        self.D = 0
        self.voters = []

        

    def getCurveId(self):
        return self.curveID

    def setCurve(self,curveid):
        self.curveID = curveid
        self.curve = registry.get_curve(curveid)

    def incR(self):
        self.R += 1

    def incD(self):
        self.D +=1

    def getStatus(self):
        print("Democrat : ",self.D,"\nRepublic : ",self.R )
        

    def findVoterById(self,id):
        c=0
        for v in self.voters:
            if v.getID() == id:
                return c
            else:
                c+=1

    def decrypt(self,key,msg) :
        decryptedMsg = DES.decrypt_ECC(msg, key)
        return decryptedMsg

    def addVoter(self, id , phone):
        excist = False
        for i in self.voters:
            if i.getID() == id:
                excist = True
                index = self.findVoterById(id)
                print("We see that you have already try to vote , Please Verrife with SMS-key to vote again")
                if(self.voters[index].Veriffie()):
                    print("ZNK is good !\n")
                    lastchoose = self.decrypt(self.voters[index].get_P_key() , self.voters[index].getMyVote())
                    if lastchoose == b'Democrat':
                        self.D = self.D - 1
                    
                    if lastchoose == b'Republic':
                        self.R = self.R - 1
                        
                    print("LASSST choose = " , lastchoose)
                    center = input("Please Choose Voting Center ( 1 , 2 )\n")
                    choose = input("Please Choose who you want to vote (Democrat , Republic)")
                    if choose == "Democrat":
                        self.incD()
                        print("inc")
                    else:
                        self.incR()
                        print("inc")
                        

                    self.voters[-1].makeVote(choose)
                    self.voters[-1].updateCenter(center)
                    print("Thank You\n")

        if excist == False:       
            self.voters.append(Voter(id,phone,self.curveID))
            if(self.voters[-1].Veriffie()):
                print("ZNK is good !\n")
                center = input("Please Choose Voting Center ( 1 , 2 )\n")
                choose = input("Please Choose who you want to vote (Democrat , Republic)")
                if choose == "Democrat":
                    self.incD()
                    print("inc")
                else:
                    self.incR()
                    print("inc")
                    

                self.voters[-1].makeVote(choose)
                self.voters[-1].updateCenter(center)
                print("Thank You\n")

    def getVoters(self):
        for i in self.voters:
            print(i.getID())
        

    

        
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
        

