nums = [1, 2, 3, 4]

for element in nums:
    print(element)

for _ in range(len(nums)): # _ represents the index
    print(nums[_])

"""
for i in range(len(nums)):
            len(nums) = 4
            i = 0, 1, 2, 3
        
        for element in nums:

        for -> each element : i(element) O(n)
            for -> each element: j(element): O(n) => O(n^2)
                if i + j = target: 
                    if i != j:
                        return [idxOf_i, idxOf_j]

        syntax sugar 



    def twoSum2(nums, target):
        print("Hello World")


            nums = [1, 2, 3, 4]
            
            target = 6

            return -> [1, 3]

            stackoverflow
            ChatGPT
            CSDN

    index = idx
    s.t. 
"""

nums = [2,7,11,15]
target = 17
d = {}

for i in range(len(nums)): # O(n)
            if target - nums[i] in d:
                print([d[target - nums[i]], i]) 
                # [    d[2] ,   i   ]
                
            d[nums[i]] = i


            # assign i(0) to d[2]
            d[7] = 1
            7: 1