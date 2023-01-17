
from tinyec import registry
import secrets
from bot import *
import DES
import hashlib, secrets, binascii
from Crypto.Cipher import *
import os




class Voter(object):

    

    def __init__(self ,id,phone, curveid):
        self.curve = registry.get_curve(curveid)
        self.p_key = secrets.randbelow(self.curve.field.n)
        self.veriffied = False
        self.voted = False
        self.id = id
        self.phone = phone
        self.confidance = 20
        self.myVote = "None"


    def get_P_key(self):
        return self.p_key
        
    def updateCenter(self,c):
        self.center = c

    def getCenter(self):
        return self.center


    def getMyVote(self):
        return self.myVote

    def getID(self):
        return str(self.id)
    
    def getPhone(self):
        return str(self.phone)

  

    def Veriffie(self):
        b = bot()
        b.send(self.getPhone(),str(self.get_P_key()))

        valid = 0
        print("Please Enter your SMS-key ( After each char press Enter )")
        for c in str(self.get_P_key()):
            inp = input()
            if inp == c:
                valid +=1

            os.system("clear")
            print(valid / 77 * 100,"%" ,"/20%")
            if valid / 77 * 100 > 20:
                self.veriffied = True
                return True
        
        return False
            

    def isVoted(self):
        return self.voted
    
    def UpdateVoted(self):
        self.voted = True

    def getShKey(self):
        return self.p_key * self.curve.g


    def makeVote(self,choose):

        if choose == "Republic":
            msg = b'Republic' 
        
        if choose == "Democrat":
            msg = b'Democrat' 


        
        # msg = b'the book that changeed my life. J.K Rowling' 
            
        print("original msg:", msg)
        print()
        # privKey = secrets.randbelow(curve.field.n)
        # pubKey = privKey * curve.g

        # print(privKey)

        encryptedMsg = DES.encrypt_ECC(msg, self.getShKey())
        encryptedMsgObj = {
            'ciphertext': binascii.hexlify(encryptedMsg[0]),
            'nonce': binascii.hexlify(encryptedMsg[1]),
            'authTag': binascii.hexlify(encryptedMsg[2]),
            'ciphertextPubKey': hex(encryptedMsg[3].x) + hex(encryptedMsg[3].y % 2)[2:]
        }
        print("encrypted msg:", encryptedMsgObj)
        print()
        self.myVote = encryptedMsg
        self.UpdateVoted()



        # decryptedMsg = DES.decrypt_ECC(encryptedMsg, privKey)
        # print("decrypted msg:", decryptedMsg)
            
        
   


