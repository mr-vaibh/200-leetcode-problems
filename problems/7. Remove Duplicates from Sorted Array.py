def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1

    for delete_index in range(len(nums)-1, count-1, -1):
        del nums[delete_index]

x = [0,1,2,2,3,0,4,2]

removeElement(x, 2)

print(x)

# https://leetcode.com/problems/remove-element/
