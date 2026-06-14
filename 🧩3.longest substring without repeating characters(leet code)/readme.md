# 🧩3. longest substring without repeating characters(leet code)

- **Language:** Python
- **Time Complexity:** O(N)
- **Difficulty:** Medium
- **Topic:** Sliding Window, Hash Table

---

## 1. 📌 Problem (What needed to be solved)

Given a string `s`, return the length of the longest substring without repeating characters.

A substring must consist of consecutive characters. Any repeated character invalidates the current window.


### ⚠️  Key constraints

- Repeated substring construction must be avoided

- Efficient duplicate tracking is required while scanning once

---

## 2. 💡 Approach

### Initial intuition (RLE-inspired)

I initially approached the problem with a run-length encoding style idea:

> If a duplicate character appears, the current segment becomes invalid, so we restart a new segment.

This led to a segmented view: ```abc | abc```
From this perspective, the string was treated as a series of independent valid blocks.


### Limitation of this approach

Unlike RLE, repeated characters are not confined to independent segments.
Characters can reappear across overlapping windows, meaning a full reset loses useful context.
This made the segmentation approach inefficient and incorrect.

### 🚀  Key insight (Sliding window)

The correct interpretation is not segmentation, but a moving window over a single pass.
The key observation:
> Only the left boundary of the current valid window needs to change when a duplicate appears.
Instead of rebuilding substrings, we maintain a dynamic range.

```
abc | abc   → invalid segmentation view
```

becomes:
```
continuous scan with moving left boundary
```

This reduces the problem to boundary updates only.

---

## 3. 💻 Implementation

A hash map stores the last seen index of each character.

```python

char_map = {}

start = 0

max_len = 0

```

### Single-pass scan

```python

for end, char in enumerate(s):

    if char in char_map and char_map[char] >= start:

        start = char_map[char] + 1



    char_map[char] = end

    max_len = max(max_len, end - start + 1)

```

### Core idea

* `char_map` tracks the most recent index of each character

* `start` defines the left boundary of the valid window

* `end` expands the window one character at a time

---

## 4. 🚀 Insights



This problem is fundamentally about maintaining a valid range, not splitting a string.
A hash map combined with a sliding window allows constant-time duplicate handling during a single pass.

### Key takeaway

> Maintaining boundaries is more efficient than reconstructing structure.

---

## 5. 🔍 What improved after refactoring

### Before

* Segmentation-based thinking

* Repeated substring reconstruction

* Implicit reset logic



### After

* Sliding window with hash map

* Single-pass traversal

* O(1) boundary updates per step

---

## Final takeaway

This problem demonstrates how an initial segmentation-based intuition can evolve into a streaming model. Replacing reconstruction with boundary control reduces both complexity and cognitive overhead.
