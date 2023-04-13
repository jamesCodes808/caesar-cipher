import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import words, names

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

word_list = words.words()
namelist = names.words()


def encrypt(phrase, key):
    # shift letters in phrase based on input
    # E.g. encrypt(‘abc’,1) would return
    # ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.
    # shifts that exceed 26 should wrap around.
    # E.g. encrypt(‘abc’,27) would return ‘bcd’.
    result = ''
    for char in phrase:
        # checks if character is alphabetic
        if char.isalpha():
            # uppercase for simplicity
            char = char.upper()
            # applies shift to char and handles wraparound
            shifted_char = chr((ord(char) - 65 + key) % 26 + 65)
            result += shifted_char
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
    tokenized_words = word_tokenize(encrypted)
    for key in range(26):
        decrypted_words = [decrypt(word, key) for word in tokenized_words]
        decrypted_message = ' '.join(decrypted_words)
        # checks if decrypted message contains any common english words
        if any(word.lower() in word_list for word in decrypted_words):
            return decrypted_message
    return ""


if __name__ == '__main__':
    phrase = 'apple'
    print(encrypt('apple', 1))
    print(decrypt('bqqmf', 10))
    print(crack('bqqmf'))