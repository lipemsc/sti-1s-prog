nums = list()
for i in range(3):
    nums.append(float(input("Insira o {0}º num: ".format(i + 1))))
# print(nums)
if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        print(nums[0])
    else:
        print(nums[2])
else:
    if nums[1] > nums[2]:
        print(nums[1])
    else:
        print(nums[2])