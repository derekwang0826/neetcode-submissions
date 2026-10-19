class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #+/- 1 for each letter count?
        words = []
        types = []

        for i in range(len(strs)):
            letters = set(strs[i])
            word = {letter: 0 for letter in letters}
            for letter in strs[i]:
                word[letter] += 1 
            if word in words: 
                pass
            else:
                types.append(word)
            words.append(word)
            
        groups = [[] for i in range(len(types))]

        for i in range(len(words)):
            for j in range(len(types)):
                if words[i] == types[j]:
                    groups[j].append(strs[i])
        
        return groups