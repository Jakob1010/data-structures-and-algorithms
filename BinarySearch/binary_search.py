import unittest
from unittest import mock

class BinarySearch:
    # Returns index of target in nums if present, else -1
    @staticmethod
    def binary_search(nums, target):
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return - 1


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        bs = BinarySearch()
        nums = [1, 2, 3, 4, 5, 10, 12, 14, 345]

        # existing target
        self.assertEqual(bs.binary_search(nums, nums[3]), 3)
        # index 0
        self.assertEqual(bs.binary_search(nums, nums[0]), 0)
        # index n-1
        self.assertEqual(bs.binary_search(nums, nums[len(nums)-1]), len(nums)-1)
        # existing target
        self.assertEqual(bs.binary_search(nums, nums[6]), 6)
        # non existing target
        self.assertEqual(bs.binary_search(nums, 100), -1)

    if __name__ == '__main__':
        unittest.main()

