# PY-007 — Employee Performance Rating

## Objective

Create a Python program that classifies an employee's performance based on their performance score.

The score is between `0` and `100`.

## Business Rules

| Score | Performance Rating |
|-------|--------------------|
| 90–100 | Excellent |
| 75–89 | Good |
| 60–74 | Satisfactory |
| Below 60 | Needs Improvement |

## Requirements

- Store the employee's performance score in a variable.
- Check the score using conditional statements.
- Use `if`.
- Use `elif`.
- Use `else`.
- Display the appropriate performance rating.

## Python Concepts Used

- Variables
- Integers (`int`)
- `if`
- `elif`
- `else`
- Comparison operators
- `>=`
- Conditions
- Boolean expressions
- Indentation
- `print()`

## Logic

The program checks the conditions from top to bottom.

```python
if score >= 90:
    ...
elif score >= 75:
    ...
elif score >= 60:
    ...
else:
    ...

Python stops at the first condition that is True.
Example
For:
score = 85
The program checks:
85 >= 90 → False
85 >= 75 → True
Therefore, the output is:
Performance Rating: Good
Examples
Excellent
score = 95
Output:
Performance Rating: Excellent
Good
score = 85
Output:
Performance Rating: Good
Satisfactory
score = 65
Output:
Performance Rating: Satisfactory
Needs Improvement
score = 50
Output:
Performance Rating: Needs Improvement
Status
Completed ✅
