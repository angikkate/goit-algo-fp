import heapq

def dijkstra(graph, start):
    # Алгоритм Дейкстри з використанням бінарної купи
    
    distances = {v: float('inf') for v in graph}  # Ініціалізація відстаней
    distances[start] = 0  # Відстань до стартової вершини = 0
    heap = [(0, start)]  # Бінарна купа (поточна відстань, вершина)

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)  # Вибір вершини з мінімальною відстанню

        if current_dist > distances[current_vertex]:
            continue  # Якщо відстань більша за вже знайдену, пропускаємо

        for neighbor, weight in graph[current_vertex]:  # Переглядаємо сусідів
            distance = current_dist + weight
            if distance < distances[neighbor]:  # Якщо знайшли коротший шлях
                distances[neighbor] = distance  # Оновлюємо відстань
                heapq.heappush(heap, (distance, neighbor))  # Додаємо у купу

    return distances  # Повертаємо найкоротші відстані

def create_graph():
    # Створення графа у вигляді словника суміжностей
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2), ("Z", 6)],
        "E": [("C", 10), ("D", 2), ("Z", 3)],
        "Z": [("D", 6), ("E", 3)]
    }
    return graph

def main():
    graph = create_graph()  # Створюємо граф
    start_vertex = "A"  # Стартова вершина
    shortest_paths = dijkstra(graph, start_vertex)  # Виконуємо алгоритм Дейкстри

    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for i, (vertex, dist) in enumerate(sorted(shortest_paths.items()), 1):
        print(f"{i}. Вершина {vertex} — відстань {dist}")  # Вивід результатів

if __name__ == "__main__":
    main()  # Запуск основної функції
