# Find the two numbers that complete the two sum, 
# then multiply them

# O(N) time and space complexity
def parse_input():
    with open('input.txt') as f:
        nums = list(int(line.split()[0]) for line in f) # list comprehension
    return nums

# O(N) time and space complexity
# it can be assumed from the problem that two such numbers exist.
def two_sum(nums) -> (int, int):
    seen = set()
    for num in nums:
        complement = 2020 - num
        if complement in seen:
            return (num, complement)
        else:
            seen.add(num)

if __name__ == "__main__":
    
    nums = parse_input()
    x, y = two_sum(nums)
    print (x * y) # (21 * 1999) = 41979