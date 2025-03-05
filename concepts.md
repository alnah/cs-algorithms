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

---

### Non deterministic polynominal time (NP) and Polynomial time (P)

#### NP and P

Nondeterministic polynomial time, NP, is the set of problems whose solutions can be verified in polynomial time, but not necessarily solved in polynomial time.

Because all problems that can be solved in polynomial time can also be verified in polynomial time, all the problems in P are also in NP.

![P is in NP](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/vO4GfRb.png)

#### Traveling Salesman Problem

Given a list of cities, the distances between each pair of cities, and a total distance, is there a path through all the cities that is less than the distance given?

![TSP](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/lOCwZI5.png)

#### NP-Complete

Some, but not all problems in NP are also NP-complete. A problem in NP is also NP-complete if every other problem in NP can be reduced to it in polynomial time.

A reducer is an algorithm that transforms some problem, Problem A, into a different problem which is already solved, Problem B. Then, Problem A can be solved with the algorithm for solving Problem B.

Problem A -> reducer -> Problem B -> solver algorithm Problem B -> solution for Problem A

However, the reducer itself needs to be fast. "Problem A is reducible to Problem B" if the reducer can run in polynomial time.

It's easy to verify if that password matches the one we have saved on file. It's literally as easy as:

```python
should_grant_access = user_input == saved_password
```

The useful bit is that it takes much longer to guess the correct password.

#### P == NP ?

The P versus NP problem is a major unsolved problem in computer science. It asks whether every problem whose solution can be quickly verified (is in NP) can also be solved quickly (is in P).

The question is, "Are all NP problems really just P problems?"

The answer is, "We don't know, but probably not".

All problems in NP (you know, hard ones like the traveling salesman problem) have been proven to also be solvable in polynomial time if we can find a solution to just one NP-Complete problem.

If a single NP-complete problem can be solved quickly (in polynomial time) that means that all problems in NP can be solved in polynomial time. That would be a huge deal, particularly because it would break digital security systems that rely on the difficulty of certain NP problems.

#### P != NP ?

We do not know for sure if P equals NP because we can't find any polynomial-time solutions to NP-complete problems. Additionally, we have been unable to prove whether P does not equal NP. We suspect P does not equal NP because it has been so difficult to prove that P = NP.

That said, it's actually more complicated to prove the negative case. To prove the positive case, that P = NP, we simply need to solve an NP-complete problem like TSP in polynomial time. In order to prove the negative case, that P != NP, we would need to exhaustively prove that there's no possible way to solve TSP in polynomial time. That's a lot trickier.

#### NP-Hard

All NP-complete problems are NP-hard, but not all NP-hard problems are NP-complete. The determining factor between NP-complete and NP-hard is that not all NP-hard problems are in NP.

> A problem is NP-hard if every problem in NP can be reduced into it in polynomial time.

Compare this to the slightly different definition of NP-complete:

> A problem is NP-complete if it is in NP and every other problem in NP can be reduced into it in polynomial time.

The difference is that NP-complete problems must be in NP, or in other words, they must be verifiable in polynomial time. NP-hard has no such restriction.

![NP-Hard](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/p8wXLqA.png)
