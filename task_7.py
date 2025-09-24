import random
import matplotlib.pyplot as plt

def monte_carlo_dice(n_simulations):
    # Створюємо словник для підрахунку сум від 2 до 12
    sums_count = {i: 0 for i in range(2, 13)}

    # Симуляція n_simulations кидків
    for _ in range(n_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums_count[total] += 1

    # Обчислюємо ймовірності
    sums_prob = {s: count / n_simulations for s, count in sums_count.items()}
    return sums_count, sums_prob

def plot_probabilities(sums_prob):
    sums = list(sums_prob.keys())
    probs = [sums_prob[s] for s in sums]

    plt.bar(sums, probs, color='skyblue')
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків (метод Монте-Карло)")
    plt.xticks(sums)
    plt.show()

def main():
    n_simulations = 100000  # кількість кидків
    counts, probs = monte_carlo_dice(n_simulations)

    print("Сума : Кількість : Ймовірність")
    for s in range(2, 13):
        print(f"{s} : {counts[s]} : {probs[s]:.4f}")

    plot_probabilities(probs)

if __name__ == "__main__":
    main()
