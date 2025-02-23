def remove_duplicates(nums: list[int]) -> list[int]:
    """
    Remove duplicates without altering the order, that's why we don't use a set.
    - O(2*n)
    """
    if not nums:
        return []
    deduped_map, deduped_list = {}, []
    for n in nums:
        deduped_map[n] = None
    for n in deduped_map:
        deduped_list.append(n)
    return deduped_list


def binary_search(target: int, nums: list[int]) -> bool:
    """
    Divide the search range in half until it finds the element.
    - 0(log(n))
    - In practice: only work on a pre-sorted list.
    """
    if not nums:
        raise ValueError("Nums can't be empty")
    start, end = 0, len(nums) - 1
    while start <= end:
        median = (start + end) // 2
        if nums[median] == target:
            return True
        elif nums[median] > target:
            end = median - 1
        elif nums[median] < target:
            start = median + 1
    return False


def bubble_sort(nums: list[int]) -> list[int]:
    """
    Iterate over and over an array to swap adjacent elements until its sorted.
    - Sorted array: O(n)
    - Reversed array: O(n^2)
    - In pratice: never used.
    """
    if not nums:
        return []
    swap, end = True, len(nums)
    while swap:
        swap = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swap = True
        end -= 1
    return nums


def merge_sort(nums: list[int]):
    """
    Divide the problem into smaller problems, and recursively solve the smaller ones.
    Combine the results of the smaller problems to solve the bigger problem.
    - O(n log(n))
    - In pratice: greedy with memory, slow in small n's, so use it for big sets.
    """
    if not nums:
        return []
    def merge(left: list[int], right: list[int]) -> list[int]:
        """
        Compare elements and add the smaller one to merged list.
        Add any remaining elements from first list.
        Add any remaining elements from second list.
        """
        merged, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

    # Merge sort starts here
    if len(nums) < 2:
        return nums
    median = len(nums) // 2
    sorted_left, sorted_right = nums[:median], nums[median:]
    return merge(merge_sort(sorted_left), merge_sort(sorted_right))


def insertion_sort(nums: list[int]) -> list[int]:
    """
    Insertion sort works by iterating through the list and building a sorted
    portion one element at a time. At each step, the current element is compared
    with the previous ones and inserted into its correct position by shifting
    larger elements to the right.
    - O(n**2): for big datasets.
    - O(n): fir small or nearly sorted datasets.
    """
    if not nums:
        return []
    length = len(nums)
    for i in range(1, length):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums


def quick_sort(nums: list[int], low: int, high: int) -> list[int]:
    """
    A divide-and-conquer sorting algorithm.
    - O(n log(n)) when shuffled data
    - O(n^2) when already sorted data with bad pivot choice
    - In practice: often used due to in-place sorting and average performance.
    - Used in production, but less stable than merge sort.
    """
    if not nums:
        return []
    def partition(nums: list[int], low: int, high: int) -> int:
        """
        Places the pivot in the correct position.
        - Chooses the last element as pivot.
        - Moves all smaller elements to the left of pivot.
        - Moves all greater elements to the right.
        """
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    # Recursion starts here
    if low < high:
        pivot = partition(nums, low, high)
        quick_sort(nums, low, pivot - 1)
        quick_sort(nums, pivot + 1, high)
    return nums


def selection_sort(nums: list[int]) -> list[int]:
    """
    A simple comparison-based sorting algorithm. Finds the smallest element in the
    unsorted part and swaps it with the first element. Repeats the process for the
    remaining unsorted elements.
    - O(n**2)
    - In practice: more efficient than bubble sort, memory-friendly, not for production.
    """
    if not nums:
        return []
    end = len(nums)
    for i in range(end):
        sm_i = i
        for j in range(sm_i + 1, end):
            if nums[j] < nums[sm_i]:
                sm_i = j
        nums[i], nums[sm_i] = nums[sm_i], nums[i]
    return nums


def fibonacci(n: int) -> int:
    """
    Polynomial implementation of fibonacci sequence, non-recursive, and very fast!
    - O(n)
    """
    if n < 0:
        raise ValueError("Fibonacci sequence must start from 0 or more")
    if n == 0:
        return 0
    if n == 1:
        return 1
    grandparent, parent, current = 0, 1, 0
    for n in range(n - 1):
        current = grandparent + parent
        grandparent = parent
        parent = current
    return current

def powerset(input_list: list[int]) -> list[list[int]]:
    """
    Exponential implementation of powerset to get all possobilities from a set.
    25 items would take 9 hours, 40 items 34 years!
    - O(2^n) 
    """
    if not input_list:
        return [[]]
    final =  []
    head, tail = input_list[0], input_list[1:]
    subsets = powerset(tail)
    for s in subsets:
        final.append([head] + s)
        final.append(s)
    return final
