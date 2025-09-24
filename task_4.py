import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    # Вузол дерева
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # унікальний id

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    # Додає вузли та ребра у граф
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    # Візуалізація дерева
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color="skyblue")
    plt.show()

def heapify(arr, n, i):
    # Перетворення піддерева на max-heap
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_heap(arr):
    # Побудова max-heap
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def array_to_heap_tree(arr):
    # Перетворення масиву купи на дерево
    build_heap(arr)
    nodes = [Node(arr[i]) for i in range(len(arr))]
    n = len(arr)
    for i in range(n // 2):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]  # повертаємо корінь

def visualize_heap(arr):
    # Функція для побудови та візуалізації купи
    root = array_to_heap_tree(arr)
    draw_tree(root)

# Приклад використання
heap_array = [4, 10, 3, 5, 1]
visualize_heap(heap_array)
