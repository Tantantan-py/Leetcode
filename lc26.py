nums = [1, 2, 3, 4, 1, 1]

slow, fast = 0, 0
slow = 0
fast = 0

res = 0
# last step for fast pointer: fast == len(nums) - 1

while fast < len(nums):
    if nums[slow] == nums[fast]:
        fast += 1
    else:
        res += 1
        nums[slow+1] = nums[fast]
        slow += 1
    
    print(res)


# swap


pos = -1
pos -= 1
pos = pos - 1
nums2 = [4, 3, 2, 1]