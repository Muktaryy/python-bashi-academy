# PY-006 — Employee Promotion Checker

## Objective

Create a Python program that determines whether an employee is eligible for a promotion.

## Business Rule

An employee is eligible for promotion if:

- They are at least 25 years old.
- They have worked for the company for at least 2 years.

Both requirements must be satisfied.

## Requirements

- Store the employee's age.
- Store the number of years they have worked at the company.
- Use comparison operators.
- Use the `and` logical operator.
- Use `if` and `else`.
- Display the appropriate promotion status.

## Python Concepts Used

- Variables
- Integers (`int`)
- `if`
- `else`
- Comparison operators
- `>=`
- Logical operator
- `and`
- Boolean expressions
- Indentation
- `print()`

## Logic

The program checks:

```python
age >= 25 and years_at_company >= 2


Both conditions must be True for the employee to be eligible.
Examples
Eligible
age = 30
years_at_company = 4
Output:
Employee is eligible for promotion.
Not Eligible — Not Enough Experience
age = 30
years_at_company = 1
Output:
Employee is not eligible for promotion.
Not Eligible — Too Young
age = 22
years_at_company = 5
Output:
Employee is not eligible for promotion.
Status
Completed ✅
