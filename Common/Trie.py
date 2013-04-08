class TrieNode:
    def __init__(self):
        self.value = None
        self.nxt = {}

class Trie:
    def __init__(self):
        self.wordcount = 0
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.nxt:
                child = TrieNode()
                node.nxt[c] = child
                node = child
            else:
                node = node.nxt[c]
        if node.value == None:
            self.wordcount += 1
        node.value = word

    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.nxt:
                return None
            else:
                node = node.nxt[c]
        return node.value
