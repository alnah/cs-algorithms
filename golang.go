package main

// RemoveDuplicates removes duplicates without altering the order,
// that's why we don't use a set.
// - O(2*n)
func RemoveDuplicates(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	// In Go, iterating over a map does not guarantee order.
	// To preserve order, we check membership while iterating.
	seen := make(map[int]bool)
	result := []int{}
	for _, n := range nums {
		if !seen[n] {
			seen[n] = true
			result = append(result, n)
		}
	}
	return result
}

// BinarySearch divides the search range in half until it finds the element.
// - O(log(n))
// - In practice: only works on a pre-sorted list.
func BinarySearch(target int, nums []int) bool {
	if len(nums) == 0 {
		panic("Nums can't be empty")
	}
	start, end := 0, len(nums)-1
	for start <= end {
		median := (start + end) / 2
		if nums[median] == target {
			return true
		} else if nums[median] > target {
			end = median - 1
		} else { // nums[median] < target
			start = median + 1
		}
	}
	return false
}

// BubbleSort iterates over and over an array to swap adjacent elements until it's sorted.
// - Sorted array: O(n)
// - Reversed array: O(n^2)
// - In practice: never used.
func BubbleSort(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	swap := true
	end := len(nums)
	// Sorting in-place
	for swap {
		swap = false
		for i := 1; i < end; i++ {
			if nums[i-1] > nums[i] {
				nums[i-1], nums[i] = nums[i], nums[i-1]
				swap = true
			}
		}
		end--
	}
	return nums
}

// MergeSort divides the problem into smaller problems, and recursively solves the smaller ones.
// Combines the results of the smaller problems to solve the bigger problem.
// - O(n log(n))
// - In practice: greedy with memory, slow on small n's, so use it for big sets.
func MergeSort(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	if len(nums) < 2 {
		return nums
	}
	median := len(nums) / 2
	sortedLeft := MergeSort(nums[:median])
	sortedRight := MergeSort(nums[median:])
	return merge(sortedLeft, sortedRight)
}

// merge compares elements and adds the smaller one to the merged list.
// It then adds any remaining elements from the first and second list.
func merge(left, right []int) []int {
	merged := []int{}
	i, j := 0, 0
	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			merged = append(merged, left[i])
			i++
		} else {
			merged = append(merged, right[j])
			j++
		}
	}
	for i < len(left) {
		merged = append(merged, left[i])
		i++
	}
	for j < len(right) {
		merged = append(merged, right[j])
		j++
	}
	return merged
}

// InsertionSort works by iterating through the list and building a sorted
// portion one element at a time. At each step, the current element is compared
// with the previous ones and inserted into its correct position by shifting
// larger elements to the right.
// - O(n**2): for big datasets.
// - O(n): for small or nearly sorted datasets.
func InsertionSort(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	for i := 1; i < len(nums); i++ {
		j := i
		for j > 0 && nums[j-1] > nums[j] {
			nums[j-1], nums[j] = nums[j], nums[j-1]
			j--
		}
	}
	return nums
}

// QuickSort is a divide-and-conquer sorting algorithm.
// - O(n log(n)) when shuffled data
// - O(n^2) when already sorted data with bad pivot choice
// - In practice: often used due to in-place sorting and average performance.
// - Used in production, but less stable than merge sort.
func QuickSort(nums []int, low, high int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	if low < high {
		pivot := partition(nums, low, high)
		QuickSort(nums, low, pivot-1)
		QuickSort(nums, pivot+1, high)
	}
	return nums
}

