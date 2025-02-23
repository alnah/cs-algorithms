// Remove duplicates without altering the order, that's why we don't use a set.
// - O(2*n)
function removeDuplicates(nums: number[]): number[] {
  if (!nums || nums.length === 0) {
    return [];
  }
  const seen: { [key: number]: boolean } = {};
  const result: number[] = [];
  for (const n of nums) {
    if (!seen[n]) {
      seen[n] = true;
      result.push(n);
    }
  }
  return result;
}

// Binary search: Divide the search range in half until it finds the element.
// - O(log(n))
// - In practice: only works on a pre-sorted list.
function binarySearch(target: number, nums: number[]): boolean {
  if (!nums || nums.length === 0) {
    throw new Error("Nums can't be empty");
  }
  let start = 0;
  let end = nums.length - 1;
  while (start <= end) {
    const median = Math.floor((start + end) / 2);
    if (nums[median] === target) {
      return true;
    } else if (nums[median] > target) {
      end = median - 1;
    } else { // nums[median] < target
      start = median + 1;
    }
  }
  return false;
}

// Bubble sort: Iterate over and over an array to swap adjacent elements until it's sorted.
// - Sorted array: O(n)
// - Reversed array: O(n^2)
// - In practice: never used.
function bubbleSort(nums: number[]): number[] {
  if (!nums || nums.length === 0) {
    return [];
  }
  let swap = true;
  let end = nums.length;
  while (swap) {
    swap = false;
    for (let i = 1; i < end; i++) {
      if (nums[i - 1] > nums[i]) {
        [nums[i - 1], nums[i]] = [nums[i], nums[i - 1]];
        swap = true;
      }
    }
    end--;
  }
  return nums;
}

// Merge sort: Divide the problem into smaller problems, and recursively solve the smaller ones.
// Combine the results of the smaller problems to solve the bigger problem.
// - O(n log(n))
// - In practice: greedy with memory, slow on small n's, so use it for big sets.
function mergeSort(nums: number[]): number[] {
  if (!nums || nums.length === 0) {
    return [];
  }
  if (nums.length < 2) {
    return nums;
  }
  const median = Math.floor(nums.length / 2);
  const sortedLeft = mergeSort(nums.slice(0, median));
  const sortedRight = mergeSort(nums.slice(median));
  return merge(sortedLeft, sortedRight);
}

// Helper for mergeSort.
// Compare elements and add the smaller one to merged list.
// Add any remaining elements from first list.
// Add any remaining elements from second list.
function merge(left: number[], right: number[]): number[] {
  const merged: number[] = [];
  let i = 0, j = 0;
  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) {
      merged.push(left[i]);
      i++;
    } else {
      merged.push(right[j]);
      j++;
    }
  }
  while (i < left.length) {
    merged.push(left[i]);
    i++;
  }
  while (j < right.length) {
    merged.push(right[j]);
    j++;
  }
  return merged;
}

// Insertion sort works by iterating through the list and building a sorted
// portion one element at a time. At each step, the current element is compared
// with the previous ones and inserted into its correct position by shifting
// larger elements to the right.
// - O(n**2): for big datasets.
// - O(n): for small or nearly sorted datasets.
function insertionSort(nums: number[]): number[] {
  if (!nums || nums.length === 0) {
    return [];
  }
  for (let i = 1; i < nums.length; i++) {
    let j = i;
    while (j > 0 && nums[j - 1] > nums[j]) {
      [nums[j - 1], nums[j]] = [nums[j], nums[j - 1]];
      j--;
    }
  }
  return nums;
}

// Quick sort: A divide-and-conquer sorting algorithm.
// - O(n log(n)) when shuffled data
// - O(n^2) when already sorted data with bad pivot choice
// - In practice: often used due to in-place sorting and average performance.
// - Used in production, but less stable than merge sort.
function quickSort(nums: number[], low: number, high: number): number[] {
  if (!nums || nums.length === 0) {
    return [];
  }
  if (low < high) {
    const pivot = partition(nums, low, high);
    quickSort(nums, low, pivot - 1);
    quickSort(nums, pivot + 1, high);
  }
  return nums;
}

// Helper for quickSort.
// Places the pivot in the correct position.
// - Chooses the last element as pivot.
// - Moves all smaller elements to the left of pivot.
// - Moves all greater elements to the right.
function partition(nums: number[], low: number, high: number): number {
  const pivot = nums[high];
  let i = low - 1;
  for (let j = low; j < high; j++) {
    if (nums[j] <= pivot) {
      i++;
      [nums[i], nums[j]] = [nums[j], nums[i]];
    }
  }
  [nums[i + 1], nums[high]] = [nums[high], nums[i + 1]];
  return i + 1;
}

// Selection sort: A simple comparison-based sorting algorithm.
// Finds the smallest element in the unsorted part and swaps it with the first element.
// Repeats the process for the remaining unsorted elements.
// - O(n**2)
// - In practice: more efficient than bubble sort, memory-friendly, not for production.
function selectionSort(nums: number[]): number[] {
  if (!nums || nums.length === 0) {
    return [];
  }
  const n = nums.length;
  for (let i = 0; i < n; i++) {
    let smI = i;
    for (let j = i + 1; j < n; j++) {
      if (nums[j] < nums[smI]) {
        smI = j;
      }
    }
    [nums[i], nums[smI]] = [nums[smI], nums[i]];
  }
  return nums;
}

// Fibonacci: Polynomial implementation of fibonacci sequence, non-recursive, and very fast!
// - O(n)
function fibonacci(n: number): number {
  if (n < 0) {
    throw new Error("Fibonacci sequence must start from 0 or more");
  }
  if (n === 0) return 0;
  if (n === 1) return 1;
  let grandparent = 0, parent = 1, current = 0;
  for (let i = 0; i < n - 1; i++) {
    current = grandparent + parent;
    grandparent = parent;
    parent = current;
  }
  return current;
}

// Powerset: Exponential implementation of powerset to get all possibilities from a set.
// 25 items would take 9 hours, 40 items 34 years!
// - O(2^n)
function powerset(inputList: number[]): number[][] {
  if (!inputList || inputList.length === 0) {
    return [[]];
  }
  const final: number[][] = [];
  const head = inputList[0];
  const tail = inputList.slice(1);
  const subsets = powerset(tail);
  for (const s of subsets) {
    final.push([head, ...s]);
    final.push(s);
  }
  return final;
}

