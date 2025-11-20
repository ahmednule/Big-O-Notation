# Big O Notation — The Foundation

Big O notation describes the time and space complexity of algorithms, essentially how they scale with input size. It answers the question: **How will this algorithm perform as the data grows?**

## Key Concepts

- **Time Complexity:** How many operations an algorithm performs.  
- **Space Complexity:** How much extra memory an algorithm requires.  
- **Worst-case scenario:** Big O represents the upper bound of performance.

## Common Complexities (from best to worst)

- **O(1) — Constant:** Same time regardless of input size.  
- **O(log n) — Logarithmic:** Problem size is halved each step.  
- **O(n) — Linear:** Time grows proportionally with input.  
- **O(n log n) — Linearithmic:** Common in efficient sorting algorithms.  
- **O(n²) — Quadratic:** Typically found in nested loops.  
- **O(2ⁿ) — Exponential:** Recursive solutions without memoization.
