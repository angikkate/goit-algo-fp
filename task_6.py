items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Вибираємо страви по співвідношенню калорії/вартість
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)
    selected = []
    total_cost = 0
    total_calories = 0
    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]
    return selected, total_calories, total_cost

def dynamic_programming(items, budget):
    # Алгоритм динамічного програмування (задача про рюкзак)
    n = len(items)
    item_list = list(items.items())
    dp = [[0]*(budget+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        name, info = item_list[i-1]
        cost = info["cost"]
        cal = info["calories"]
        for w in range(budget+1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + cal)
            else:
                dp[i][w] = dp[i-1][w]
    
    # Відновлення вибраних страв
    w = budget
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name, info = item_list[i-1]
            selected.append(name)
            w -= info["cost"]
    
    selected.reverse()
    total_cost = sum(items[name]["cost"] for name in selected)
    total_calories = sum(items[name]["calories"] for name in selected)
    return selected, total_calories, total_cost

# Приклад використання
budget = 100

print("Жадібний алгоритм:")
sel, cal, cost = greedy_algorithm(items, budget)
print("Страви:", sel, "\nКалорії:", cal, "\nВартість:", cost)

print("\nДинамічне програмування:")
sel, cal, cost = dynamic_programming(items, budget)
print("Страви:", sel, "\nКалорії:", cal, "\nВартість:", cost)
