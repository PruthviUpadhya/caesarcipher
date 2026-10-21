"""
CNS Assignment 2: Caesar Cipher with Cryptanalysis
Language: Python 3
Purpose: Demonstrate classical encryption/decryption and brute-force cryptanalysis.

Educational note:
Caesar cipher is NOT secure for real-world use. It is included to demonstrate
basic cryptographic concepts and why small key spaces are vulnerable.
"""

ALPHABET_SIZE = 26


def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt letters by shifting them; preserve case and non-letters."""
    shift %= ALPHABET_SIZE
    result = []

    for char in text:
        if "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
        elif "a" <= char <= "z":
            result.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(char)

    return "".join(result)


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Decrypt by reversing the encryption shift."""
    return caesar_encrypt(ciphertext, -shift)


def brute_force(ciphertext: str) -> list[tuple[int, str]]:
    """Return all 26 possible decryptions, one for each Caesar key."""
    return [(key, caesar_decrypt(ciphertext, key)) for key in range(26)]


def run_demo() -> None:
    print("=== Caesar Cipher with Brute-Force Cryptanalysis ===")
    message = "Hola, World! at meet 5 PM."
    key = 3

    encrypted = caesar_encrypt(message, key)
    decrypted = caesar_decrypt(encrypted, key)

    print(f"Original message : {message}")
    print(f"Key              : {key}")
    print(f"Encrypted message: {encrypted}")
    print(f"Decrypted message: {decrypted}")
    print(f"Round-trip test  : {'PASS' if decrypted == message else 'FAIL'}")

    print("\nBrute-force candidates for ciphertext 'Hola':")
    for candidate_key, candidate_text in brute_force("Hola"):
        print(f"Key {candidate_key:2}: {candidate_text}")


if __name__ == "__main__":
    run_demo()
