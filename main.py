# import os
from VotingSystem import *

from tinyec import registry
import DES
import hashlib, secrets, binascii

from bot import *

from Crypto.Cipher import *




m = 3
Voting_System = VotingSystem("brainpoolP256r1")
Voting_System.getStatus()


while(m > 0):
    print("Hello and welcome to the Secure Voting System \n")
    id = input("Please enter your ID : \n")
    phoneNum = input("Please Enter your Phone Number : \n")

    Voting_System.addVoter(id,phoneNum)
    
    # Voting_System.getVoters()
    Voting_System.getStatus()


    m -= 1

Voting_System.getStatus()



