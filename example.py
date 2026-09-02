"""
Standalone example of the voting system's cryptographic core.

Runs the ECC key generation, vote encryption/decryption, and tallying logic
directly, without the interactive Twilio SMS verification step that main.py
requires. Useful for seeing how the pieces fit together, or for testing
without Twilio credentials.

Run with: python3 example.py
"""

from Voter import Voter
from VotingSystem import VotingSystem

CURVE_ID = "brainpoolP256r1"


def main():
    voting_system = VotingSystem(CURVE_ID)

    # Each voter gets an ECC keypair; the private key doubles as their
    # SMS verification secret in the full flow (see Voter.Veriffie).
    alice = Voter(id="111", phone="0000000", curveid=CURVE_ID)
    bob = Voter(id="222", phone="0000000", curveid=CURVE_ID)

    voting_system.voters.append(alice)
    alice.makeVote("Democrat")
    voting_system.incD()

    voting_system.voters.append(bob)
    bob.makeVote("Republic")
    voting_system.incR()

    print("\nTally after both votes:")
    voting_system.getStatus()

    # Only someone holding a voter's private key can decrypt that voter's
    # stored ciphertext -- the tally above never touches plaintext votes.
    print("\nDecrypting each stored ballot with its own private key:")
    print("Alice voted:", voting_system.decrypt(alice.get_P_key(), alice.getMyVote()))
    print("Bob voted:  ", voting_system.decrypt(bob.get_P_key(), bob.getMyVote()))


if __name__ == "__main__":
    main()
