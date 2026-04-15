class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)

            if key not in results:
                results[key] = []
            results[key].append(s)

        return list(results.values())