// partition places the pivot in the correct position.
// - Chooses the last element as pivot.
// - Moves all smaller elements to the left of pivot.
// - Moves all greater elements to the right.
func partition(nums []int, low, high int) int {
	pivot := nums[high]
	i := low - 1
	for j := low; j < high; j++ {
		if nums[j] <= pivot {
			i++
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	nums[i+1], nums[high] = nums[high], nums[i+1]
	return i + 1
}

// SelectionSort is a simple comparison-based sorting algorithm.
// Finds the smallest element in the unsorted part and swaps it with the first element.
// Repeats the process for the remaining unsorted elements.
// - O(n**2)
// - In practice: more efficient than bubble sort, memory-friendly, not for production.
func SelectionSort(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	n := len(nums)
	for i := 0; i < n; i++ {
		smI := i
		for j := i + 1; j < n; j++ {
			if nums[j] < nums[smI] {
				smI = j
			}
		}
		nums[i], nums[smI] = nums[smI], nums[i]
	}
	return nums
}

// Fibonacci is a polynomial implementation of the fibonacci sequence,
// non-recursive, and very fast!
// - O(n)
func Fibonacci(n int) int {
	if n < 0 {
		panic("Fibonacci sequence must start from 0 or more")
	}
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	grandparent, parent, current := 0, 1, 0
	for i := 0; i < n-1; i++ {
		current = grandparent + parent
		grandparent = parent
		parent = current
	}
	return current
}

// Powerset is an exponential implementation of the powerset to get all possibilities from a set.
// 25 items would take 9 hours, 40 items 34 years!
// - O(2^n)
func Powerset(inputList []int) [][]int {
	if len(inputList) == 0 {
		return [][]int{{}}
	}
	var final [][]int
	head := inputList[0]
	tail := inputList[1:]
	subsets := Powerset(tail)
	for _, s := range subsets {
		// Prepend head to each subset.
		newSubset := make([]int, len(s)+1)
		newSubset[0] = head
		copy(newSubset[1:], s)
		final = append(final, newSubset)
		final = append(final, s)
	}
	return final
}

// tsp checks if any tour (permutation) of cities has total distance less than dist.
// cities is a slice of city indices, and paths is a 2D slice representing the distance between cities.
func tsp(cities []int, paths [][]int, dist int) bool {
	perms := permutations(cities)
	for _, path := range perms {
		total := 0
		for i := 0; i < len(path)-1; i++ {
			total += paths[path[i]][path[i+1]]
		}
		if total < dist {
			return true
		}
	}
	return false
}

// permutations generates all permutations of arr using Heap's algorithm.
func permutations(arr []int) [][]int {
	var res [][]int
	heapPermutation(arr, len(arr), &res)
	return res
}

// heapPermutation recursively generates permutations and appends them to res.
func heapPermutation(arr []int, n int, res *[][]int) {
	if n == 1 {
		// Create a copy of arr before appending
		perm := make([]int, len(arr))
		copy(perm, arr)
		*res = append(*res, perm)
		return
	}
	for i := 0; i < n; i++ {
		heapPermutation(arr, n-1, res)
		// Swap logic depends on whether n is odd or even
		if n%2 == 1 {
			// Swap the last element with the i-th element
			arr[n-1], arr[i] = arr[i], arr[n-1]
		} else {
			// Swap the first element with the last element
			arr[0], arr[n-1] = arr[n-1], arr[0]
		}
	}
}

// verifyTSP verifies if the distance of actualPath is less than dist.
func verifyTSP(paths [][]int, actualPath []int, dist int) bool {
	total := 0
	for i := 1; i < len(actualPath); i++ {
		total += paths[actualPath[i-1]][actualPath[i]]
	}
	return total < dist
}

// getNumGuesses computes the total number of guesses for strings of length 1 to length,
// assuming 26 possible letters at each position.
func getNumGuesses(length int) int {
	total := 0
	for n := 1; n <= length; n++ {
		guess := int(math.Pow(26, float64(n)))
		total += guess
	}
	return total
}

// primeFactors returns the prime factors of n.
func primeFactors(n int) []int {
	var factors []int
	// Factor out all 2s.
	for n%2 == 0 {
		factors = append(factors, 2)
		n /= 2
	}
	// Factor out odd numbers.
	for i := 3; i*i <= n; i += 2 {
		for n%i == 0 {
			factors = append(factors, i)
			n /= i
		}
	}
	// If n is a prime greater than 2.
	if n > 2 {
		factors = append(factors, n)
	}
	return factors
}

// subsetSum checks if any subset of nums sums to target.
func subsetSum(nums []int, target int) bool {
	return findSubsetSum(nums, target, len(nums)-1)
}

// findSubsetSum is a recursive helper for subsetSum.
func findSubsetSum(nums []int, target int, index int) bool {
	if target == 0 {
		return true
	}
	if index < 0 {
		return false
	}
	if nums[index] > target {
		return findSubsetSum(nums, target, index-1)
	}
	return findSubsetSum(nums, target, index-1) || findSubsetSum(nums, target-nums[index], index-1)
}
