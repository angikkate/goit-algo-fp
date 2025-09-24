class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Реверсування списку
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev

# Сортування злиттям
def merge_sort(head):
    if not head or not head.next:
        return head
    # пошук середини списку
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    mid = slow.next
    slow.next = None
    # рекурсивне сортування та злиття
    left = merge_sort(head)
    right = merge_sort(mid)
    return merge_sorted(left, right)


# Об’єднання двох відсортованих списків
def merge_sorted(a, b):
    dummy = Node(0)
    tail = dummy
    while a and b:
        if a.data <= b.data:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a if a else b
    return dummy.next


# Допоміжна функція для виводу
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


# Приклад
if __name__ == "__main__":
    # створення списку
    head = Node(3); head.next = Node(1); head.next.next = Node(4)
    head.next.next.next = Node(2); head.next.next.next.next = Node(5)

    print("Початковий список:")
    print_list(head)

    print("Реверсований:")
    head = reverse(head)
    print_list(head)

    print("Відсортований:")
    head = merge_sort(head)
    print_list(head)

    print("Об’єднання двох відсортованих:")
    a = Node(1); a.next = Node(3); a.next.next = Node(5)
    b = Node(2); b.next = Node(4); b.next.next = Node(6)
    merged = merge_sorted(a, b)
    print_list(merged)
