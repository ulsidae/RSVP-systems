# 🧩 7-Day Intensive Log: Exploring Algorithmic Efficiency

> **About this Log**  
> A 7-day study log documenting how I explored algorithmic efficiency through experimentation, code restructuring, and mathematical reinterpretation.

> Throughout this process, I focused on reducing unnecessary operations, simplifying implementations, and analyzing common algorithmic patterns from a more structural perspective.

**Most notes and experiments were originally written in Korean.**
**Some pages also contain rough exploratory notes written during the process of analyzing implementation trade-offs and runtime behavior.**

---

## ⚡ Day 0: Pragmatic Simplification

While studying examples from an algorithm textbook, I noticed that several implementations were intentionally written inefficiently to demonstrate time complexity concepts.

To better understand the trade-offs involved, I restructured parts of the code with a stronger emphasis on practical efficiency and cleaner execution flow.

### Reducing Unnecessary Runtime Operations
<img src="https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%A7%A90.%207-Day%20Intensive%20Log%3A%20Exploring%20Algorithmic%20Efficiency/img/0_1.jpg" height="400"/>

---

### Reducing Overall Code Length
<img src="https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%A7%A90.%207-Day%20Intensive%20Log%3A%20Exploring%20Algorithmic%20Efficiency/img/0_2.jpg" height="600"/>

---

---

## 🚀 Day 1: Execution Speed & Native Optimization

Beyond shortening code, I began focusing more directly on execution speed and reducing unnecessary processing overhead.

I experimented with faster I/O handling, built-in Python functions, and more compact implementations.

### Minimizing Code While Improving Speed
<img src="https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%A7%A90.%207-Day%20Intensive%20Log%3A%20Exploring%20Algorithmic%20Efficiency/img/1_0.jpg" height="600"/>

---

### Applying Earlier Optimization Ideas to Mathematical Calculations
<img src="https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%A7%A90.%207-Day%20Intensive%20Log%3A%20Exploring%20Algorithmic%20Efficiency/img/1_1.jpg" height="600"/>

---

---

## 📈 Days 2 & 3: Prefix Sums & $\Sigma$ Notation

I focused mainly on prefix sums and range sum queries.

Rather than treating prefix sums as just another implementation technique, I began interpreting them as a programmatic representation of mathematical sigma notation ($\Sigma$).

This perspective helped me think about accumulation logic more structurally instead of treating it as a memorized pattern.

### Initial Notes About the $\Sigma$ Concept
<img src="https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%A7%A90.%207-Day%20Intensive%20Log%3A%20Exploring%20Algorithmic%20Efficiency/img/2_0.jpg" height="540"/>

---

### Implementing Prefix Sums Using Temporary Accumulator Variables
<img src="https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%A7%A90.%207-Day%20Intensive%20Log%3A%20Exploring%20Algorithmic%20Efficiency/img/2_1.jpg" height="800"/>

---

### Exploring Prefix Sum Construction with Python's `accumulate`
<img src="https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%A7%A90.%207-Day%20Intensive%20Log%3A%20Exploring%20Algorithmic%20Efficiency/img/2_2.jpg" height="800"/>

---

---

## 🗺️ Day 4: Multi-Dimensional Spaces & Double $\Sigma$

I extended the prefix sum concept into two-dimensional space.

During this process, I began thinking of 2D prefix sums as a programmatic equivalent of double sigma notation. Using this interpretation, I experimented with several approaches for implementing 2D range sum calculations.

### Exploring Properties of Double $\Sigma$ Based on Earlier Notes
<img src="https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%A7%A90.%207-Day%20Intensive%20Log%3A%20Exploring%20Algorithmic%20Efficiency/img/3_1.jpg" height="540"/>

---

### Implementing 2D Range Sum Logic with Double $\Sigma$ Concepts
<img src="https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%A7%A90.%207-Day%20Intensive%20Log%3A%20Exploring%20Algorithmic%20Efficiency/img/3_0.jpg" height="800"/>

---

---

## ⚖️ Days 5–7: Discrete Mathematics & Pragmatic Trade-offs

Before finishing this log, I spent additional time studying discrete mathematics to better understand optimization trade-offs and algorithmic constraints.

This changed how I think about "optimal" solutions in practical environments.

### Sometimes Simpler Code Is Enough
<img src="https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%A7%A90.%207-Day%20Intensive%20Log%3A%20Exploring%20Algorithmic%20Efficiency/img/4_0.jpg" height="540"/>

---

### Simpler Approaches Also Have Clear Limitations
<img src="https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%A7%A90.%207-Day%20Intensive%20Log%3A%20Exploring%20Algorithmic%20Efficiency/img/4_1.jpg" height="800"/>

---

## 🎯 Final Thoughts

Through this short study process, I realized that optimization is not always about forcing the mathematically fastest solution. In many situations, the better engineering decision is choosing a simpler and more maintainable implementation that still satisfies the actual constraints of the environment.

This experience also changed how I approach algorithmic problem solving itself — not simply as finding correct answers, but as understanding the structure, constraints, and trade-offs behind an implementation.
