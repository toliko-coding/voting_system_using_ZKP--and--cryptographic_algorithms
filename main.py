import pySudoku
# import os
from VotingSystem import *
from Prover import *
from Voter import *

from Client import *
from Server import *
import random
from tinyec import registry
import DES
import hashlib, secrets, binascii

from bot import *

from Crypto.Cipher import *




m = 3
Voting_System = VotingSystem("brainpoolP256r1")
Voting_System.getStatus()
# toli = Voter(324413756,547905391,Voting_System.getCurveId())
# print(toli.get_P_key())
# print(toli.getShKey())

# toli.makeVote("Democrat")
# print(toli.getMyVote())


# decryptedMsg = DES.decrypt_ECC(toli.getMyVote(), toli.get_P_key())
# print("decrypted msg:", decryptedMsg)

while(m > 0):
    print("Hello and welcome to the Secure Voting System \n")
    id = input("Please enter your ID : \n")
    phoneNum = input("Please Enter your Phone Number : \n")

    Voting_System.addVoter(id,phoneNum)
    
    Voting_System.getVoters()
    Voting_System.getStatus()


    m -= 1

Voting_System.getStatus()

# BOT = bot()
# BOT.send(str(547905391),"wow1123")

