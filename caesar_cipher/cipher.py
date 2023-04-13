import nltk
from nltk.corpus import words, names
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt', quiet=True)
nltk.download('words', quiet=True)

word_list = words.words()
namelist = names.words()



def encrypt(message, key):
    # shift letters in phrase based on input
    # E.g. encrypt(‘abc’,1) would return
    # ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.
    # shifts that exceed 26 should wrap around.
    # E.g. encrypt(‘abc’,27) would return ‘bcd’.
    result = ''
    for char in message:
        # checks if character is alphabetic
        if char.isalpha():
            if char.isupper():
                # applies shift to char and handles wraparound
                result += chr((ord(char) + key-65) % 26+65)
            else:
                result += chr((ord(char) + key-97) % 26 + 97)
        else:
            result += char
    return result


def decrypt(encrypted, key):
    # restores the encrypted text back to its original form when
    # correct key supplied
    return encrypt(encrypted, -key)


def crack(encrypted):
    # decode cipher so that an encrypted message can be
    # transformed into its original state WITHOUT access to key
    # split the string to words
    # split_encrypted = encrypted.split()

    for key in range(1, 27):
        decrypted = decrypt(encrypted, key)
        if decrypted.lower() in word_list or decrypted.lower() in namelist:
            # if the decrypted message is a valid English word or name, return it
            return decrypted
    # if none of the keys produced a meaningful message, return ''
    return ''


if __name__ == '__main__':
    phrase = 'apple'
    # print(encrypt('apple', 1))
    # print(decrypt('bqqmf', 1))
    print(crack('Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd.'))