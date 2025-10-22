import re
from typing import Iterable, Set
from .trie import Trie

TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z'\-\+]*")

def tokenize(text: str):
    return (m.group(0).lower() for m in TOKEN_RE.finditer(text))

class HashSetSentimentScorer:
    """
    Membership via Python set (amortized O(1) lookup).
    Keeps the algorithm identical to the Trie variant: only membership differs.
    """
    def __init__(self, pos_words: Iterable[str], neg_words: Iterable[str]):
        self.pos: Set[str] = {w.strip().lower() for w in pos_words if w.strip()}
        self.neg: Set[str] = {w.strip().lower() for w in neg_words if w.strip()}

    def score_review(self, text: str) -> int:
        score = 0
        for w in tokenize(text):
            if w in self.pos:
                score += 1
            elif w in self.neg:
                score -= 1
        return score

class TrieSentimentScorer:
    """
    Membership via Trie (O(m) per lookup, m = word length).
    """
    def __init__(self, pos_words: Iterable[str], neg_words: Iterable[str]):
        self.pos_trie = Trie()
        self.neg_trie = Trie()
        for w in pos_words:
            w = w.strip().lower()
            if w:
                self.pos_trie.insert(w)
        for w in neg_words:
            w = w.strip().lower()
            if w:
                self.neg_trie.insert(w)

    def score_review(self, text: str) -> int:
        score = 0
        for w in tokenize(text):
            if self.pos_trie.contains(w):
                score += 1
            elif self.neg_trie.contains(w):
                score -= 1
        return score