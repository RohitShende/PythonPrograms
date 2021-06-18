# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
# to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].


# approach 1 -
# for i in l:
#     for j in l:
#         l[i] + l[j] == target

# approach 2 -
l = [2, 7, 11, 15]
target = 9
d = {target - num: i for i, num in enumerate(l)}  # O(n)
print(d)
for i, num in enumerate(l):  # O(n)
    index2 = d.get(num)
    if index2:
        print(i, index2)
        break
