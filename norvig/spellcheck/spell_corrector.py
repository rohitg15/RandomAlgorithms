from collections import Counter
import re
import sys
from typing import List

class SpellChecker:
    def __init__(self, file_name: str) -> None:
        self._known_words = Counter( re.findall( r'\w+',
                                                open(file_name).read().lower()
                                                )
                                    )
        self._total = sum(self._known_words.values(), 0)
    
    def correct(self, word: str) -> str:
        def Pr(word):
            count = self._known_words[word]
            return 0 if count is None else count / self._total
        return max(self.__candidates(word), key=Pr)

    def __candidates(self, word: str) -> List[str]:
        def known(words: List[str]) -> List:
            return [w for w in words if w in self._known_words]
        # assuming that Pr(word) > Pr(1edit)
        return known([word]) or known(SpellChecker.__edits1(word))
    
    @staticmethod
    def __edits1(word: str) -> List[str]:
        letters = "abcdefghijklmnopqrstuvwxyz"
        splits = ( (word[:i], word[i:]) for i in range(len(word) + 1) )
        res = []
        for l, r in splits:
            if r:
                res.append(l + r[1:])               # delete
            if len(r) > 1:
                res.append(l + r[1] + r[0] + r[2:]) # transpose
            for c in letters:
                res.append(l + c + r[1:])           # replace
                res.append(l + c + r)               # insert
        return res

if __name__ == "__main__":
    spell_check = SpellChecker(sys.argv[1])
    print (spell_check.correct(sys.argv[2]))
