import turtle as t
import math as m

def draw_branch(length, spread, depth):
    if depth == 0:
        return

    # Рухаємося вперед, малюючи поточну гілку
    t.forward(length)

    # Поворот вправо і рекурсивне малювання правої гілки
    t.right(spread)
    draw_branch(length * m.cos(m.radians(spread)), spread, depth - 1)

    # Поворот вліво для малювання лівої гілки
    t.left(2 * spread)
    draw_branch(length * m.cos(m.radians(spread)), spread, depth - 1)

    # Повертаємося в початкову позицію гілки
    t.right(spread)
    t.backward(length)

def main():
    # Запитуємо у користувача глибину рекурсії
    depth = int(input("Введіть рівень рекурсії: "))

    # Підготовка екрану для малювання
    screen = t.Screen()
    screen.bgcolor("white")

    # Налаштовуємо черепашку: початкова позиція і напрямок
    t.left(90)  # дивимося вгору
    t.penup()
    t.goto(0, -screen.window_height() // 2)  # старт знизу екрана
    t.pendown()
    t.speed(0)  # максимальна швидкість малювання

    # Малюємо дерево рекурсивно
    draw_branch(100, 30, depth)

    # Завершуємо роботу черепашки
    t.done()

if __name__ == "__main__":
    main()