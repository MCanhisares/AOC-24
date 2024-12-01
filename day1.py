from collections import defaultdict

class Solution:
    def solve1(self, nums1, nums2):
        # Write your code here        
        nums1.sort()
        nums2.sort()
        distance = 0
        for i in range(len(nums1)):
            distance += abs(nums1[i] - nums2[i])
        return distance
    
    def solve2(self, nums1, nums2):
        occ = defaultdict(int)
        for n in nums2:
            occ[n] += 1
        
        res = 0
        for n in nums1:
            res += n * occ[n]
        return res


def __main__():
    file = open("day1.txt", "r")
    nums1, nums2 = [], []
    for line in file:               
        for i, el in enumerate(line.split(" ")):
            if i == 0:
                nums1.append(int(el.strip()))
            else:
                nums2.append(int(el.strip()))                    
    s = Solution()
    print(s.solve1(nums1.copy(), nums2.copy()))        
    print(s.solve2(nums1.copy(), nums2.copy()))


if __name__ == "__main__":
    __main__()