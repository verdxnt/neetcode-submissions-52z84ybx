class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[]for i in range(len(nums)+1)] #indexs represent the frequency/count, and value represents the number (category)
        count = {} #number:count

        for n in nums:
            count[n] = count.get(n,0) + 1

        for n, c in count.items():
            freq[c].append(n)

        results = [] 
        for i in range(len(freq)-1 ,0 ,-1):
            for val in freq[i]:
                results.append(val)
                if len(results) == k:
                    return results


