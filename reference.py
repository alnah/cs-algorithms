
"""
Remember:
- Log(16, base 2) means "How many times 2 need to be multiplied by itself to react 16?"

From slow to fast:
- logarithmic: log(n, b)
- linear: (a * n) + b
- quadratic: n ** n
- factorial: !n

Excellent:
- hashmap lookup: O(1)
Great:
- binary search in sorted array: 0(log(n))
Fair:
- iteration: O(n)
- sequence of iterations: 0(nm)
Horrible:
- nested iterations: 0(n^2)
- recursive branching: 0(2^n)
Hell:
- generating all permutations: O(n!)
"""


def binary_search(target: int, array: list[int]) -> bool:
    """
        Divide the search range in half until it finds the element
        - 0(log(n))
        - In practice: only work on a pre-sorted list
    """
    start, end = 0, len(array) - 1
    while start <= end:
        median = (start + end) // 2
        if array[median] == target:
            return True
        elif array[median] > target:
            end = median - 1
        elif array[median] < target:
            start = median + 1
    return False


def bubble_sort(nums: list[int]) -> list[int]:
    """
        Iterate over and over an array to swap adjacent elements until its sorted.
        - Sorted array: O(n)
        - Reversed array: O(n^2)
        - In pratice: never used
    """
    swap, end = True, len(nums)
    while swap:
        swap = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swap = True
        end -= 1
    return nums

def merge_sort(nums: list[int]):
    """
        Divide the problem into smaller problems, and recursively solve the smaller ones
        Combine the results of the smaller problems to solve the bigger problem
        - O(n log(n))
        - In pratice: greedy with memory, slow in small n's, so use it for big sets
    """
    if len(nums) < 2:
        return nums
    median = len(nums) // 2
    sorted_left, sorted_right = nums[:median], nums[median:]
    return merge(merge_sort(sorted_left), merge_sort(sorted_right))
    
def merge(left: list[int], right: list[int]) -> list[int]:
    merged, i, j = [], 0, 0
    # Compare elements and add the smaller one to merged list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Add any remaining elements from first list
    while i < len(left):
        merged.append(left[i])
        i += 1
    # Add any remaining elements from second list
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

