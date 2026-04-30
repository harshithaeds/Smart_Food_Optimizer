# 🍔 Smart Food & Budget Optimizer

A Python-based simulation that helps users select the best combination of food items within a given budget using optimization algorithms.

---

## 📖 Project Overview

This project solves a real-world **budget optimization problem** using:

- Greedy Algorithm  
- Dynamic Programming (0/1 Knapsack)  

Each food item has:
- Price (cost)  
- Value rating (benefit)  

The goal is to **maximize value within a limited budget**.

---

## 🎯 Objective

- Compare Greedy vs Dynamic Programming  
- Demonstrate real-world application of algorithms  
- Provide optimal and approximate solutions  

---

## 🧠 Algorithms Used

### 🔹 Greedy Algorithm
- Selects items based on **value/price ratio**  
- Time Complexity: `O(n log n)`  
- Fast but **not always optimal**  

### 🔹 Dynamic Programming (0/1 Knapsack)
- Guarantees **optimal solution**  
- Time Complexity: `O(n × B)`  
- Uses DP table approach  

---

## 📂 Project Structure
SmartFoodOptimizer/
├── main.py
├── data.txt
└── README.md

---

## 📊 Sample Input
Pizza 120 8
Burger 80 6
Fries 50 5

---

## ▶️ How to Run

```bash
cd SmartFoodOptimizer
python main.py
 
📈 Sample Output

Budget = 160

Algorithm	Items Selected	        Cost	Value
Greedy	     Fries, Salad, Coffee	 150	  13
DP	         Burger, Fries, Coffee	 160	  13

⚖️ Comparison
Feature	      Greedy	Dynamic Programming
Speed	        Fast	      Slower
Optimal	       ❌ No	        ✅ Yes

⚠️ Edge Cases Handled
Budget = 0
Negative input
Invalid data
Empty dataset
All items exceed budget

🏁 Conclusion
Dynamic Programming gives optimal results
Greedy provides fast approximation
Both are useful depending on the scenario

🚀 Future Enhancements
GUI (Tkinter / Web)
Database integration
Real-time recommendations
Multiple quantity support

📄 Detailed Report

Full project report available here:
[View Report](./SmartFoodOptimizer_Report.docx)

