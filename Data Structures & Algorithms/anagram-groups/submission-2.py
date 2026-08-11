class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs: 
            word_token = self.tokenize(word)
            anagrams[word_token].append(word)

        return list(anagrams.values())


    def tokenize(self, word: str) -> Dict[str, int]:
        arr = [0] * 26 
        for char in word: 
            arr[ord(char) - ord('a')] += 1

        return tuple(arr)
        

        