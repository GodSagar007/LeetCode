from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slowAgain = nums[0]
        while slowAgain != fast:
            slowAgain = nums[slowAgain]
            fast = nums[fast]
        return slowAgain

# ✅ TEST FUNCTION for pytest
def test_findDuplicate():
    s = Solution()
    assert s.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert s.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert s.findDuplicate([1, 1, 2]) == 1
    assert s.findDuplicate([1, 4, 6, 5, 3, 2, 6]) == 6
    assert s.findDuplicate([1, 1]) == 1
    assert s.findDuplicate([5, 4, 3, 2, 1, 6, 6]) == 6
    big_test = list(range(1, 10001)) + [789]
    assert s.findDuplicate(big_test) == 789
