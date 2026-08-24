# Day 005 — Notes

## 1. `for` Loop

A `for` loop iterates over the items of an iterable.

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

### Mental Model

```text
Take one item
    ↓
Process it
    ↓
Take the next item
    ↓
Continue until the iterable is exhausted
```

---

## 2. `range()`

`range()` generates a sequence of numbers.

### `range(stop)`

```python
range(5)
```

Produces:

```text
0 1 2 3 4
```

The stop value is excluded.

### `range(start, stop)`

```python
range(1, 5)
```

Produces:

```text
1 2 3 4
```

### `range(start, stop, step)`

```python
range(1, 10, 2)
```

Produces:

```text
1 3 5 7 9
```

### Counting backwards

```python
range(5, 0, -1)
```

Produces:

```text
5 4 3 2 1
```

### Important Rule

```text
range(start, stop, step)
      ↑       ↑      ↑
   included excluded change
```

The `step` determines the amount and direction of change.

---

## 3. Iterating Over Strings

Strings are iterable.

```python
text = "Python"

for character in text:
    print(character)
```

Output:

```text
P
y
t
h
o
n
```

This is useful for:

- Character counting
- Validation
- Searching
- Text processing

---

## 4. Iterating Over Sequences

A `for` loop can process items in a sequence.

```python
languages = ["Python", "Java", "C"]

for language in languages:
    print(language)
```

Lists and other collections will be studied more deeply later.

---

## 5. `for` vs `while`

### `for`

Use `for` naturally when processing each item in a sequence or a known range.

```python
for number in range(1, 11):
    print(number)
```

### `while`

Use `while` when repetition depends primarily on a condition.

```python
while password != correct_password:
    password = input("Password: ")
```

The distinction is about the structure of the problem, not a strict rule.

---

## 6. Accumulator Pattern

An accumulator stores a value that grows as the loop runs.

```python
total = 0

for number in range(1, 6):
    total += number

print(total)
```

Output:

```text
15
```

General pattern:

```python
total = initial_value

for value in values:
    total += value
```

Common uses:

- Sum
- Total marks
- Total price
- Total distance
- Counts

---

## 7. Counter Pattern

A counter tracks how many times something happens.

```python
count = 0

for number in range(1, 11):
    if number % 2 == 0:
        count += 1
```

The counter changes only when the required condition is satisfied.

---

## 8. Running Maximum

A running maximum stores the largest value seen so far.

### Important

Do not always do this:

```python
largest = 0
```

because it fails if all valid inputs are negative.

Instead, initialize the maximum from the first actual value.

Conceptually:

```text
Read first value
      ↓
largest = first value
      ↓
Read next value
      ↓
Is it larger?
      ↓
Yes → update largest
No  → keep largest
```

This pattern is used frequently in algorithms.

---

## 9. Running Minimum

The same idea works for minimum values.

```text
Read first value
      ↓
lowest = first value
      ↓
Read next value
      ↓
Is it smaller?
      ↓
Yes → update lowest
No  → keep lowest
```

---

## 10. State Across Iterations

One of the most important concepts from Day 005 is **state**.

For example, a marks analyzer may maintain:

```text
total_marks
highest_score
lowest_score
passed_students
failed_students
```

After each student, these values represent everything the program needs to remember from previous iterations.

This concept becomes increasingly important in:

- Algorithms
- Data processing
- File processing
- APIs
- Databases
- Backend development

---

## 11. `break`

`break` immediately terminates the loop.

```python
for number in range(1, 10):
    if number == 5:
        break

    print(number)
```

Output:

```text
1
2
3
4
```

---

## 12. `continue`

`continue` skips the rest of the current iteration and moves to the next one.

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

---

## 13. Nested Loops

A loop inside another loop is a nested loop.

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row, column)
```

Nested loops are useful for:

- Grids
- Tables
- Patterns
- Matrix operations
- Combinations

They can also increase algorithmic complexity, so they should be used intentionally.

---

## 14. Common Mistakes

### Mistake 1 — Forgetting that stop is excluded

```python
range(1, 5)
```

does not include `5`.

### Mistake 2 — Wrong step direction

```python
range(5, 1)
```

does not count backwards.

Use:

```python
range(5, 0, -1)
```

### Mistake 3 — Incorrect initial maximum/minimum

Avoid arbitrary initial values when the input range is unknown.

### Mistake 4 — Adding restrictions not required by the specification

If a problem says the input must be an integer, do not automatically reject negative integers unless the requirements say so.

### Mistake 5 — Overcomplicating iteration

Prefer the simplest loop structure that clearly expresses the algorithm.

---

## 15. Professional Algorithm Thinking

Before writing code, ask:

1. What input do I have?
2. What needs to be repeated?
3. What state must I remember?
4. How does that state change?
5. When does the loop stop?
6. What edge cases can break my assumptions?

This is more important than memorizing syntax.

---

## Day 005 Takeaway

The key progression is:

```text
for loop
   ↓
range()
   ↓
iteration
   ↓
counter / accumulator
   ↓
state
   ↓
running maximum / minimum
   ↓
algorithmic thinking
```
