class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answers = []
        count = defaultdict(int)
        for num in nums:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
        
        for i in range(k):
            for j in count.keys():
                if count[j] == max(count.values()):
                    answers.append(j)
            for n in answers:
                count.pop(n, None)
            if len(answers) == k:
                return answers
            else:
                pass
        
        return answers