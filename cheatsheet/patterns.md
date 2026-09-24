# DSA Patterns Cheatsheet

For each pattern: **when to use it** (the signals in the question), **the idea**, and **classic problems**.
Code for each one is in [snippets.py](snippets.py).

---

## Quick lookup: "the question says..." → try this

| Signal in the question | Pattern |
|---|---|
| Sorted array, find a pair / triplet | Two Pointers |
| Contiguous subarray / substring, "longest", "shortest", "at most K" | Sliding Window |
| Subarray sum equals K (numbers can be negative) | Prefix Sum + Hash Map |
| Many range-sum queries | Prefix Sum |
| Sorted array, or "minimum X such that..." | Binary Search (on answer) |
| "Remove from the ends", "take from left/right" | Flip it: longest middle window (Sliding Window) |
| Linked list cycle, middle node | Fast & Slow Pointers |
| Overlapping intervals, meetings, schedules | Sort + Merge Intervals |
| Numbers 1..n in an array, find missing/duplicate | Cyclic Sort / index marking |
| Next greater / smaller element | Monotonic Stack |
| Sliding window max / min | Monotonic Deque |
| Top K, K-th largest, "closest K" | Heap |
| Merge K sorted things | Heap (K-way merge) |
| Running median | Two Heaps |
| All combinations / permutations / subsets | Backtracking |
| Shortest path, unweighted, "minimum steps" | BFS |
| Explore everything, count islands, connected parts | DFS / BFS / Union-Find |
| Task ordering, prerequisites, dependencies | Topological Sort |
| Shortest path with weights | Dijkstra |
| "Are these connected?", grouping, merging sets | Union-Find |
| Prefix / word search, autocomplete | Trie |
| "Count ways", "min/max cost", choices overlap | Dynamic Programming |
| Locally best choice is always safe | Greedy (prove it first!) |
| Pairs that appear twice except one, bit tricks | Bit Manipulation (XOR) |

---

## 1. Two Pointers

**When:** sorted array, pairs/triplets summing to a target, reversing, removing duplicates in place, comparing from both ends.

**Idea:** one pointer at each end (or both at the start moving at different speeds). Move the one that brings you closer to the goal.

**Problems:** Two Sum II (167), 3Sum (15), Container With Most Water (11), Remove Duplicates (26), Valid Palindrome (125), Move Zeroes (283).

## 2. Sliding Window

**When:** contiguous subarray/substring + "longest / shortest / count / at most K / exactly K".

**Idea:** grow the window with `right`, shrink it with `left` while it's invalid. Update the answer when it's valid.
- **Fixed size k:** add `nums[right]`, remove `nums[right - k]`.
- **Variable size:** `while invalid: shrink`.
- **Only works cleanly with non-negative numbers** for sum problems. With negatives use Prefix Sum + Hash Map.
- "Exactly K" = atMost(K) − atMost(K − 1).

**Problems:** Longest Substring Without Repeating (3), Min Size Subarray Sum (209), Min Operations to Reduce X to Zero (1658), Minimum Window Substring (76), Max Consecutive Ones III (1004), Fruit Into Baskets (904).

## 3. Prefix Sum

**When:** many range-sum queries, or "subarray sum equals K".

**Idea:** `prefix[i] = sum of nums[0..i-1]`, so `sum(l..r) = prefix[r+1] - prefix[l]`.
For "subarray sum = K": keep a hash map of how many times each prefix sum has appeared, and look up `current - K`.

**Problems:** Range Sum Query (303), Subarray Sum Equals K (560), Contiguous Array (525), Product of Array Except Self (238).

## 4. Hashing (Hash Map / Set)

**When:** "have I seen this before?", counting frequencies, grouping, O(1) lookups.

**Idea:** trade memory for speed. `dict` for counts/positions, `set` for existence.

**Problems:** Two Sum (1), Group Anagrams (49), Longest Consecutive Sequence (128), Valid Anagram (242), Top K Frequent (347).

## 5. Binary Search

**When:** sorted data, OR the answer is a number and you can check "is X enough?" (the check is monotonic: false false false true true true).

**Idea:** keep `lo`, `hi`; look at `mid`; throw away half each step. O(log n).
- **Search on answer:** binary search over possible answers, with a `feasible(x)` function.
- Use `bisect_left` / `bisect_right` in Python for the standard cases.

**Problems:** Binary Search (704), Search in Rotated Array (33), Find Min in Rotated Array (153), Koko Eating Bananas (875), Capacity to Ship Packages (1011), Median of Two Sorted Arrays (4).

