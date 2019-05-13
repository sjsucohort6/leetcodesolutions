#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(nums, target) :
    """
    Algo:
    1. Create a map with first element from list as key and its index as value.
    2. Iterate the remaining elements in the list and check if corresponding (target-num) key is present in the map.
    3. If found in map, return the current element's index and the one in the map.
    4. If not found, add the element as key and its index as value to the map.

    Time complexity: O(n) as we iterate the array just 1 time.
    Space complexity: O(n) worst case
    """
    map = {}
    map[nums[0]] = 0

    for i in range(1,len(nums)):
        num = nums[i]
        if (target - num) in map:
            return [map[target - num], i]
        else:
            map[nums[i]] = i 
    

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

# print(twoSum([2,7,11,15], 9))
# print(twoSum([3,2,4], 6))
print(twoSum([4,6], 10))
print(twoNumberSum([4,6], 10))