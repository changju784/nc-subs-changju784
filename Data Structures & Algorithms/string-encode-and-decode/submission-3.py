class Solution:

    def encode(self, strs: List[str]) -> str:
        result = [] 
        for s in strs: 
            result.append(str(len(s)))
            result.append('#')
            result.append(s)
        return "".join(result)


    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = s.find('#', i)
            n = int(s[i:j])
            result.append(s[j + 1 : j + 1 + n])
            i = j + 1 + n
        return result



