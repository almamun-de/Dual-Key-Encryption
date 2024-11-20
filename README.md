# Dual-key Encryption Scheme

## Overview
This project attempts to solve the problem where a single ciphertext can be decrypted into two different plaintexts using two different keys. The goal is to decrypt `task02.cryp` into `sentence_1.txt` using key `k1` and into `sentence_2.txt` using key `k2`.

## Files
- `find_keys.py`: The script used to attempt to find or create the keys `k1` and `k2`.
- `sentence_1.txt`: The first plaintext.
- `sentence_2.txt`: The second plaintext.
- `task02.cryp`: The resulting ciphertext.

## Usage
1. **Generate or find the keys**:
   - The script may need customization depending on your approach to deriving `k1` and `k2`.
   - Once the keys are identified, the script will encrypt and decrypt the messages accordingly.

2. **Decrypt**:
   - The script will output the plaintexts when decrypting with the respective keys.

## Results
- The correct keys `k1` and `k2` will decrypt the ciphertext `task02.cryp` into `sentence_1.txt` and `sentence_2.txt`, respectively.

