class TrieNode: 
    def __init__(self):
        self.children = {} 
        self.end = False 

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for s in word: 
            if s not in node.children: 
                node.children[s] = TrieNode()
            node = node.children[s]
        node.end = True 

    def search(self, word: str) -> bool:
        node = self._walk(word)
        if not node: 
            return False 
        return node.end 


    def startsWith(self, prefix: str) -> bool:
        node = self._walk(prefix)
        if not node: 
            return False 
        return True 

    def _walk(self, word: str): 
        node = self.root
        for s in word: 
            if s not in node.children:
                return None 
            node = node.children[s]
        return node 
        
        