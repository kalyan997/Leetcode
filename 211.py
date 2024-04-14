class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c  not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr= self.root

        def searchInNode(curr_ind, word, node):
            if node is None:
                return False
            if curr_ind == len(word):
                return node.isEnd
            curr_char = word[curr_ind]
            if curr_char != '.':
                if curr_char not in node.children:
                    return False
                return searchInNode(curr_ind + 1, word, node.children[curr_char])
            for child in node.children.values():
                if searchInNode(curr_ind + 1, word, child):
                    return True
            return False

        return searchInNode(0,word,curr)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)