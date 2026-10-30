"""
Hashmap 
store key - len(word), value - list of words 
when search get same length words from map and compare 
"""
class TrieNode: 
    def __init__(self):
        self.children = {} # key letter, value children
        self.end = False 

class TrieNode:
    def __init__(self):
        self.children = {}  # key: letter, value: child TrieNode
        self.end = False    # 여기서 끝나는 단어가 추가된 적 있는지

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)

    def dfs(self, word: str, i: int, curr: TrieNode) -> bool:
        # 1. 단어를 끝까지 다 봤으면, 여기서 끝나는 단어가 있는지 반환
        if i == len(word):
            return curr.end

        c = word[i]

        # 2. '.'이면 모든 child에서 남은 부분(i+1부터)을 시도
        if c == '.':
            for child in curr.children.values():
                if self.dfs(word, i + 1, child):
                    return True
            return False

        # 3. 일반 글자: 없으면 실패, 있으면 그 child로 이동
        if c not in curr.children:
            return False
        return self.dfs(word, i + 1, curr.children[c])
