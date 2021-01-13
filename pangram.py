class Pangram:
    def is_pangram(self, word):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        word = word.lower()
        if type(word) == str:
            for letter in alphabet:
                if letter not in word:
                    return False
            return True
        else:
            raise Exception("Error in pangram")
