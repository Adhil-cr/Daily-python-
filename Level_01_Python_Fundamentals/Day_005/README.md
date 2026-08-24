# Day 005 — for Loops & Iteration

## 🎯 Main Topics

- `for` loops
- `range()`
- `range(start, stop, step)`
- Iterating over strings
- Iterating over sequences
- `break` and `continue` with `for`
- Accumulator and counter patterns
- Running maximum and minimum
- State management across iterations
- `for` vs `while`
- Introduction to nested loops

## 🧠 Learning Objectives

By the end of Day 005, I should be able to:

- Write a `for` loop confidently.
- Use `range()` with start, stop, and step values.
- Iterate through strings and sequences.
- Use counters and accumulators.
- Maintain state while processing multiple values.
- Find maximum/minimum values without `max()` or `min()`.
- Decide when a `for` loop is more appropriate than a `while` loop.
- Handle basic edge cases when designing iterative algorithms.

## 💻 Problems Completed

1. **Print Even Numbers** — Used `range()` with a step of `2`.
2. **Count Vowels** — Iterated through a string and counted vowels.
3. **Multiplication Table** — Used `for` and `range()` for repeated calculations.
4. **Find the Largest Number** — Practiced running maximum and state management.
5. **Number Classification** — Used conditions and multiple counters.

## 🛠️ Mini Task

### Student Marks Analyzer

Built a CLI program that analyzes student marks and calculates:

- Number of students
- Highest mark
- Lowest mark
- Average mark
- Passed students
- Failed students

The task combined loops, validation, counters, accumulators, and running maximum/minimum logic.

## ⭐ Mentor's Challenge

For Problem 04 and the Mini Task, the main focus was identifying:

> **What state does the program need to remember while the loop is running?**

This introduced an important algorithmic concept: variables can preserve information from previous iterations and update that state as new input is processed.

## 📌 Key Lesson

A loop is not just about repeating code.

A useful mental model is:

```text
Input / Iterable
      ↓
Process one item
      ↓
Update state
      ↓
Process next item
      ↓
...
```

Understanding **state across iterations** is an important foundation for algorithms and data processing.

## 📂 Files

```text
Day_005/
├── README.md
├── notes.md
├── resources.md
├── practice.py
├── problem_01.py
├── problem_02.py
├── problem_03.py
├── problem_04.py
├── problem_05.py
└── mini_task.py
```

## 📈 Status

- Knowledge Check: ✅ 8/8
- Coding Problems: ✅ 5/5
- Mini Task: ✅
- Mentor's Challenge: ✅
- Code Review: ✅
