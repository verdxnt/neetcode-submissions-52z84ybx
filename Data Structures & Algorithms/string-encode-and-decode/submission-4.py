class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        delimiter = "#"
        for word in strs:
            encoded_str += str(len(word)) + delimiter + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        words = []
        idx = 0
        while idx < len(s):
            delimiter = "#"
            cur = idx
            while s[cur] != delimiter:
                cur += 1
            length = int(s[idx:cur])
            idx = cur + 1
            word = s[idx:idx+length]
            words.append(word)
            idx = idx + length
        return words
