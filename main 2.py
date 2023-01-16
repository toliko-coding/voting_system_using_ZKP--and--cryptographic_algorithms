
'''
Anatoli Kot 324413756
Eden Barsheshet 203531918
Yuval Varshavsky 207326703
'''

from Verifier import *
from Prover import *
import pySudoku
import os

print()
print()
print("**************************************************************************")
print("**** Hello and Welcome to the Zero-Knowledge Proof Example for Sudoku ****")
print("**************************************************************************")
print()
print("a zero-knowledge proof or zero-knowledge protocol is a method by which one party (the prover) can prove to another party (the verifier) that a given statement is true while the prover avoids conveying any additional information apart from the fact that the statement is indeed true. The essence of zero-knowledge proofs is that it is trivial to prove that one possesses knowledge of certain information by simply revealing it; the challenge is to prove such possession without revealing the information itself or any additional information.")
print()
print()
print("First of all we need a sodoku table with values included \n\nplease choose how to want to Genarate the table :")
print(" 1.Export unsolved table from Sudokus2.txt file")
print(" 2.Generate random unsolved table\n")
while True:
    tableselect = input("your selection : ")
    if tableselect == "1" or tableselect == "2":
        break
print()

# print(tableselect)

'''
import input(sodoku table) from .txt file -> create sodoku -> solve
   this functuion returns 2 values [ Solve , Original]
'''
x  = pySudoku.main(tableselect)

print("\n Please Choose Confidence precentage : (80 or 90 , etc )")
conf = input("-->")
Prover = prover(conf)
verifier = Verifier(conf)

#Build solved + orginal tables
solved = x[0]
text = x[1]
org = []
Prover.buildTable(text,org)
print(solved)

#Collect Rows colums and grids
rowsDict = Prover.rowsCollector(solved)
colsList = Prover.colCollector(solved)
gridList = Prover.gridCollector(solved)

#Create Packets to choose
r = ["r1" , "r2" , "r3" , "r4" , "r5" , "r6" , "r7" , "r8" ,"r9"]
c = ["c1" , "c2" , "c3" , "c4" , "c5" , "c6" , "c7" , "c8" , "c9"]
g = ["g1" , "g2" , "g3" , "g4" , "g5" , "g6" , "g7" , "g8" , "g9"]

def printrcg():
    
    print("\n-----------CHOOSE---ONE----PACKET-----------------")
    print("ROWS : ")
    print(r)
    print("COULMS :")
    print(c)
    print("GRIDS:")
    print(g)
    print()
    print("Exampl : r1 , r3 ....")

    if not r and not c and not g:
        print("\n Not approved ! all the packets have been open")
        quit()

# Main loop - ask Verifier for feedback + uopdate the confidance
while(True):
    os.system("clear")
    pySudoku.print_sudoku(org)
    printrcg()
    choose = ""
    
    print("Confidence : ")
    print("%.2f" % (verifier.getapprlvl() * 100) + "% \ "+conf+"%" )
    print()

    choose = input("your selection : ")
    try:
        
        print(solved)
        
        num = choose[1]
        if choose[0] == "r":

            r.remove(choose)
            print()
            temp = list(rowsDict[int(num)-1])
            temp.sort()
            print(temp)
            while(True):
                 
                answer = input("Is this packet valid ? : ( y , n ) :")

                if answer == "y":
                    verifier.approvePacket()
                    break

                elif answer == "n":
                    break

                else:
                    print("Invalid Answer , please try again")

        elif choose[0] == "c":

            c.remove(choose)
            print()
            temp = list(colsList[int(num)-1])
            temp.sort()
            print(temp)
            answer = input("Is this packet valid ? : ( y , n ) :")

            if answer == "y":
                verifier.approvePacket()

        elif choose[0] == "g":

            g.remove(choose)
            print()
            temp = gridList[int(num) -1 ]
            temp.sort()
            print(temp)
            answer = input("Is this packet valid ? : ( y , n ) :")

            if answer == "y":
                verifier.approvePacket()
        
        else:
            raise
    except:
        print("Invalid selection - Packet "+ choose + " does not excist Please try again")

    if verifier.isProff():
        print("\n You reach your confidence precetage : %.2f" % (verifier.getapprlvl() * 100) + "% \ "+conf+"%")
        break
