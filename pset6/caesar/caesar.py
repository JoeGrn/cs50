import sys
from cs50 import  get_string

def main():

    if len(sys.argv) != 2:
        print("Usage: Provide a Positive Integer")
        sys.exit(1)

    k = int(sys.argv[1])
    if k < 0 or sys.argv[1] == None:
        print("Not a Positive Integer")
        sys.exit(1)

    while True:
        print("Please Provide Text to Encrypt:")
        plaintext = get_string()
        if plaintext == None:
            continue
        else:
            break

    ciphertext = []

    for char in plaintext:
        if char.isalpha():
            ciphertext.append(caesar(char, k))
        else:
            ciphertext.append(char)

    print("ciphertext: ", end = "".join(ciphertext))
    print("")

    sys.exit(0)

def caesar(index, k):
    if index.isupper():
        return chr(((ord(index) - 65 + k) % 26) + 65)
    else:
        return chr(((ord(index) - 97 + k) % 26) + 97)


if __name__ == "__main__":
    main()