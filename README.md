# Smart Food & Budget Optimizer Simulation

## Description

This is a Python simulation project that suggests the best food items a user can buy within a given budget.

Each food item has:

- Name
- Price
- Value rating

The simulation compares two algorithms:

- Greedy Algorithm
- Dynamic Programming using 0/1 Knapsack

## Project Structure

```text
SmartFoodOptimizer/
├── main.py
├── data.txt
└── README.md
```

## Algorithms Used

### Greedy Algorithm

The greedy algorithm sorts food items by value-to-price ratio in descending order. It selects the best ratio items first until the budget is exhausted.

Time Complexity: `O(n log n)`

This approach is fast, but it does not always guarantee the best possible result.

### Dynamic Programming

The dynamic programming approach uses the 0/1 Knapsack method. It builds a 2D table to find the maximum possible value within the budget.

Time Complexity: `O(n * budget)`

Space Complexity: `O(n * budget)`

This approach gives the optimal result.

## Input Format

The `data.txt` file contains one food item per line:

```text
name price value
```

Example:

```text
Pizza 120 8
Burger 80 6
Fries 50 5
```

## How To Run

Open PowerShell or Command Prompt in the project folder:

```powershell
cd C:\Users\sirig\Desktop\coding\SmartFoodOptimizer
```

Run:

```powershell
python main.py
```

If `python` does not work, try:

```powershell
py main.py
```

## Sample Output

```text
=============================================
 Smart Food & Budget Optimizer Simulation
=============================================

Available Food Items
----------------------------------------
Name           Price     Value
----------------------------------------
Pizza          120       8
Burger         80        6
Fries          50        5
Pasta          100       7
Sandwich       60        4
Juice          40        3
Salad          70        6
Tacos          90        7
Noodles        110       8
Coffee         30        2

Enter your budget: 160

Greedy Result
-------------
Items       : Fries, Salad, Coffee
Total Cost  : 150
Total Value : 13

Dynamic Programming Result
--------------------------
Items       : Burger, Fries, Coffee
Total Cost  : 160
Total Value : 13

Comparison
----------
Both algorithms give the same total value.
Greedy reaches that value with lower cost.
```

## Edge Cases Handled

- Budget is `0`
- Negative budget
- Invalid budget input
- Empty `data.txt`
- Invalid lines in `data.txt`
- All items exceed the budget
