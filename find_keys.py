def xor_bytes(data1, data2):
    return bytes(a ^ b for a, b in zip(data1, data2))

def encrypt(plaintext, key):
    return xor_bytes(plaintext, key)

def decrypt(ciphertext, key):
    return xor_bytes(ciphertext, key)

if __name__ == "__main__":
    # Load the plaintexts
    with open('sentence_1.txt', 'rb') as f:
        p1 = f.read()

    with open('sentence_2.txt', 'rb') as f:
        p2 = f.read()

    # Check if lengths match
    if len(p1) != len(p2):
        raise ValueError("Plaintext files must be of the same length")

    # Generate a key that could result in c when decrypted with p1 or p2
    k1 = xor_bytes(p1, p2)  # This is highly conceptual and needs adjustment
    c = xor_bytes(p1, k1)

    # Decrypt with key1 (should give p1)
    decrypted_p1 = decrypt(c, k1)
    print("Decrypted p1:", decrypted_p1)

    # Decrypt with key2 (needs to be found or constructed)
    # Here you'd experiment with different key2 approaches
    # Assuming k2 is somehow derived:
    k2 = ...  # Need a method to derive this
    decrypted_p2 = decrypt(c, k2)
    print("Decrypted p2:", decrypted_p2)

    # Save the ciphertext
    with open('task02.cryp', 'wb') as f:
        f.write(c)
