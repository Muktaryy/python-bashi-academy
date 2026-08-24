# PY-004 — Employee Access Checker

## Objective

Create a Python program that determines an employee's access level based on their active status and admin status.

## Business Rules

| Active | Admin | Access |
|--------|-------|--------|
| `True` | `True` | Full Admin Access |
| `True` | `False` | Employee Access |
| `False` | `True` | Access Denied |
| `False` | `False` | Access Denied |

## Requirements

- Store the employee's active status.
- Store the employee's admin status.
- Use `if`.
- Use `elif`.
- Use `else`.
- Use logical operators.
- Display the appropriate access level.

## Python Concepts Used

- Variables
- Boolean (`bool`)
- `if`
- `elif`
- `else`
- `and`
- `not`
- Conditions
- Logical operators
- Indentation
- `print()`

## Example

When:

```python
is_active = True
is_admin = True