## 6. Fast & Slow Pointers

**When:** linked list cycle, middle of list, "happy number"-style repeating sequences.

**Idea:** slow moves 1, fast moves 2. If there's a cycle they meet. When fast hits the end, slow is at the middle.

**Problems:** Linked List Cycle (141, 142), Middle of the Linked List (876), Happy Number (202), Find the Duplicate Number (287).

## 7. Linked List Manipulation

**When:** reverse, merge, reorder, remove nth node.

**Idea:** use a **dummy node** so you never special-case the head. Reverse with `prev, curr` pointers.

**Problems:** Reverse Linked List (206), Merge Two Sorted Lists (21), Remove Nth From End (19), Reorder List (143), Reverse Nodes in k-Group (25).

## 8. Merge Intervals

**When:** intervals, meetings, ranges that overlap.

**Idea:** sort by start. Walk through; if the current start ≤ last end, merge (extend the end), else start a new interval.

**Problems:** Merge Intervals (56), Insert Interval (57), Non-overlapping Intervals (435), Meeting Rooms II (253).

## 9. Cyclic Sort

**When:** array contains numbers in range `1..n` (or `0..n`); find missing / duplicate numbers in O(n) time, O(1) space.

**Idea:** put each number at its correct index (`nums[i]` belongs at `nums[i] - 1`) by swapping. Then scan for the index that's wrong.

**Problems:** Missing Number (268), Find All Numbers Disappeared (448), Find the Duplicate (287), First Missing Positive (41).

## 10. Monotonic Stack

**When:** "next greater element", "previous smaller", "how many days until warmer", histogram areas.

**Idea:** keep a stack whose values are always increasing (or decreasing). When a new value breaks the order, pop — the popped items just found their answer.

**Problems:** Daily Temperatures (739), Next Greater Element (496, 503), Largest Rectangle in Histogram (84), Trapping Rain Water (42).

## 11. Monotonic Deque

**When:** max/min of every window of size k.

**Idea:** a deque of indices whose values are decreasing. Front is always the max. Pop from the front when it slides out of the window.

**Problems:** Sliding Window Maximum (239), Shortest Subarray with Sum at Least K (862).

## 12. Stack (general)

**When:** matching brackets, undo, evaluating expressions, nested structures.

**Problems:** Valid Parentheses (20), Min Stack (155), Evaluate RPN (150), Decode String (394), Simplify Path (71).

## 13. Heap / Priority Queue

**When:** "top K", "K-th largest/smallest", repeatedly need the current min/max, merging sorted lists.

**Idea:** Python's `heapq` is a **min-heap**. For a max-heap, push negatives.
- **Top K largest:** keep a min-heap of size K; pop when it gets bigger than K.
- **K-way merge:** push the first element of each list, pop smallest, push its next.
- **Two heaps:** max-heap for the lower half, min-heap for the upper half → running median.

**Problems:** Kth Largest Element (215), Top K Frequent (347), K Closest Points (973), Merge K Sorted Lists (23), Find Median from Data Stream (295), Task Scheduler (621).

## 14. Trees — DFS

**When:** anything about paths, depth, subtrees, validating a BST.

**Idea:** recursion. Decide what the function returns for a node, assume it works for the children, combine.
- **Preorder** (node, left, right): copying / serializing.
- **Inorder** (left, node, right): BST → sorted order.
- **Postorder** (left, right, node): need children's answers first (height, diameter).

**Problems:** Max Depth (104), Invert Tree (226), Diameter (543), Validate BST (98), Path Sum (112), Lowest Common Ancestor (236), Kth Smallest in BST (230).

## 15. Trees — BFS (Level Order)

**When:** "level by level", "right side view", minimum depth, zigzag.

**Idea:** queue; process `len(queue)` nodes per level.

**Problems:** Level Order Traversal (102), Right Side View (199), Zigzag (103), Min Depth (111).

## 16. Graphs — DFS / BFS

**When:** islands, connected components, flood fill, "can I reach X".

**Idea:** build an adjacency list (or treat a grid as a graph with 4 neighbours). Keep a `visited` set.
- **BFS** gives the **shortest path** in unweighted graphs.
- **Multi-source BFS:** start the queue with all sources (rotting oranges, 01 matrix).

**Problems:** Number of Islands (200), Clone Graph (133), Rotting Oranges (994), Pacific Atlantic (417), Word Ladder (127), Course Schedule (207).

## 17. Topological Sort

**When:** prerequisites, build order, dependencies, detecting cycles in a directed graph.

