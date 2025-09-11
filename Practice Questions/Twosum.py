# adding number in the array to get the target sum

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (f"This is the target sum {target} and the numbers are {nums[i]} and {nums[j]}. in the indexes {i} and {j}")
            else:
                return "No two numbers add up to the target sum."

two_sum([2,7,11,15], 9)
print(two_sum([2,7,11,15], 9))



# new_list = [1,2,3,4,5]

# for x in range(len(new_list)):
#     print(x)
#     # new_map = x + (x+1)
#     # if new_map == 9:
#     #     print(f"This is the target sum {new_map} and the numbers are {x} and {x+1}. in the indexes {new_list.index(x)} and {new_list.index(x+1)}")
#     #     break
#     # else:
#     #     x += 1