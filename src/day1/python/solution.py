# Find the two numbers that complete the two sum, 
# then multiply them

# O(N) time and space complexity
def parse_input():
    with open('../input.txt') as f:
        nums = list(int(line.split()[0]) for line in f) # list comprehension
    return nums

from typing import List
# O(N) time and space complexity
# it can be assumed from the problem that two such numbers exist.
def two_sum(nums : List[int]) -> List[int]:
    seen = set()
    for num in nums:
        complement = 2020 - num
        if complement in seen:
            return [num, complement]
        else:
            seen.add(num)

# O(N^2) time, O(N) worst case space
# again, the question implies that there exists
# a unique and non-empty triplet.

def three_sum(nums : List[int]) -> List[int]:
    nums.sort()
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        
        # use a two-pointer solution to check where our sum is
        l = i + 1
        r = len(nums) - 1

        while l < r:
            total = num + nums[l] + nums[r]
            if total > 2020:
                r -= 1
            elif total < 2020:
                l += 1
            else:
                return [num, nums[l], nums[r]]

def productOfEntries(entries) -> int:
    from functools import reduce
    return reduce((lambda x,y: x * y), entries)

if __name__ == "__main__":
    nums = parse_input()
    print("Part 1:", productOfEntries(two_sum(nums))) # (21 * 1999) = 41979
    print("Part 2:", productOfEntries(three_sum(nums))) 