**Idea (Kahn's):** count incoming edges; queue every node with 0; pop, add to order, decrease neighbours' counts. If order length < n there's a cycle.

**Problems:** Course Schedule I & II (207, 210), Alien Dictionary (269).

## 18. Union-Find (Disjoint Set)

**When:** grouping, "are A and B connected?", counting components while adding edges, redundant edge.

**Idea:** `parent` array; `find` with path compression, `union` by rank/size. Near O(1) per operation.

**Problems:** Number of Provinces (547), Redundant Connection (684), Accounts Merge (721), Graph Valid Tree (261).

## 19. Shortest Paths

- **Unweighted:** BFS.
- **Non-negative weights:** Dijkstra (heap). O(E log V).
- **Negative weights / at most K edges:** Bellman-Ford.
- **All pairs, small n:** Floyd-Warshall.

**Problems:** Network Delay Time (743), Cheapest Flights Within K Stops (787), Path With Minimum Effort (1631).

## 20. Backtracking

**When:** "all combinations / permutations / subsets", N-Queens, Sudoku, word search.

**Idea:** choose → explore → un-choose. Prune early when a path can't work.

**Problems:** Subsets (78), Permutations (46), Combination Sum (39), Palindrome Partitioning (131), N-Queens (51), Word Search (79).

## 21. Dynamic Programming

**When:** "count the ways", "min/max cost", "is it possible", and the same subproblem comes up again and again.

**Steps:**
1. Define the **state**: `dp[i]` = answer for the first i items (or `dp[i][j]`).
2. Write the **transition**: how `dp[i]` comes from smaller states.
3. Set the **base cases**.
4. Pick the **order** (top-down with memo, or bottom-up loop).

**Common shapes:**
- **1D:** Climbing Stairs (70), House Robber (198), Coin Change (322), Decode Ways (91).
- **2D grid:** Unique Paths (62), Min Path Sum (64).
- **Two strings:** LCS (1143), Edit Distance (72).
- **0/1 Knapsack:** Partition Equal Subset Sum (416), Target Sum (494).
- **Unbounded Knapsack:** Coin Change (322), Coin Change II (518).
- **LIS:** Longest Increasing Subsequence (300).
- **Intervals:** Burst Balloons (312), Palindromic Substrings (647).

## 22. Greedy

**When:** a locally best choice is always safe (you can argue why). If you can find a counterexample, it's DP instead.

**Warning:** "pick the bigger end" failed on 1658. Always test greedy on a tricky small case before trusting it.

**Problems:** Jump Game (55, 45), Gas Station (134), Assign Cookies (455), Partition Labels (763), Non-overlapping Intervals (435).

## 23. Trie

**When:** prefix search, autocomplete, word dictionaries, word search on a board.

**Problems:** Implement Trie (208), Add and Search Word (211), Word Search II (212).

## 24. Bit Manipulation

**When:** "every element appears twice except one", subsets as bitmasks, powers of two.

**Tricks:**
- `a ^ a = 0`, `a ^ 0 = a` → XOR everything to find the single one.
- `n & (n - 1)` removes the lowest set bit → power of two check, counting bits.
- `n & 1` → odd/even.
- `1 << k` → k-th bit mask.

**Problems:** Single Number (136), Number of 1 Bits (191), Counting Bits (338), Missing Number (268), Reverse Bits (190).

## 25. Matrix / Grid

**When:** 2D arrays: rotate, spiral, search.

**Tricks:**
- Rotate 90° clockwise = transpose + reverse each row.
- Neighbours: `for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]`.
- Sorted matrix search: start at the top-right corner.

**Problems:** Rotate Image (48), Spiral Matrix (54), Set Matrix Zeroes (73), Search a 2D Matrix (74, 240).

---

## Complexity reminders

| n up to | Target complexity |
|---|---|
| 10 | O(n!) — permutations, backtracking |
| 20 | O(2ⁿ) — subsets, bitmask |
| 500 | O(n³) |
| 5,000 | O(n²) |
| 10⁵ – 10⁶ | O(n log n) or O(n) |
| 10⁹+ | O(log n) or O(1) — binary search / math |

| Operation | list | dict / set | heapq | deque |
|---|---|---|---|---|
| Access by index | O(1) | — | — | O(n) |
| Search | O(n) | O(1) | O(n) | O(n) |
| Insert/remove at end | O(1) | O(1) | O(log n) | O(1) |
| Insert/remove at front | O(n) | — | — | O(1) |
| Get min | O(n) | O(n) | O(1) | O(n) |
