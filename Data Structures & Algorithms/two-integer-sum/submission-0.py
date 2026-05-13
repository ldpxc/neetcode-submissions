class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        rs = []
        for i in range(len(nums)):
            if target - nums[i] in hm:
                rs.append(hm[target - nums[i]])
                rs.append(i)
                return rs
            else:
                hm[nums[i]] = i
        return rs