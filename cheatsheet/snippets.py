"""
DSA Code Snippets (Python)

Ready-to-copy code for common operations and patterns.
See patterns.md for when to use each pattern.

Run this file to check every snippet: python snippets.py
"""

from collections import Counter, defaultdict, deque, OrderedDict
from bisect import bisect_left, bisect_right, insort
from functools import lru_cache
import heapq


# =============================================================================
# 1. LISTS / ARRAYS — everyday operations
# =============================================================================

def list_basics():
    nums = [5, 2, 8, 1, 9, 2]

    # ---- sorting ----
    a = sorted(nums)                      # new sorted list      [1,2,2,5,8,9]
    b = sorted(nums, reverse=True)        # descending           [9,8,5,2,2,1]
    nums_copy = nums[:]
    nums_copy.sort()                      # sorts in place, returns None
    pairs = [(3, 'c'), (1, 'a'), (2, 'b')]
    pairs.sort(key=lambda p: p[0])        # sort by first item
    words = ["bb", "a", "ccc"]
    words.sort(key=len)                   # sort by length
    people = [("amy", 30), ("bob", 25), ("cat", 30)]
    people.sort(key=lambda p: (-p[1], p[0]))   # age desc, then name asc

    # ---- adding ----
    nums.append(7)                        # add at end          O(1)
    nums.insert(0, 100)                   # add at index 0      O(n)
    nums.extend([3, 4])                   # add many at end

    # ---- deleting ----
    nums.pop()                            # remove last         O(1)
    nums.pop(0)                           # remove first        O(n)
    del nums[1]                           # remove by index
    nums.remove(8)                        # remove first 8 found (error if missing)
    nums = [x for x in nums if x != 2]    # remove ALL 2s
    del nums[1:3]                         # remove a slice

    # ---- searching ----
    arr = [4, 7, 1, 7]
    idx = arr.index(7)                    # first index of 7 (error if missing)
    has = 7 in arr                        # True/False        O(n)
    cnt = arr.count(7)                    # how many 7s

    # ---- reversing / slicing ----
    r1 = arr[::-1]                        # reversed copy
    arr.reverse()                         # reverse in place
    first_two = arr[:2]
    last_two = arr[-2:]
    every_other = arr[::2]

    # ---- rearranging ----
    k = 2
    rotated_right = arr[-k:] + arr[:-k]   # rotate right by k
    rotated_left = arr[k:] + arr[:k]      # rotate left by k
    arr[0], arr[1] = arr[1], arr[0]       # swap two items

    # ---- building ----
    zeros = [0] * 5
    grid = [[0] * 3 for _ in range(4)]    # 4 rows x 3 cols (NOT [[0]*3]*4)
    squares = [x * x for x in range(5)]
    evens = [x for x in range(10) if x % 2 == 0]

    # ---- useful built-ins ----
    total, biggest, smallest = sum(arr), max(arr), min(arr)
    for i, val in enumerate(arr):         # index + value
        pass
    for x, y in zip([1, 2], [3, 4]):      # walk two lists together
        pass

    return a, b, words, people, rotated_right


def move_zeroes(nums):
    """Move all 0s to the end, keep order of the rest. In place."""
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
    return nums


