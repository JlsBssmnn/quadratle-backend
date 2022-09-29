class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True

    def searchString(self, word):
        """
        returns status of word in trie
        0 no further options
        1 word is in trie
        2 further options available
        """
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return 0
            currentNode = node
        if currentNode.endOfString == True:
            return 1
        else:
            return 2
