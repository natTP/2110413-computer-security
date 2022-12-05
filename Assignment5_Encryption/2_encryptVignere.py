message = input("Enter your message to be encrypted (alphabet only, no spaces and periods): ").upper()
key = input("Enter key: ")

keyword = (key * (len(message) // len(key) + 1))[:len(message)]

encrypted_text = ""
for i in range(len(message)):
    e = ord('A') + (ord(message[i]) + ord(keyword[i])) % 26
    encrypted_text += chr(e)

print("Encrypted message:", encrypted_text)