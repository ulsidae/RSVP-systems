# Earth Science Project

## 📂 About This Archived Project

This repository preserves one of my [high school Earth Science portfolio projects](https://github.com/ulsidae/RSVP-systems/tree/main/%F0%9F%93%9ACase%20Study%3A%20Reviewing%20My%20High%20School%20README/earth-science-portfolio).

The program accepts two sets of user-defined coordinates, overlays them onto a reference image, and visualizes the results using Matplotlib.

It was developed as a simple educational visualization tool for plotting coordinate data during an Earth Science assignment.

Rather than rewriting or removing the original work, I chose to preserve it as an archive and review it from both a product management and software engineering perspective.

---

# 🎯 PM Review

## Problem

While revisiting this repository, I identified several issues with the original README. Although it fulfilled its purpose as a school assignment, it did not provide sufficient context for readers outside its original classroom environment.

## Goal

The goal of this review is to evaluate the original README from a product management perspective and identify opportunities to improve clarity, information architecture, and overall user experience.

The original README is reproduced below.

```md
# earthScience repogitory
for the studies of school, especially earth science

#
This project is my project. So, Pls don't copy or intercept my code -> Don't reupload!
 Nevertheless, If you want to use my code. I hope you contact me,

#
#

#지구과학 레포지토리는
학교 지구과학 포트폴리오 기록용으로 만든 레포지토리입니다.

#
이 프로젝트는 제 프로젝트입니다. 그러니, 제 코드를 복사하거나 자신의 것처럼 속여 재업로드하는 등의 행위는 하지말아주세요,
 그럼에도, 제 코드를 사용해야한다면 먼저 제게 알려주세요.
```

### 1. Inconsistent Language Usage

The README mixed English and Korean without any clear structure.

As a result, readers had to switch between languages throughout the document, increasing cognitive overhead and reducing readability.

---

### 2. Inconsistent Writing Style and Tone

The README included expressions such as:

* "Pls"
* "This project is my project."
* "intercept my code"

These informal and unnatural expressions made the documentation feel less professional and reduced its overall clarity.

---

### 3. Insufficient Project Context

The repository contained only source code.

It did not explain:

* why the project was created,
* what the program actually does,
* how to run it,
* what output it produces,
* or the educational objective behind the implementation.

Although these details were covered in the accompanying school report, anyone visiting the repository independently would have little context.

---

### 4. Lack of Information Hierarchy

The project description, copyright notice, usage notes, and personal comments were presented without any clear organization.

Documentation should be organized into logical sections that enable readers to quickly understand the project and locate relevant information.

---

### 5. Author-Centered Documentation

The README reflected what I wanted to communicate rather than what readers needed to understand.

Good documentation should prioritize the reader's perspective by providing sufficient context, clear organization, and actionable information.

---

# 💻 Technical Review

## Implementation

The program:

* accepts two sets of coordinate points from user input,
* overlays those coordinates onto a reference image,
* connects each set using line segments,
* visualizes the results using Matplotlib.

The implementation demonstrates basic user input handling, coordinate plotting, image overlay, and data visualization using Matplotlib.

## Technical Observations

Reviewing the implementation also revealed several opportunities for improvement.

### 1. Repetitive Input Handling

Each coordinate is collected through manually duplicated input statements.

Today, I would replace these repetitive blocks with iteration to improve maintainability and reduce duplication.

---

### 2. Fixed-Size Data Structure

The implementation assumes exactly five coordinate pairs for each dataset.

A more flexible design would allow an arbitrary number of points by storing them in lists or other dynamic data structures.

---

### 3. Tight Coupling

User input, data processing, and visualization are implemented within a single script.

Separating these responsibilities would improve readability, testing, and future extensibility.

---

### 4. Missing Input Validation

The program assumes that all user input follows the expected format.

Robust input validation and error handling would improve reliability and user experience.

---

### 5. Positive Design Decision

Despite being an early project, the plotting logic was extracted into the `plot_line()` function instead of being duplicated.

Although simple, this demonstrates an early attempt to improve code reuse and readability.

---

## Insights

Reviewing this repository reinforced an important lesson:

> **Documentation is part of the product.**

The same principle applies to code.

Even a small educational project benefits from documentation that explains its purpose and implementation, while the code itself should remain maintainable, reusable, and easy to understand.

Today, I place greater emphasis on:

* designing documentation from the reader's perspective,
* maintaining consistent language throughout a repository,
* providing sufficient project context,
* organizing information with a clear information hierarchy,
* writing maintainable and reusable code,
* separating responsibilities,
* and ensuring repositories remain self-explanatory.

Instead of rewriting or removing this repository, I chose to preserve it as an archive.

It serves as a snapshot of both an early programming project and the evolution of my approach to documentation, software design, and product thinking.
