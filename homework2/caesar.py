import typing as tp
import string


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encripta el texto plano usando un cifrado César.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if char.islower():
            ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Desencripta un texto cifrado usando un cifrado César.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if char.islower():
            plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        elif char.isupper():
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            plaintext += char
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    max_matches = 0
    for shift in range(26):
        matches = 0
        decrypted = decrypt_caesar(ciphertext, shift)
        for word in decrypted.split():
            if word.lower() in dictionary:
                matches += 1
        if matches > max_matches:
            max_matches = matches
            best_shift = shift
    return best_shift

