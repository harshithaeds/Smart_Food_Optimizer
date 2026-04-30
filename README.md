# Smart Food & Budget Optimizer Simulation

A Python simulation project that recommends the best food items to purchase within a given budget, using two classical optimization algorithms.

---

## 📄 Report

A full technical report for this project is available here:
**[📄 View Technical Report (PDF)](./SmartFoodOptimizer_Report.pdf)**

The report covers problem formulation, algorithm design, complexity analysis, edge case handling, sample outputs, and conclusions.

---

## 📁 Project Structure

```text
SmartFoodOptimizer/
├── main.py                        # Core logic: data loading, algorithms, output
├── data.txt                       # Food item database
├── SmartFoodOptimizer_Report.docx # Full technical report
└── README.md                      # Project documentation
```

---

## 📝 Description

Each food item in the database has three properties:

- **Name** — the food item label
- **Price** — the cost in currency units
- **Value** — a numeric rating representing how desirable the item is

The simulation reads these items, takes a user-defined budget, and runs two algorithms independently to find the best possible selection. Results are displayed side by side with a comparison summary.

---

## ⚙️ Algorithms Used

### Greedy Algorithm

Sorts all food items by their **value-to-price ratio** in descending order, then greedily selects items that fit within the remaining budget.

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)`
- **Optimality:** Not guaranteed — fast but may miss the globally optimal solution

### Dynamic Programming — 0/1 Knapsack

Builds a 2D table `dp[i][b]` representing the maximum value achievable using the first `i` items with budget `b`. The optimal selection is recovered via backtracking.

- **Time Complexity:** `O(n × budget)`
- **Space Complexity:** `O(n × budget)`
- **Optimality:** Always produces the globally optimal result

---

## 📂 Input Format

The `data.txt` file contains one food item per line:

```text
Name Price Value
```

Example:

```text
Pizza 120 8
Burger 80 6
Fries 50 5
```

Lines with missing fields, non-integer values, or non-positive prices are automatically skipped with a diagnostic message.

---

## ▶️ How To Run

Open PowerShell or Command Prompt and navigate to the project folder:

```powershell
cd C:\Users\sirig\Desktop\coding\SmartFoodOptimizer
```

Run the simulation:

```powershell
python main.py
```

If `python` does not work, try:

```powershell
py main.py
```

---

## 🖥️ Sample Output

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

---

## 🛡️ Edge Cases Handled

| Edge Case | Behaviour |
|---|---|
| Budget is `0` | Both algorithms return empty selections immediately |
| Negative budget | Rejected with a descriptive error message |
| Non-numeric budget input | `ValueError` caught; user is prompted again |
| Empty `data.txt` | Simulation exits gracefully with a notice |
| Invalid lines in `data.txt` | Skipped individually with a line-number warning |
| All items exceed the budget | Both algorithms return empty selections without errors |

---

## 📊 Algorithm Comparison

| Property | Greedy | Dynamic Programming |
|---|---|---|
| Time Complexity | `O(n log n)` | `O(n × budget)` |
| Space Complexity | `O(n)` | `O(n × budget)` |
| Optimal Result | ✗ Not guaranteed | ✓ Always optimal |
| Best Use Case | Fast estimates | Exact solutions |

---

## 🛠️ Requirements

- Python 3.x (no external libraries required)