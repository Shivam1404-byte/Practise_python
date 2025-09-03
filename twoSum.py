print("Two Sum ")

def twoSum(arr,target):
    my_dict = {}

    for i,num in enumerate(arr):
        complement = target - num
        if complement in my_dict:
            return [my_dict[complement],i]
        my_dict[num] = i

    return []

arr = [2,7,11,5]
target = 9
print(twoSum(arr,target))