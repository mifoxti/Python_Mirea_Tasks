import ast
import tkinter as tk


class TreeDrawer:
    def __init__(self, root, canvas, width=800, height=600):
        self.root = root
        self.canvas = canvas
        self.width = width
        self.height = height
        self.node_radius = 20
        self.level_height = 80
        self.level_width = 40
        self.level_padding = 40

    def draw_tree(self):
        self.canvas.delete("all")
        if self.root:
            self._draw_node(self.root, self.width / 2, self.level_padding, self.width / 4)

    def _draw_node(self, node, x, y, dx):
        if node:
            self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius,
                                    fill="lightblue")
            self.canvas.create_text(x, y, text=node.name, font=("Arial", 12))
            if node.children:
                next_dx = dx / len(node.children)
                next_x = x - (dx * (len(node.children) - 1)) / 2
                next_y = y + self.level_height
                for child in node.children:
                    self.canvas.create_line(x, y + self.node_radius, next_x, next_y - self.node_radius)
                    self._draw_node(child, next_x, next_y, next_dx)
                    next_x += dx
            self.canvas.update()


class TreeNode:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children if children else []


def ast_to_tree(node):
    if isinstance(node, ast.AST):
        name = type(node).__name__
        children = [ast_to_tree(child) for child in ast.iter_child_nodes(node)]
        return TreeNode(name, children)
    else:
        return TreeNode(str(node))


def main():
    code = """
for i in range(5):
    print(i)
    if i == 3:
        break
    """
    tree = ast.parse(code)
    root = ast_to_tree(tree)

    window = tk.Tk()
    window.title("AST Tree Visualization")
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack()

    tree_drawer = TreeDrawer(root, canvas)
    tree_drawer.draw_tree()

    window.mainloop()


if __name__ == "__main__":
    main()
