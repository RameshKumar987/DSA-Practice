#method 1

# nums = [2,3,4,5,4,6,3,2,6,7,6,5,2,8,9,0,5,6,7,8,9]
# frequency_map = dict()
# for i in range(0, len(nums)):
#     if nums[i] in frequency_map:
#         frequency_map[nums[i]] += 1
#     else:
#         frequency_map[nums[i]] = 1
# print(frequency_map)

#method 2

nums = [2,3,45,2,5,6,3,2,6,7,7,6,86,5,3,6,33]
n = len(nums)
hash_map = {}
for i in range(0 , n):
    hash_map[nums[i]] = hash_map.get(nums[i],0) + 1

print(hash_map)