def remove_duplicates_sorted(nums):
    """Remove duplicates in place from a sorted list. Returns new length."""
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def rotate_in_place(nums, k):
    """Rotate right by k with O(1) extra space (three reverses)."""
    n = len(nums)
    k %= n

    def rev(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    rev(0, n - 1)
    rev(0, k - 1)
    rev(k, n - 1)
    return nums


def dutch_flag(nums):
    """Sort an array of 0s, 1s, 2s in one pass (Sort Colors, 75)."""
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


# =============================================================================
# 2. STRINGS
# =============================================================================

def string_basics():
    s = "  Hello World  "
    t = s.strip()                         # remove spaces at both ends
    low, up = t.lower(), t.upper()
    parts = t.split()                     # ['Hello', 'World']
    joined = "-".join(parts)              # 'Hello-World'
    rev = t[::-1]
    replaced = t.replace("World", "There")
    found = t.find("World")               # index or -1
    starts = t.startswith("He")
    is_digit, is_alpha, is_alnum = "123".isdigit(), "abc".isalpha(), "a1".isalnum()

    # strings are immutable: build with a list, then join
    chars = list("hello")
    chars[0] = "j"
    new = "".join(chars)                  # 'jello'

    # char <-> number
    pos = ord("c") - ord("a")             # 2
    ch = chr(ord("a") + 2)                # 'c'

    # sorted string (anagram key)
    key = "".join(sorted("listen"))       # 'eilnst'

    return joined, new, pos, ch, key


def is_palindrome(s):
    """Ignore non-alphanumeric chars and case (Valid Palindrome, 125)."""
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


# =============================================================================
# 3. HASH MAP / SET
# =============================================================================

def hashing_basics():
    d = {}
    d["a"] = 1                            # add / update
    val = d.get("z", 0)                   # safe get with default
    d.pop("a", None)                      # delete (no error if missing)
    for key, value in d.items():
        pass

    counts = Counter("banana")            # {'a':3,'n':2,'b':1}
    top2 = counts.most_common(2)          # [('a',3),('n',2)]

    groups = defaultdict(list)            # no KeyError, starts as []
    for word in ["eat", "tea", "tan"]:
        groups["".join(sorted(word))].append(word)

    s = set([1, 2, 3])
    s.add(4)
    s.discard(10)                         # remove, no error if missing
    union, inter, diff = s | {5}, s & {1, 2}, s - {1}

    return top2, dict(groups), union, inter, diff


def two_sum(nums, target):
    """Indices of the two numbers that add to target (1)."""
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


def longest_consecutive(nums):
    """Length of the longest run of consecutive numbers, O(n) (128)."""
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 not in s:                # only start at the beginning of a run
            length = 1
            while x + length in s:
                length += 1
            best = max(best, length)
    return best


# =============================================================================
# 4. TWO POINTERS
# =============================================================================

def pair_with_sum_sorted(nums, target):
    """Sorted array: return indices of a pair adding to target."""
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        if s < target:
            l += 1
        else:
            r -= 1
    return []


def three_sum(nums):
    """All unique triplets that sum to 0 (15)."""
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res


# =============================================================================
# 5. SLIDING WINDOW
# =============================================================================

def max_sum_fixed_window(nums, k):
    """Max sum of any window of size k."""
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        best = max(best, window)
    return best


def longest_substring_no_repeat(s):
    """Variable window: longest substring without repeating chars (3)."""
    last_seen = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


def min_subarray_len(target, nums):
    """Shortest subarray with sum >= target (209). Non-negative nums."""
    left = window = 0
    best = float("inf")
    for right in range(len(nums)):
        window += nums[right]
        while window >= target:
            best = min(best, right - left + 1)
            window -= nums[left]
            left += 1
    return 0 if best == float("inf") else best


def min_operations_reduce_x(nums, x):
    """1658: remove from ends = keep the longest middle window."""
    target = sum(nums) - x
    if target < 0:
        return -1
    if target == 0:
        return len(nums)
    left = window = 0
    longest = -1
    for right in range(len(nums)):
        window += nums[right]
        while window > target:
            window -= nums[left]
            left += 1
        if window == target:
            longest = max(longest, right - left + 1)
    return -1 if longest == -1 else len(nums) - longest


# =============================================================================
# 6. PREFIX SUM
# =============================================================================

def build_prefix(nums):
    """prefix[i] = sum of nums[0..i-1];  sum(l..r) = prefix[r+1] - prefix[l]"""
    prefix = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x
    return prefix


def subarray_sum_equals_k(nums, k):
    """Count subarrays with sum k. Works with negatives (560)."""
    count = current = 0
    seen = {0: 1}
    for x in nums:
        current += x
        count += seen.get(current - k, 0)
        seen[current] = seen.get(current, 0) + 1
    return count


# =============================================================================
# 7. BINARY SEARCH
# =============================================================================

def binary_search(nums, target):
    """Classic: index of target or -1."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(nums, target):
    """First index with nums[i] >= target (same as bisect_left)."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_examples():
    a = [1, 3, 3, 3, 7]
    first = bisect_left(a, 3)             # 1
    after = bisect_right(a, 3)            # 4
    how_many_3 = after - first            # 3
    insort(a, 5)                          # insert and keep sorted
    return first, after, how_many_3, a


def min_eating_speed(piles, h):
    """Binary search on the answer (Koko, 875)."""
    def feasible(speed):
        return sum((p + speed - 1) // speed for p in piles) <= h

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def search_rotated(nums, target):
    """Search in rotated sorted array (33)."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:                 # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                     # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# =============================================================================
# 8. SORTING ALGORITHMS (know how they work)
# =============================================================================

def bubble_sort(a):
    a = a[:]
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(a):
    """O(n log n), stable."""
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]


def quick_sort(a):
    """O(n log n) average."""
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    return (quick_sort([x for x in a if x < pivot])
            + [x for x in a if x == pivot]
            + quick_sort([x for x in a if x > pivot]))


def counting_sort(a):
    """O(n + k) for small non-negative integers."""
    if not a:
        return a
    count = [0] * (max(a) + 1)
    for x in a:
        count[x] += 1
    out = []
    for val, c in enumerate(count):
        out.extend([val] * c)
    return out


def quickselect_kth_largest(nums, k):
    """K-th largest in O(n) average (215)."""
    pivot = nums[len(nums) // 2]
    bigger = [x for x in nums if x > pivot]
    equal = [x for x in nums if x == pivot]
    smaller = [x for x in nums if x < pivot]
    if k <= len(bigger):
        return quickselect_kth_largest(bigger, k)
    if k <= len(bigger) + len(equal):
        return pivot
    return quickselect_kth_largest(smaller, k - len(bigger) - len(equal))


# =============================================================================
# 9. INTERVALS
# =============================================================================

def merge_intervals(intervals):
    """Merge overlapping intervals (56)."""
    intervals.sort(key=lambda iv: iv[0])
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def min_meeting_rooms(intervals):
    """How many rooms needed at once (253)."""
    intervals.sort(key=lambda iv: iv[0])
    ends = []                                     # min-heap of end times
    for start, end in intervals:
        if ends and ends[0] <= start:
            heapq.heappop(ends)
        heapq.heappush(ends, end)
    return len(ends)


# =============================================================================
# 10. CYCLIC SORT
# =============================================================================

def find_missing_numbers(nums):
    """Numbers 1..n; return the ones missing (448)."""
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    return [i + 1 for i in range(len(nums)) if nums[i] != i + 1]


# =============================================================================
# 11. STACK / QUEUE / DEQUE
# =============================================================================

def stack_queue_basics():
    stack = []
    stack.append(1)                       # push
    stack.append(2)
    top = stack[-1]                       # peek
    stack.pop()                           # pop -> 2

    q = deque()
    q.append(1)                           # enqueue at right
    q.append(2)
    front = q.popleft()                   # dequeue from left -> 1  O(1)
    q.appendleft(0)                       # add at left
    q.pop()                               # remove from right
    return top, front


def valid_parentheses(s):
    """(20)"""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


def next_greater(nums):
    """Monotonic stack: next greater element to the right, -1 if none."""
    res = [-1] * len(nums)
    stack = []                                    # indices, values decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            res[stack.pop()] = x
        stack.append(i)
    return res


def daily_temperatures(temps):
    """Days until a warmer day (739)."""
    res = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res


def sliding_window_max(nums, k):
    """Monotonic deque (239)."""
    dq = deque()                                  # indices, values decreasing
    res = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res


# =============================================================================
# 12. HEAP / PRIORITY QUEUE
# =============================================================================

def heap_basics():
    h = []
    heapq.heappush(h, 5)
    heapq.heappush(h, 1)
    heapq.heappush(h, 3)
    smallest = h[0]                       # peek min
    popped = heapq.heappop(h)             # 1

    nums = [4, 1, 7, 3]
    heapq.heapify(nums)                   # list -> heap in O(n)

    # max-heap: push negatives
    maxh = []
    for x in [4, 1, 7]:
        heapq.heappush(maxh, -x)
    biggest = -heapq.heappop(maxh)        # 7

    # tuples: sorted by first item, then second
    tasks = []
    heapq.heappush(tasks, (2, "write"))
    heapq.heappush(tasks, (1, "read"))
    first_task = heapq.heappop(tasks)     # (1, 'read')

    k_largest = heapq.nlargest(2, [4, 1, 7, 3])    # [7, 4]
    k_smallest = heapq.nsmallest(2, [4, 1, 7, 3])  # [1, 3]
    return smallest, popped, biggest, first_task, k_largest, k_smallest


def top_k_frequent(nums, k):
    """(347)"""
    counts = Counter(nums)
    return [x for x, _ in heapq.nlargest(k, counts.items(), key=lambda p: p[1])]


def kth_largest_heap(nums, k):
    """Keep a min-heap of size k (215)."""
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]


def merge_k_sorted_lists(lists):
    """K-way merge of Python lists."""
    h = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(h)
    out = []
    while h:
        val, i, j = heapq.heappop(h)
        out.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(h, (lists[i][j + 1], i, j + 1))
    return out


class MedianFinder:
    """Two heaps: running median (295)."""

    def __init__(self):
        self.low = []                     # max-heap (negatives)
        self.high = []                    # min-heap

    def add(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2


# =============================================================================
# 13. LINKED LIST
# =============================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_pylist(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def merge_two_sorted(a, b):
    dummy = cur = ListNode()
    while a and b:
        if a.val <= b.val:
            cur.next, a = a, a.next
        else:
            cur.next, b = b, b.next
        cur = cur.next
    cur.next = a or b
    return dummy.next


def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


def delete_value(head, val):
    """Delete every node with this value."""
    dummy = ListNode(0, head)
    cur = dummy
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next


# =============================================================================
# 14. TREES
# =============================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build from LeetCode-style level order list, None = empty."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []


def inorder_iterative(root):
    res, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


def level_order(root):
    """BFS level by level (102)."""
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def diameter(root):
    """Longest path (edges) between any two nodes (543)."""
    best = 0

    def height(node):
        nonlocal best
        if not node:
            return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)

    height(root)
    return best


def is_valid_bst(root, lo=float("-inf"), hi=float("inf")):
    if not root:
        return True
    if not lo < root.val < hi:
        return False
    return is_valid_bst(root.left, lo, root.val) and is_valid_bst(root.right, root.val, hi)


def bst_insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    else:
        root.right = bst_insert(root.right, val)
    return root


def bst_delete(root, key):
    """(450)"""
    if not root:
        return None
    if key < root.val:
        root.left = bst_delete(root.left, key)
    elif key > root.val:
        root.right = bst_delete(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        succ = root.right                         # smallest in right subtree
        while succ.left:
            succ = succ.left
        root.val = succ.val
        root.right = bst_delete(root.right, succ.val)
    return root


def lowest_common_ancestor(root, p, q):
    """p, q are values (236)."""
    if not root or root.val in (p, q):
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


# =============================================================================
# 15. GRAPHS
# =============================================================================

def build_graph(n, edges, directed=False):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph


def dfs(graph, start):
    visited = set()
    order = []

    def go(node):
        visited.add(node)
        order.append(node)
        for nei in graph[node]:
            if nei not in visited:
                go(nei)

    go(start)
    return order


def bfs_shortest_path(graph, start, goal):
    """Fewest edges from start to goal, -1 if unreachable."""
    q = deque([(start, 0)])
    visited = {start}
    while q:
        node, dist = q.popleft()
        if node == goal:
            return dist
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))
    return -1


def num_islands(grid):
    """Grid DFS (200)."""
    rows, cols = len(grid), len(grid[0])
    seen = set()

    def sink(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if grid[r][c] != "1" or (r, c) in seen:
            return
        seen.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            sink(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in seen:
                sink(r, c)
                count += 1
    return count


def rotting_oranges(grid):
    """Multi-source BFS (994)."""
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while q and fresh:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
    return minutes if fresh == 0 else -1


def topo_sort(n, edges):
    """Kahn's algorithm. edges: (a, b) means a before b. [] if cycle."""
    graph = defaultdict(list)
    indeg = [0] * n
    for a, b in edges:
        graph[a].append(b)
        indeg[b] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph[node]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)
    return order if len(order) == n else []


def dijkstra(n, edges, src):
    """edges: (u, v, w). Returns shortest distance to every node."""
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    dist = [float("inf")] * n
    dist[src] = 0
    h = [(0, src)]
    while h:
        d, u = heapq.heappop(h)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(h, (dist[v], v))
    return dist


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path compression
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                                    # already connected
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


# =============================================================================
# 16. BACKTRACKING
# =============================================================================

def subsets(nums):
    """(78)"""
    res = []

    def go(i, path):
        if i == len(nums):
            res.append(path[:])
            return
        path.append(nums[i])              # choose
        go(i + 1, path)                   # explore
        path.pop()                        # un-choose
        go(i + 1, path)

    go(0, [])
    return res


def permutations(nums):
    """(46)"""
    res = []
    used = [False] * len(nums)

    def go(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                go(path)
                path.pop()
                used[i] = False

    go([])
    return res


def combination_sum(candidates, target):
    """Reuse allowed (39)."""
    res = []

    def go(start, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                path.append(candidates[i])
                go(i, remaining - candidates[i], path)
                path.pop()

    candidates.sort()
    go(0, target, [])
    return res


# =============================================================================
# 17. DYNAMIC PROGRAMMING
# =============================================================================

def climb_stairs(n):
    """1D DP with two variables (70)."""
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def house_robber(nums):
    """(198)"""
    take = skip = 0
    for x in nums:
        take, skip = skip + x, max(take, skip)
    return max(take, skip)


def coin_change(coins, amount):
    """Fewest coins (322). Unbounded knapsack."""
    dp = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


def can_partition(nums):
    """0/1 knapsack: split into two equal-sum halves (416)."""
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [True] + [False] * target
    for x in nums:
        for s in range(target, x - 1, -1):        # backwards for 0/1
            dp[s] = dp[s] or dp[s - x]
    return dp[target]


def unique_paths(m, n):
    """2D grid DP (62)."""
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[-1][-1]


def lcs(a, b):
    """Longest common subsequence (1143)."""
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def edit_distance(a, b):
    """(72)"""
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[-1][-1]


def length_of_lis(nums):
    """Longest increasing subsequence in O(n log n) (300)."""
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


@lru_cache(maxsize=None)
def fib_memo(n):
    """Top-down DP: just add @lru_cache to the recursion."""
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)


# =============================================================================
# 18. GREEDY
# =============================================================================

def can_jump(nums):
    """(55)"""
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + x)
    return True


def max_subarray(nums):
    """Kadane's algorithm (53)."""
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


# =============================================================================
# 19. TRIE
# =============================================================================

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True                          # end of word

    def search(self, word):
        node = self._walk(word)
        return node is not None and "$" in node

    def starts_with(self, prefix):
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node


# =============================================================================
# 20. BIT MANIPULATION
# =============================================================================

def bit_tricks():
    single = 0
    for x in [4, 1, 2, 1, 2]:
        single ^= x                               # 4 (pairs cancel)
    n = 16
    is_power_of_two = n > 0 and n & (n - 1) == 0
    ones = bin(13).count("1")                     # 3
    is_odd = 7 & 1 == 1
    kth_bit_set = (13 >> 2) & 1 == 1              # bit 2 of 1101 -> 1
    all_subsets = [[x for j, x in enumerate("abc") if mask >> j & 1]
                   for mask in range(1 << 3)]
    return single, is_power_of_two, ones, is_odd, kth_bit_set, len(all_subsets)


# =============================================================================
# 21. MATRIX
# =============================================================================

def rotate_matrix(m):
    """90° clockwise in place (48): transpose, then reverse each row."""
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    for row in m:
        row.reverse()
    return m


def spiral_order(m):
    """(54)"""
    res = []
    while m:
        res += m.pop(0)                           # top row
        m = [list(row) for row in zip(*m)][::-1]  # rotate the rest left
    return res


def matrix_tricks():
    m = [[1, 2, 3], [4, 5, 6]]
    transposed = [list(row) for row in zip(*m)]   # [[1,4],[2,5],[3,6]]
    flat = [x for row in m for x in row]          # [1,2,3,4,5,6]
    col_1 = [row[1] for row in m]                 # [2, 5]
    return transposed, flat, col_1


# =============================================================================
# 22. LRU CACHE (design question, 146)
# =============================================================================

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key, value):
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.cap:
            self.data.popitem(last=False)


