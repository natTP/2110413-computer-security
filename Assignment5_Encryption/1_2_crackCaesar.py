import itertools
import enchant

english_dictionary = enchant.Dict("en_US")

# ----- functions -----

def decrypt(encrypted_text, cipher):
    decrypted_text = ""
    for c in encrypted_text:
        if c in " .":
            decrypted_text += c
        else:
            decrypted_text += chr(ord("A") + cipher.index(c))
    return decrypted_text

def is_text_valid(text):
    text = text.split()
    for word in text:
        if(english_dictionary.check(word) == False):
            return False
    return True

# ----- script -----
# encrypted_text = "PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE."
# cipher = "ZECURABDFGHIJKLMBOPQSTVWXY"

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

has_ans = False

encrypted_text = input("Enter encrypted text: ")

for key_length in range(0,10):
    print("Trying keys with length", key_length)
    all_permutations = list(itertools.permutations(alphabet, key_length))
    for permutation in all_permutations: 
        key = ''.join([char for char in permutation])
        cipher = key

        for char in alphabet:
            if char not in key:
                cipher += char
        
        decrypted_text = decrypt(encrypted_text, cipher)

        if(is_text_valid(decrypted_text)):
            print('decrypted text = ' + decrypted_text + ', key = ' + key)
            has_ans = True
            break

    if(has_ans):
        break