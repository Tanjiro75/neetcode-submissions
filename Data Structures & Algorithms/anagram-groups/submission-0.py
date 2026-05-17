class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       map=defaultdict(list)
       for s in strs:
        srtd = "".join(sorted(s))
        map[srtd].append(s)
       return list(map.values())





        