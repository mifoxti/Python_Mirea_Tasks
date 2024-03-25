import tkinter as tk


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_tree():
    """
    Создает пример бинарного дерева.
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


def tree_coordinates(root, x, y, canvas, level_height=50, level_width=50):
    """
    Рекурсивно определяет координаты узлов дерева.
    """
    if root is None:
        return

    # Рисуем текущий узел
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white", outline="black")
    canvas.create_text(x, y, text=str(root.val))

    # Рисуем связь с левым узлом
    if root.left:
        canvas.create_line(x, y, x - level_width, y + level_height, fill="black")
        tree_coordinates(root.left, x - level_width, y + level_height, canvas, level_height, level_width / 2)

    # Рисуем связь с правым узлом
    if root.right:
        canvas.create_line(x, y, x + level_width, y + level_height, fill="black")
        tree_coordinates(root.right, x + level_width, y + level_height, canvas, level_height, level_width / 2)


def visualize_tree(root):
    """
    Визуализирует бинарное дерево.
    """
    root_window = tk.Tk()
    root_window.title("Binary Tree Visualization")

    canvas_width = 800
    canvas_height = 600
    canvas = tk.Canvas(root_window, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Рисуем дерево
    tree_coordinates(root, canvas_width / 2, 50, canvas)

    root_window.mainloop()


# Создаем пример бинарного дерева
root = create_tree()

# Визуализируем дерево
visualize_tree(root)
