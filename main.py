from dataclasses import dataclass
from typing import List


@dataclass
class FoodItem:
    name: str
    price: int
    value: int


@dataclass
class SelectionResult:
    selected_items: List[FoodItem]
    total_cost: int
    total_value: int


def read_food_items(file_name: str) -> List[FoodItem]:
    """Read food items from data.txt."""
    items = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                parts = line.strip().split()

                if not parts:
                    continue

                if len(parts) != 3:
                    print(f"Skipping invalid line {line_number}: {line.strip()}")
                    continue

                name, price_text, value_text = parts

                try:
                    price = int(price_text)
                    value = int(value_text)
                except ValueError:
                    print(f"Skipping invalid line {line_number}: {line.strip()}")
                    continue

                if price > 0 and value >= 0:
                    items.append(FoodItem(name, price, value))
                else:
                    print(f"Skipping invalid line {line_number}: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: {file_name} not found.")

    return items


def greedy_selection(items: List[FoodItem], budget: int) -> SelectionResult:
    """
    Greedy simulation:
    Sort items by value/price ratio and select affordable items first.

    Time Complexity: O(n log n)
    """
    selected_items = []
    total_cost = 0
    total_value = 0

    if budget <= 0 or not items:
        return SelectionResult(selected_items, total_cost, total_value)

    sorted_items = sorted(items, key=lambda item: item.value / item.price, reverse=True)

    for item in sorted_items:
        if total_cost + item.price <= budget:
            selected_items.append(item)
            total_cost += item.price
            total_value += item.value

    return SelectionResult(selected_items, total_cost, total_value)


def dp_selection(items: List[FoodItem], budget: int) -> SelectionResult:
    """
    Dynamic Programming simulation using 0/1 Knapsack.

    Time Complexity: O(n * budget)
    Space Complexity: O(n * budget)
    """
    selected_items = []
    total_cost = 0
    total_value = 0
    n = len(items)

    if budget <= 0 or not items:
        return SelectionResult(selected_items, total_cost, total_value)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = items[i - 1]

        for current_budget in range(budget + 1):
            dp[i][current_budget] = dp[i - 1][current_budget]

            if item.price <= current_budget:
                include_value = item.value + dp[i - 1][current_budget - item.price]
                dp[i][current_budget] = max(dp[i][current_budget], include_value)

    remaining_budget = budget

    for i in range(n, 0, -1):
        if dp[i][remaining_budget] != dp[i - 1][remaining_budget]:
            item = items[i - 1]
            selected_items.append(item)
            total_cost += item.price
            total_value += item.value
            remaining_budget -= item.price

    selected_items.reverse()
    return SelectionResult(selected_items, total_cost, total_value)


def print_food_items(items: List[FoodItem]) -> None:
    print("\nAvailable Food Items")
    print("-" * 40)
    print(f"{'Name':<15}{'Price':<10}{'Value':<10}")
    print("-" * 40)

    for item in items:
        print(f"{item.name:<15}{item.price:<10}{item.value:<10}")


def print_result(title: str, result: SelectionResult) -> None:
    print(f"\n{title}")
    print("-" * len(title))

    if result.selected_items:
        item_names = ", ".join(item.name for item in result.selected_items)
    else:
        item_names = "None"

    print(f"Items       : {item_names}")
    print(f"Total Cost  : {result.total_cost}")
    print(f"Total Value : {result.total_value}")


def print_comparison(greedy_result: SelectionResult, dp_result: SelectionResult) -> None:
    print("\nComparison")
    print("-" * 10)

    if dp_result.total_value > greedy_result.total_value:
        print("Dynamic Programming gives a better result than Greedy.")
    elif greedy_result.total_value > dp_result.total_value:
        print("Greedy gives a better result than Dynamic Programming.")
    else:
        print("Both algorithms give the same total value.")

        if dp_result.total_cost < greedy_result.total_cost:
            print("Dynamic Programming reaches that value with lower cost.")
        elif greedy_result.total_cost < dp_result.total_cost:
            print("Greedy reaches that value with lower cost.")


def run_simulation() -> None:
    print("=" * 45)
    print(" Smart Food & Budget Optimizer Simulation")
    print("=" * 45)

    items = read_food_items("data.txt")

    if not items:
        print("No valid food items available.")
        return

    print_food_items(items)

    try:
        budget = int(input("\nEnter your budget: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if budget < 0:
        print("Budget cannot be negative.")
        return

    greedy_result = greedy_selection(items, budget)
    dp_result = dp_selection(items, budget)

    print_result("Greedy Result", greedy_result)
    print_result("Dynamic Programming Result", dp_result)
    print_comparison(greedy_result, dp_result)


if __name__ == "__main__":
    run_simulation()

