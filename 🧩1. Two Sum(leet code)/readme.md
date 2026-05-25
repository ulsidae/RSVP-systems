# 🧩1. Two Sum(leetcode)

- **Language:** C++
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)
- **Difficulty:** Easy
- **Topic:** Array, Hash Table

---

## 1. 📌 Problem (What needed to be solved)

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

### ⚠️ Constraints & Core Challenges
- Exactly one valid solution exists
- The same element cannot be used twice
- A brute-force approach using nested loops would take O(N²) time, which becomes inefficient as the input size grows

The goal is to reduce lookup time by using a hash table.

---

## 2. 💡 Approach (How I approached it)

### One-pass Hash Table Strategy

Instead of comparing every possible pair, this solution uses an `unordered_map` to store previously visited values while traversing the array.

For each element:

1. **Calculate the Complement**

```text
diff = target - nums[i]
```

### 2. Hash Map Lookup
- Check whether the complement already exists in the hash map
- If it exists, return the stored index and the current index
- If it does not exist, store the current value and continue

### 3. Single Pass Traversal
- The array is traversed exactly once
- This reduces the overall time complexity from O(N²) to O(N)

---

## 3. 💻 Implementation (How it was built)

```cpp
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];

            // Check whether the complement already exists
            if (seen.find(diff) != seen.end()) {
                return {seen[diff], i};
            }

            // Store current value and index
            seen[nums[i]] = i;
        }

        return {};
    }
};
```

## 4. 🚀 Insights (What I learned or improved afterward)

### ⚡ Why the Order Matters

The lookup operation must happen before inserting the current value into the hash map.

```cpp
if (seen.find(diff) != seen.end())
```

must come before:

```cpp
seen[nums[i]] = i;
```

Otherwise, a value could incorrectly match with itself.

For example:

```text
nums = [3, 4]
target = 6
```

If `3` is inserted before the lookup step, it could immediately match with itself and produce an invalid result.

The correct sequence is:

1. Check for the complement
2. Store the current value

This guarantees that only previously visited elements are considered.

---

### 📊 Complexity Analysis

#### Time Complexity: O(N)

- The array is traversed once
- Hash table lookup and insertion take O(1) on average

#### Space Complexity: O(N)

- In the worst case, the hash map stores up to N elements

---

## 5. 🔍 What Improved After Refactoring

Compared to the initial implementation, the final version was refined for readability, portability, and maintainability:

- **Portability:** Added explicit standard headers (`<vector>`, `<unordered_map>`) for independent compilation
- **Type Safety:** Used fully defined template types (`vector<int>`) instead of incomplete declarations
- **Readability:** Improved comments and explanation flow for easier understanding
- **Maintainability:** Refined the overall structure to make the implementation cleaner and easier to follow

The final version focuses not only on correctness, but also on writing code that is easier to understand and maintain.