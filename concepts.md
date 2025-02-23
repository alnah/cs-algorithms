### Understanding Logarithms

- **Log(16, base 2)** means: "How many times does 2 need to be multiplied by itself to reach 16?"
- Answer: **4**, because \( 2^4 = 16 \).

---

### Growth Rates: From Slow to Fast

1. **Logarithmic**: \( log_b(n) \) → Very efficient
2. **Linear**: \( a \* n + b \) → Grows steadily
3. **Quadratic**: \( n^n \) → Slow
4. **Factorial**: \( n! \) → Extremely slow

---

### Big-O Complexity Rankings

#### **Excellent** ✅

- **HashMap lookup**: \( O(1) \) → Constant time.

#### **Great** 🏆

- **Binary search in sorted array**: \( O(log(n)) \) → Fast!

#### **Fair** ⚖️

- **Iteration**: \( O(n) \) → Reasonable.
- **Sequence of iterations**: \( O(n \* m) \) → Good for small datasets. 💪
- **Merge Sort**: \( O(n log(n)) \) → Best for large datasets. 💪

#### **Horrible** 😨

- **Nested iterations**: \( O(n^2) \) → Gets slow quickly.
- **Recursive branching**: \( O(2^n) \) → Exponential growth.

#### **Hell** 🔥

- **Generating all permutations**: \( O(n!) \) → Unmanageable for large inputs.

---

### Polynomial vs. Exponential Algorithms

#### **Polynomial Algorithms (P) ✅**

- Examples: \( O(1) \), \( O(n) \), \( O(n log(n)) \), \( O(n^2) \), \( O(n^3) \), … \( O(n^k) \)
- **Runtime**: Grows at most as \( n^k \), where \( k \) is a constant.
- **Computers are good at solving these!**

#### **Exponential Algorithms ❌**

- Examples: \( O(2^n) \), \( O(3^n) \), … \( O(k^n) \)
- **Runtime**: Grows incredibly fast.

#### **Factorial Algorithms ☢️**

- Example: \( O(n!) \)
- **Runtime**: Practically unusable, except in cryptography & security.
- **Future hope?** Quantic computation.

---

### Rules of Thumb 📝

- **Use hashing whenever possible.**
- **Sort once, then search.**
- **Avoid nested loops** unless dealing with small inputs.
- **Recursion is dangerous** unless:
  - You can **early stop**.
  - You can **eliminate branches**.
  - You can **memoize results**.
- **Don’t use educational-purpose algorithms in real-life**; rely on built-in language implementations.

---

### Python Sorting Algorithm (Timsort)

Python uses **Timsort**, a hybrid sorting algorithm optimized for real-world data.

- It is a combination of **MergeSort** and **InsertionSort**.
- It is **stable**, meaning it maintains the relative order of equal elements.
- It adapts well to **partially sorted data**, achieving better-than-**O(n log n)** performance in some cases.
- It performs **MergeSort** on large partitions and falls back to **InsertionSort** for small subarrays.
- It requires **additional memory for merging**, unlike in-place sorting algorithms like **IntroSort**.

---

### Go Sorting Algorithm (IntroSort)

Go uses **IntroSort**, a hybrid sorting algorithm that optimizes performance.

- It begins with **QuickSort** for fast average-case sorting.
- It switches to **HeapSort** when recursion depth exceeds **log₂(input size)** to avoid worst-case **O(n²)** complexity.
- It falls back to **InsertionSort** for small partitions, as it is efficient for small datasets.
- It is **not stable**, meaning the relative order of equal elements is not preserved.
- It is **in-place**, meaning it does **not require extra memory** for sorting, unlike **Timsort**.

---

### JavaScript Sorting Algorithm

JavaScript uses different sorting algorithms depending on the engine implementation:

#### **V8 Engine (Chrome, Node.js)**

- Uses **Timsort** for arrays with **more than 10 elements**.
- Uses **InsertionSort** for **small arrays (≤10 elements)**.
- **Timsort is stable**, preserving the relative order of equal elements.
- Like Python, it is optimized for **real-world data** and **partially sorted input**.
- **Requires additional memory for merging**.

#### **SpiderMonkey Engine (Firefox)**

- Uses **MergeSort** for array sorting.
- **MergeSort is stable**, preserving the order of equal elements.
- **Requires extra memory** for merging.

#### **JavaScriptCore (Safari)**

- Uses a **hybrid QuickSort-based algorithm**.
- **Not guaranteed to be stable**.
- Generally performs well but lacks the adaptive behavior of **Timsort**.

### General JavaScript Sorting Behavior

- JavaScript’s `.sort()` is implemented as an **adaptive, optimized algorithm** based on the engine’s choice.
- By default, JavaScript’s `.sort()` **converts elements to strings** and sorts them **lexicographically**, unless a comparison function is provided.
