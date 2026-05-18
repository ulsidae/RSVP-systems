# 🎯 Wave Function Streams

A probability-based number puzzle inspired by uncertainty, observation, and wave collapse systems.

---

# Concept

While playing Streams in school,
the game was introduced as a simple example of uncertainty.

As the game progressed, one question kept appearing:

```text
Where does this number naturally belong?
```

There was never a perfectly certain answer.

Every number seemed to exist in multiple possible positions at once,
until the player finally made a decision.

That moment strongly resembled the idea of a:

Wave Function

where multiple states coexist until observation collapses them into a single outcome.

This project was created from that feeling.

---

# Core Idea

Each cell is not simply empty.

Every cell contains a probabilistic state:

```js
WaveProbability(number)
```

Example:

```text
Cell 8

1 -> 5%
2 -> 12%
3 -> 37%
4 -> 18%
...
```

Before observation,
all possibilities coexist.

---

# Observation Collapse

When the player places a number:

```text
Observation occurs
```

The probabilistic state collapses into a single confirmed value.

```text
Possibility -> Determined State
```

Example:

```text
Cell 8 = 3
```

Every choice permanently changes the field.

---

# Constraint Propagation

Once a state collapses,
neighboring cells are affected as well.

The system continuously propagates constraints through the grid.

Current rules include:

* minimizing adjacent number difference
* maintaining ascending flows
* favoring consecutive values
* reducing entropy
* stabilizing local structures

A single observation reshapes the entire probability field.

---

# Entropy Field

Every cell contains an entropy value.

High entropy:

* unstable
* unpredictable
* chaotic

Low entropy:

* stable
* structured
* predictable

The system naturally gravitates toward lower entropy configurations.

---

# Human vs Wave Function

The main idea of the project is not competition.

It is comparison.

```text
Human Intuition
vs
Probabilistic Stability
```

Humans choose based on instinct and visual patterns.

The system chooses based on probability propagation and entropy reduction.

Sometimes both agree.

Sometimes they diverge completely.

---

# Product & UX Insights

Observed gameplay revealed an interesting UX dynamic:

When player intuition aligns with the system's probabilistic prediction,
the experience feels stable and satisfying.

When human intuition diverges from probabilistic stability,
the interaction creates tension and uncertainty.

This contrast became one of the core engagement mechanisms of the prototype.

The system also translates mathematical states into simple product-facing metrics:

### Field Entropy

Represents overall board instability and uncertainty progression.

### Wave Sync

Represents how closely player decisions align with probabilistic optimization.

Together, these systems create a lightweight uncertainty-feedback loop focused on pattern recognition and structural stabilization.

---

# Technical Structure

* Single HTML File
* Inline CSS
* Inline JavaScript
* No Frameworks
* Pure Client-Side Logic
* Entropy-Based Probability System
* Wave Collapse Inspired Architecture

---

# Why

The goal was not to create another number game.

The goal was to create a small interactive system where:

```text
observation changes probability
and probability shapes structure
```

A playable uncertainty field.

---

# Limitations

Although the project is inspired by wave functions, uncertainty, and probabilistic collapse systems,
this implementation is still a simplified mathematical abstraction rather than a physically accurate quantum simulation.

Several limitations intentionally remain in the current system.

---

# 1. Not a Real Quantum Simulation

The system does not simulate actual quantum mechanics.

There is:

* no complex-valued wave equation
* no Schrödinger equation
* no true superposition mathematics
* no quantum interference
* no physical measurement model

The term:

```text
Wave Function
```

is used as conceptual inspiration rather than scientific simulation.

The implementation focuses on:

* probabilistic states
* uncertainty
* entropy
* observation collapse
* constraint propagation

rather than real quantum physics.

---

# 2. Heuristic Probability Model

The probability field is generated using handcrafted heuristics.

```js
waveProbability(cell, number)
```

is deterministic logic rather than learned behavior.

The system does not:

* train on player data
* evolve strategies
* perform machine learning
* generate emergent intelligence

Instead, probabilities are constructed from:

* neighboring relationships
* entropy penalties
* sequence flow
* positional weighting

---

# 3. Local Stability vs Global Structure

Earlier versions of the system mainly optimized:

```text
local neighbor stability
```

rather than full-field structural consistency.

Although global flow constraints were later added,
the current implementation still approximates large-scale stabilization using simplified positional weighting.

The field does not yet perform:

* recursive constraint solving
* global state search
* multi-step future prediction
* recursive collapse simulation

As a result, some board states may remain locally stable while globally inconsistent.

---

# 4. Simplified Entropy System

Entropy in this project is symbolic rather than mathematically rigorous.

Current entropy values are:

* manually initialized
* locally reduced after collapse
* numerically simplified

The system does not calculate:

* Shannon entropy
* Bayesian uncertainty fields
* true probability distributions
* recursive entropy minimization

Entropy currently acts as a gameplay stabilization parameter rather than a complete information-theoretic model.

---

# 5. Constraint Propagation Scope

The current propagation model only affects:

* neighboring cells
* positional tendencies
* sequence resonance

A true Wave Function Collapse architecture would recursively propagate constraints across the entire field until equilibrium is reached.

This implementation instead uses:

* lightweight local updates
* simplified propagation rules
* immediate recalculation

to preserve responsiveness inside a single zero-dependency HTML file.

---

# 6. Streams Inspiration vs Original Rules

The project is inspired by the uncertainty and placement tension experienced while playing Streams.

However, this system is not a recreation of the original game.

Several mechanics differ intentionally:

* entropy systems
* wave probability scoring
* collapse synchronization
* positional weighting
* probabilistic visualization

The goal was not rule accuracy,
but the creation of an uncertainty-driven mathematical puzzle field.

---

# 7. Human Intuition Cannot Be Fully Modeled

One of the central ideas of the project is the comparison between:

```text
Human Intuition
vs
Probabilistic Stability
```

However, human decision-making contains:

* pattern bias
* aesthetic preference
* risk perception
* emotional reasoning
* future anticipation

that are difficult to formalize mathematically.

The system therefore represents only a partial approximation of strategic intuition.

---

# 8. Designed as a Conceptual Prototype

This project was intentionally built as:

* a conceptual prototype
* a mathematical toy system
* a probability visualization experiment

rather than a commercially balanced puzzle game.

The architecture prioritizes:

* interpretability
* visibility of logic
* probabilistic structure
* readable collapse mechanics

over competitive balance or large-scale optimization.

---

# Future Directions

Possible future extensions include:

* recursive wave propagation
* recursive collapse chains
* adaptive probability balancing
* probability heatmap visualization
* player behavior analysis
* entropy balancing experiments
* procedural field generation
* multi-layer uncertainty systems

The current implementation represents only the first observable layer of the system.
