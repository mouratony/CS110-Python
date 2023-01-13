from symboltable import SymbolTable
import stdio
import stdrandom
import sys


class MarkovModel(object):
    # Creates a Markov model of order k from the given text.
    def __init__(self, text, k):
        # Initialize _k(int) to k
        self._k = int(k)
        # Create a symbol table _st
        self._st = SymbolTable()
        # Set circ_text to text + the k first characters of text
        circ_text = text + text[:k]

        for i in range(len(circ_text) - self._k):
            # For each kgram from circ_text,

            # set kgram to circ_text[i: k + i],
            kgram = circ_text[i: self._k + i]
            # set next_char to the character that follows kgram ,
            next_char = circ_text[i + self._k]
            # if kgram is not a key of _st,
            if kgram not in self._st:
                # insert a SymbolTable to _st
                self._st[kgram] = SymbolTable()
            # if next_char is a key of the symbol table inside _st,
            if next_char in self._st[kgram]:
                # increment the said next_char by 1
                self._st[kgram][next_char] += 1
            else:
                # otherwise insert that next_char to _st[kgram] with the value as 1
                self._st[kgram][next_char] = 1

    # Returns the order this Markov model.
    def order(self):
        return self._k

    # Returns the number of occurrences of kgram in this Markov model; and 0 if kgram is
    # nonexistent. Raises an error if kgram is not of length k.
    def kgram_freq(self, kgram):
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))
        elif kgram not in self._st:
            return 0
        # return the sum of values of _st[kgram]
        return sum(self._st[kgram].values())

    # Returns number of times character c follows kgram in this Markov model; and 0 if kgram is
    # nonexistent or if it is not followed by c. Raises an error if kgram is not of length k.
    def char_freq(self, kgram, c):
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))
        elif kgram not in self._st or c not in self._st[kgram]:
            return 0
        # return the value of the key c in _st[kgram]
        return self._st[kgram][c]

    # Returns a random character following kgram in this Markov model. Raises an error if kgram is
    # not of length k or if kgram is nonexistent.
    def rand(self, kgram):
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))
        if kgram not in self._st:
            raise ValueError('Unknown kgram ' + kgram)
        # set index to random index of list of values of _st[kgram]
        index = stdrandom.discrete(list(self._st[kgram].values()))
        # set a to the sorted list of keys of _st[kgram]
        a = sorted(list(self._st[kgram].keys()))
        # return a[index].
        return a[index]

    # Generates and returns a string of length n from this Markov model, the first k characters of
    # which is kgram.
    def gen(self, kgram, n):
        # set text to kgram
        text = kgram
        for i in range(n - self._k):
            # for each i in [o, n - k],
            # append random characters obtained using a call to self.rand()
            # and updating kgram to the last _k characters of text.
            text += self.rand(text[i: self._k + i])
        # return text.
        return text

    # Replaces unknown characters (~) in corrupted with most probable characters from this Markov
    # model, and returns that string.
    def replace_unknown(self, corrupted):
        # set original to ''.
        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                kgram_before = corrupted[i - self._k: i]
                kgram_after = corrupted[i + 1: i + self._k + 1]
                probs = []
                hypotheses = []
                for h in self._st[kgram_before].keys():
                    hypotheses.append(h)
                    context = kgram_before + h + kgram_after
                    p = 1.0
                    for c in range(self._k):
                        kgram = context[c: self._k + c]
                        char = context[self._k + c]
                        if kgram not in self._st or char not in self._st[kgram]:
                            p = 0
                            break
                        p *= self.char_freq(kgram, char) / self.kgram_freq(kgram)
                    probs.append(p)
                x = _argmax(probs)
                original += hypotheses[x]
            else:
                original += corrupted[i]
        return original


# Given a list a, _argmax returns the index of the maximum value in a.
def _argmax(a):
    return a.index(max(a))


# Unit tests the data type [DO NOT EDIT].
def _main():
    text = sys.argv[1]
    k = int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        kgram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace('-', ' '), char.replace('-', ' ')))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char, model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()
