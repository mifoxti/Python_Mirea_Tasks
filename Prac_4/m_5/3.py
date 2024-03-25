import tkinter as tk

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_tree_size(tree):
    if tree is None:
        return 0, 0
    left_width, left_height = get_tree_size(tree.left)
    right_width, right_height = get_tree_size(tree.right)
    width = max(left_width + right_width + 50, 50)
    height = max(left_height, right_height) + 50
    return width, height

def draw_tree(canvas, tree, x, y, level, height):
    if tree is None:
        return

    y_offset = 50 * level

    if tree.left:
        left_x = x - 2 ** (height - level - 1) * 25
        left_y = y + y_offset
        canvas.create_line(x, y, left_x, left_y, fill="black")
        draw_tree(canvas, tree.left, left_x, left_y, level + 1, height)

    if tree.right:
        right_x = x + 2 ** (height - level - 1) * 25
        right_y = y + y_offset
        canvas.create_line(x, y, right_x, right_y, fill="black")
        draw_tree(canvas, tree.right, right_x, right_y, level + 1, height)

    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white", outline="black")
    canvas.create_text(x, y, text=str(tree.val))

def draw_binary_tree(canvas, tree):
    if tree is None:
        return

    width, height = get_tree_size(tree)
    canvas.config(width=width, height=height)
    draw_tree(canvas, tree, width // 2, 50, 1, height // 50)

# Пример использования:
tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
tree = Tree(1, tree_2, tree_8)

# Создаем окно Tkinter
root = tk.Tk()
root.title("Binary Tree Visualization")

# Создаем холст для рисования дерева
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Рисуем дерево
draw_binary_tree(canvas, tree)

root.mainloop()
