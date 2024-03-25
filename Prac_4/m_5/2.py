import tkinter as tk

scale_x = 25
scale_y = 50
radius = 10

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.x = 0
        self.y = 0

class BinaryTreeVisualizer:
    def __init__(self):
        self.current_x = 0

    def visualize(self, tree, depth=0):
        if tree is None:
            return

        # Рекурсивно обходим левое поддерево
        self.visualize(tree.left, depth + 1)

        # Назначаем координаты текущему узлу
        tree.x = self.current_x
        tree.y = depth * scale_y

        # Увеличиваем текущую позицию x
        self.current_x += scale_x

        # Рекурсивно обходим правое поддерево
        self.visualize(tree.right, depth + 1)

def draw_tree(canvas, tree):
    if tree is None:
        return

    # Рисуем узел
    canvas.create_oval(tree.x - radius, tree.y - radius, tree.x + radius, tree.y + radius, fill="white", outline="black")
    canvas.create_text(tree.x, tree.y, text=str(tree.val))

    # Рисуем связь с левым узлом
    if tree.left:
        canvas.create_line(tree.x, tree.y, tree.left.x, tree.left.y, fill="black")

    # Рисуем связь с правым узлом
    if tree.right:
        canvas.create_line(tree.x, tree.y, tree.right.x, tree.right.y, fill="black")

# Пример использования:
tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
tree = Tree(1, tree_2, tree_8)

visualizer = BinaryTreeVisualizer()
visualizer.visualize(tree)

# Создаем окно Tkinter
root = tk.Tk()
root.title("Binary Tree Visualization")

# Создаем холст для рисования дерева
canvas_width = visualizer.current_x + scale_x
canvas_height = max(node.y for node in [tree, tree_2, tree_8]) + scale_y
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Рисуем дерево
draw_tree(canvas, tree)

root.mainloop()
