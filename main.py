

def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    result = []
    tmp = []
    nums = sorted(set(nums))
    
    for num in range(len(nums)):
        if tmp == []:
            tmp.append(nums[num])

        elif tmp[-1] == nums[num] - 1:
            tmp.append(nums[num])

        elif len(result) < len(tmp):
            result = tmp
            tmp = []
            tmp.append(nums[num])

        else:
            tmp = []
            tmp.append(nums[num])
            
    if len(tmp) > len(result):
        return len(tmp)
    
    return len(result)        

nums = [0, -1, 1, -2, 2, -3, 3]
if __name__ == "__main__":
    print(longest_consecutive(nums))
