import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    # Вузол дерева
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#330033"  # початковий темний фіолетовий
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    # Додає вузли та ребра у граф
    if node is not None:
        graph.add_node(node.id, label=str(node.val), color=node.color)
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

def draw_tree(root):
    # Візуалізація дерева з підписами та кольорами
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8,5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500,
            node_color=colors, font_color='white', font_size=12)
    plt.show()

def generate_purple_colors(n):
    # Генеруємо n кольорів від темного до світлого фіолетового
    colors = []
    for i in range(n):
        val = int(51 + (204 * i) / max(n-1, 1))  # 51 → 255
        hex_val = hex(val)[2:].zfill(2)
        colors.append(f"#{hex_val}00{hex_val}")  # фіолетовий від темного до світлого
    return colors

def dfs(root):
    # Обхід в глибину (стек)
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order

def bfs(root):
    # Обхід в ширину (черга)
    queue = deque([root])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order

def visualize_traversal(root, traversal_type="DFS"):
    # Вибір обходу та кольори вузлів
    if traversal_type == "DFS":
        order = dfs(root)
    else:
        order = bfs(root)
    colors = generate_purple_colors(len(order))
    for node, color in zip(order, colors):
        node.color = color
    draw_tree(root)

# Приклад дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходів
print("DFS:")
visualize_traversal(root, traversal_type="DFS")
print("BFS:")
visualize_traversal(root, traversal_type="BFS")
