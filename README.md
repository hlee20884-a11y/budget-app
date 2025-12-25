# Build a Budget App

A simple Python budget app that tracks spending in different categories and displays the relative spending percentage on a graph.

## Features
- Add spending in different categories
- View total spending and spending per category
- Display a visual representation (graph) of relative spending
- Easily track and manage your budget

## Example Usage
```python
# Example of adding expenses
budget = Budget()
budget.add_expense("Food", 50)
budget.add_expense("Entertainment", 30)
budget.add_expense("Transport", 20)

# View total spending
print(budget.total_expenses())

# View spending per category
print(budget.expenses_by_category())

# Display a graph of relative spending
budget.plot_expenses()
