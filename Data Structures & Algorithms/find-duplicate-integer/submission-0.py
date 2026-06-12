class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd's tortoise and hare
        # because one number is duplicated, two indices will point to the same chain, creating a cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # each index points to the next index given by its value
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow