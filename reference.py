"""
Remember:
- Log(16, base 2) means "How many times 2 need to be multiplied by itself to react 16?"

From slow to fast:
- logarithmic: log(n, b)
- linear: (a * n) + b
- quadratic: n ** n
- factorial: !n

Big-O complexity:
- Excellent:
    * hashmap lookup: O(1)

- Great:
    * binary search in sorted array: 0(log(n))

- Fair:
    * iteration: O(n)
    * sequence of iterations: 0(n*m) 💪 best on smallest sets
    * merge sort: O(n*log(n)) 💪 best on largest sets

- Horrible:
    * nested iterations: 0(n**2)
    * recursive branching: 0(2**n)

- Hell:
    * generating all permutations: O(n!)

Computers are good to solve (P) polynomial problems.
- Polynomial algorithms (P) ✅:
    * O(1), O(n), O(n*log(n)), O(n^2), O(n^3), ... O(n^k)
    * Runtime: doesn't grow faster than n^k, where k is a constant,
    and n the size of the input.

- Exponential algorithms ❌:
    * O(2^n), O(3^n), ... O(k^n)
    * Runtime: grows faster.
    
- Factorial algorithms ☢️:
    * O(n!)
    * Runtime: terrible, we only use them in cryptography, and security.
    * Future: quantic computation?

Rules of Thumbs:
- use hashing whenever possible
- sort once, then search
- avoid nested loops, unless dealing with small inputs
- recursion is dangerous unless you can:
    * early stop
    * eliminate branch
    * memoize
- don't use educational purpose algorithms in reaf-life, but rely on the language implementation.
"""

"""
    Python uses Timsort: a hybrid sorting algorithm optimized for real-world data.
    - It is a combination of MergeSort and InsertionSort.
    - It is stable, meaning it maintains the relative order of equal elements.
    - It adapts well to partially sorted data, achieving better-than-O(n log n) performance in some cases.
    - It performs MergeSort on large partitions and falls back to InsertionSort for small subarrays.
    - It requires additional memory for merging, unlike in-place sorting algorithms like IntroSort.
"""

"""
    Go uses IntroSort: a hybrid sorting algorithm that optimizes performance.
     - It begins with QuickSort for fast average-case sorting.
     - It switches to HeapSort when recursion depth exceeds a level based on log2(input size) to avoid worst-case O(n²)
     - It falls back to InsertionSort for small partitions, as it is efficient for small datasets.
     - It is not stable, meaning the relative order of equal elements is not preserved.
     - It is in-place, meaning it does not require extra memory for sorting, unlike Timsort. 
"""


def remove_duplicates(nums: list[int]) -> list[int]:
    """
    Remove duplicates without altering the order, that's why we don't use a set.
    - O(2*n)
    """
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
    length = len(nums)
    for i in range(1, length):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
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
    end = len(nums)
    for i in range(end):
        sm_i = i
        for j in range(sm_i+1, end):
            if nums[j] < nums[sm_i]:
                sm_i = j
        nums[i], nums[sm_i] = nums[sm_i], nums[i]
    return nums
