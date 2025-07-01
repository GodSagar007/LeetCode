import pytest
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            raise ValueError("Both arrays are empty")
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

        raise ValueError("Input arrays are not sorted")

@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        # Basic tests
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),

        # One empty array
        ([], [1], 1.0),
        ([2], [], 2.0),

        # Both arrays same elements
        ([2, 2], [2, 2], 2.0),

        # One long, one short
        ([1, 3, 5], [2, 4, 6, 8, 10], 4.5),

        # Large gap between arrays
        ([1, 2], [100, 200], 51.0),

        # Arrays with duplicates
        ([1, 2, 2], [2, 2, 3], 2.0),

        # Negative numbers
        ([-5, -3, -1], [-2, 0, 1], -1.5),

        # Odd total length
        ([1, 2], [3], 2.0),

        # Even total length
        ([1, 2], [3, 4], 2.5),

        # Large one-sided array
        ([1], [2, 3, 4, 5, 6], 3.5),
    ]
)
def test_find_median_sorted_arrays(nums1, nums2, expected):
    sol = Solution()
    assert sol.findMedianSortedArrays(nums1, nums2) == expected

def test_empty_arrays_raises():
    sol = Solution()
    with pytest.raises(ValueError):
        sol.findMedianSortedArrays([], [])