# =============================================================================
# Self-check: python snippets.py
# =============================================================================

if __name__ == "__main__":
    assert list_basics()[0] == [1, 2, 2, 5, 8, 9]
    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert remove_duplicates_sorted([1, 1, 2, 3, 3]) == 3
    assert rotate_in_place([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert dutch_flag([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]

    assert string_basics() == ("Hello-World", "jello", 2, "c", "eilnst")
    assert is_palindrome("A man, a plan, a canal: Panama")

    hashing_basics()
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4

    assert pair_with_sum_sorted([1, 2, 4, 7, 11], 15) == [2, 4]
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

    assert max_sum_fixed_window([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39
    assert longest_substring_no_repeat("abcabcbb") == 3
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_operations_reduce_x([1, 1, 4, 2, 3], 5) == 2
    assert min_operations_reduce_x([2, 2, 5, 3], 4) == 2
    assert min_operations_reduce_x([1, 1], 3) == -1
    assert min_operations_reduce_x([10, 1, 1, 1, 1, 1], 5) == 5

    assert build_prefix([1, 2, 3]) == [0, 1, 3, 6]
    assert subarray_sum_equals_k([1, -1, 1, 1], 1) == 5

    assert binary_search([1, 3, 5, 7], 5) == 2
    assert lower_bound([1, 3, 3, 7], 3) == 1
    assert bisect_examples()[:3] == (1, 4, 3)
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4

    data = [5, 3, 8, 1, 9, 2, 2]
    for sort_fn in (bubble_sort, insertion_sort, merge_sort, quick_sort, counting_sort):
        assert sort_fn(data) == sorted(data), sort_fn.__name__
    assert quickselect_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

    assert merge_intervals([[1, 3], [8, 10], [2, 6]]) == [[1, 6], [8, 10]]
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert find_missing_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]

    assert stack_queue_basics() == (2, 1)
    assert valid_parentheses("({[]})") and not valid_parentheses("(]")
    assert next_greater([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    assert heap_basics() == (1, 1, 7, (1, "read"), [7, 4], [1, 3])
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert kth_largest_heap([3, 2, 1, 5, 6, 4], 2) == 5
    assert merge_k_sorted_lists([[1, 4], [2, 5], [3]]) == [1, 2, 3, 4, 5]
    mf = MedianFinder()
    for x in [1, 2, 3]:
        mf.add(x)
    assert mf.median() == 2

    assert to_pylist(reverse_list(build_list([1, 2, 3]))) == [3, 2, 1]
    assert middle_node(build_list([1, 2, 3, 4, 5])).val == 3
    assert not has_cycle(build_list([1, 2, 3]))
    assert to_pylist(merge_two_sorted(build_list([1, 3]), build_list([2, 4]))) == [1, 2, 3, 4]
    assert to_pylist(remove_nth_from_end(build_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert to_pylist(delete_value(build_list([6, 1, 6, 2]), 6)) == [1, 2]

    t = build_tree([4, 2, 6, 1, 3, 5, 7])
    assert inorder(t) == inorder_iterative(t) == [1, 2, 3, 4, 5, 6, 7]
    assert preorder(t) == [4, 2, 1, 3, 6, 5, 7]
    assert postorder(t) == [1, 3, 2, 5, 7, 6, 4]
    assert level_order(t) == [[4], [2, 6], [1, 3, 5, 7]]
    assert max_depth(t) == 3 and diameter(t) == 4
    assert is_valid_bst(t)
    assert lowest_common_ancestor(t, 1, 3).val == 2
    t = bst_delete(bst_insert(t, 8), 4)
    assert inorder(t) == [1, 2, 3, 5, 6, 7, 8] and is_valid_bst(t)
    assert inorder(invert_tree(build_tree([2, 1, 3]))) == [3, 2, 1]

    g = build_graph(5, [(0, 1), (0, 2), (1, 3), (3, 4)])
    assert dfs(g, 0) == [0, 1, 3, 4, 2]
    assert bfs_shortest_path(g, 0, 4) == 3
    assert num_islands([["1", "1", "0"], ["0", "0", "0"], ["0", "1", "1"]]) == 2
    assert rotting_oranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert topo_sort(3, [(0, 1), (1, 2)]) == [0, 1, 2]
    assert topo_sort(2, [(0, 1), (1, 0)]) == []
    assert dijkstra(3, [(0, 1, 4), (0, 2, 1), (2, 1, 2)], 0) == [0, 3, 1]
    uf = UnionFind(4)
    uf.union(0, 1)
    uf.union(2, 3)
    assert uf.components == 2 and uf.find(0) == uf.find(1) and not uf.union(1, 0)

    assert len(subsets([1, 2, 3])) == 8
    assert len(permutations([1, 2, 3])) == 6
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]

    assert climb_stairs(5) == 8
    assert house_robber([2, 7, 9, 3, 1]) == 12
    assert coin_change([1, 2, 5], 11) == 3 and coin_change([2], 3) == -1
    assert can_partition([1, 5, 11, 5]) and not can_partition([1, 2, 3, 5])
    assert unique_paths(3, 7) == 28
    assert lcs("abcde", "ace") == 3
    assert edit_distance("horse", "ros") == 3
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert fib_memo(30) == 832040

    assert can_jump([2, 3, 1, 1, 4]) and not can_jump([3, 2, 1, 0, 4])
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") and not trie.search("app") and trie.starts_with("app")

    assert bit_tricks() == (4, True, 3, True, True, 8)

    assert rotate_matrix([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert matrix_tricks() == ([[1, 4], [2, 5], [3, 6]], [1, 2, 3, 4, 5, 6], [2, 5])

    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.get(1)
    lru.put(3, 3)
    assert lru.get(2) == -1 and lru.get(1) == 1

    print("All snippets OK")
