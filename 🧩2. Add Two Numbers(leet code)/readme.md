# 🧩2. Add Two Numbers(leet code)

- **Language:** Python
- **Time Complexity:** O(max(N,M))
- **Difficulty:** Medium
- **Topic:** Linked List, Recursion
---

> [!NOTE]
> This write-up was created as an experiment in AI-assisted development workflows.
>
> After completing the implementation of the problem, I used an AI model to help structure and formalize the explanation based on my solution and understanding.
>
> The final structure, organization, and presentation were handled by me, and the content was reviewed and adjusted to ensure technical correctness and clarity.

## 1. 📌 Problem (What needed to be solved)

Two non-empty linked lists represent two non-negative integers in reverse order.
Each node contains a single digit.

The task is to add these two numbers and return the result as a linked list in the same reverse order format.

### ⚠️ Constraints & Core Challenges

- Each node contains a single digit (0–9)
- Numbers are stored in reverse order
- Lists may have different lengths
- Carry propagation must be handled across digits
- Processing must continue until both lists and carry are fully exhausted

The main challenge is implementing digit-wise addition without converting the linked lists into integers.

---

## 2. 💡 Approach (How I approached it)

Initially, I solved the problem using an iterative approach that simulates manual addition with a carry variable.

Later, I refactored the solution into a recursive version to improve structural clarity and to better express the problem as a state-based digit transition.

### 🔄 Refactored Approach (Iterative → Recursive)

The original iterative solution:

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = n = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            n.next = ListNode(carry % 10)
            n = n.next
            carry //= 10
            
        return root.next
```

was refactored into a recursive implementation:

```python
class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
        if not l1 and not l2 and not carry:
            return None

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry

        node = ListNode(total % 10)

        next_l1 = l1.next if l1 else None
        next_l2 = l2.next if l2 else None

        node.next = self.addTwoNumbers(next_l1, next_l2, total // 10)

        return node
```

---

## 3. 💻 Implementation (How it was built)

The final implementation uses recursion to perform digit-by-digit addition while passing the carry as a function parameter.

Each recursive call processes one digit and delegates the next step to the following call.

---

## 4. 🚀 Insights (What I learned or improved afterward)

I realized that the problem can be modeled as a digit stream processing system, rather than a direct numeric conversion problem.

-Carry handling can be naturally expressed through function parameters in recursion
-Recursive structure removes explicit loop control and improves conceptual clarity
-Each function call represents a single step of manual addition

---

### 📊 Complexity Analysis

- Time Complexity: O(max(N, M))
- Each node is visited exactly once during traversal

---

## 5. 🔍 What Improved After Refactoring

- Improved abstraction by replacing iterative loop control with recursive state transitions
- Simplified logic by removing explicit pointer manipulation
- Enhanced readability by expressing each computation step as a single recursive call
- Strengthened understanding of linked list traversal as a sequential data stream
- Shifted perspective from “number addition” to “structured data flow processing”
