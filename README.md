# Secure Voting System

A terminal-based e-voting prototype combining elliptic-curve (ECC) key exchange, AES-GCM authenticated encryption, and SMS-based voter verification via Twilio. Voters register, verify by phone, and cast ballots encrypted per-voter, so tallies are computed by the election authority without ever exposing a plaintext vote in storage.

## How it works

1. **Registration** — a voter enters an ID and phone number (`VotingSystem.addVoter`). A new `Voter` is created with an ECC keypair on the `brainpoolP256r1` curve; the private key is generated with `secrets.randbelow`, never transmitted, and doubles as the voter's verification secret.
2. **Verification** — the private key is sent to the voter's phone over SMS (Twilio, `bot.py`). The voter re-enters it character by character in the terminal; matching enough characters marks them verified (`Voter.Veriffie`).
3. **Casting a vote** — once verified, the voter picks a candidate. The choice is encrypted with ECIES (ECC-derived shared secret → SHA-256 → AES-256-GCM, see `DES.py`) using the voter's own public key, so only their private key can decrypt it later.
4. **Tallying** — `VotingSystem` keeps running totals (`D`/`R`) without ever needing to decrypt a ballot. Decryption only happens if a voter re-verifies to change their vote, at which point their previous choice is decrypted, the old count is reversed, and the new one applied.
5. **Changing a vote** — a voter can register again with the same ID; after re-verifying by SMS, their existing encrypted ballot is decrypted, the tally is corrected, and the new choice replaces it.

## Project structure

| File | Purpose |
|---|---|
| `main.py` | Entry point — interactive CLI loop for registering and voting |
| `VotingSystem.py` | Election state: voter roster, vote tallying, re-vote handling |
| `Voter.py` | Per-voter identity, ECC keypair, SMS verification, vote casting |
| `DES.py` | ECIES-style encryption/decryption (ECC + AES-GCM) — despite the filename, this is not DES |
| `bot.py` | Twilio SMS client used for the verification step |
| `example.py` | Non-interactive demo of the crypto core, no Twilio required |

## Requirements

- Python 3.9+
- A [Twilio](https://www.twilio.com/) account (Account SID, Auth Token, and a Messaging Service SID) — only needed to run `main.py`'s SMS verification step

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

`main.py` sends real SMS messages through Twilio, so it needs credentials supplied as environment variables (never hardcode them in source):

```bash
export TWILIO_ACCOUNT_SID="your_account_sid"
export TWILIO_AUTH_TOKEN="your_auth_token"
export TWILIO_MESSAGING_SERVICE_SID="your_messaging_service_sid"
```

## Usage

```bash
python3 main.py
```

You'll be prompted for a voter ID and phone number, sent a verification code by SMS, asked to re-type it, and then asked to pick a voting center and a candidate (`Democrat` or `Republic`). The loop repeats for a fixed number of voters (`m` in `main.py`).

## Example (no Twilio required)

Since `main.py` needs live Twilio credentials and manual SMS entry, `example.py` exercises the underlying cryptography directly — key generation, per-voter vote encryption, tallying, and decryption:

```bash
python3 example.py
```

```
Tally after both votes:
Democrat :  1
Republic :  1

Decrypting each stored ballot with its own private key:
Alice voted: b'Democrat'
Bob voted:   b'Republic'
```

## Known limitations

This is a student project (see credits below), not a production voting system:

- The "verification" step is a simple SMS-code re-entry, not a real zero-knowledge proof protocol, despite the project name.
- Ballots are encrypted per-voter but not anonymized from the tally process — the election authority can trivially decrypt any ballot since it never discards the corresponding private key material passed around in-memory.
- There's no persistence layer; all state lives in memory for the duration of one `main.py` run.
- `os.system("clear")` in `Voter.Veriffie` is Unix-only.

## Security note

Earlier commits in this repository's history contained hardcoded Twilio credentials in `bot.py`. They have since been removed from the code (replaced with environment variables), but **anyone with access to the git history can still recover them from prior commits**. If you cloned this repo before that fix, treat those credentials as compromised and rotate them in the Twilio console.

## Credits

- Anatoli Kot
- Eden Barsheshet
- Yuval Varshavsky
