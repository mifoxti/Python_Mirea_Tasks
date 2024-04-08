import math
from random import randint
from tkinter import Tk, Canvas, Button

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600

NODE_R = 15

C1, C2, C3, C4 = 2, 50, 20000, 0.1

DELAY = 10

# Boolean variable to track which law is currently in use
USE_LOGARITHMIC_HOOKE = False


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, text):
        self.text = text
        self.targets = []
        self.vec = Vec(0, 0)

    def to(self, *nodes):
        for n in nodes:
            self.targets.append(n)
            n.targets.append(self)
        return self


class Graph:
    def __init__(self):
        self.nodes = []

    def add(self, text):
        self.nodes.append(Node(text))
        return self.nodes[-1]


class GUI:
    def __init__(self, root):
        self.canvas = Canvas(root, width=CANVAS_WIDTH,
                             height=CANVAS_HEIGHT, bg="white")
        self.draw_button = Button(root, text="Draw", command=self.start_draw)
        self.switch_law_button = Button(root, text="Switch Law", command=self.switch_law)
        self.canvas.pack()
        self.draw_button.pack(side="left")
        self.switch_law_button.pack(side="right")
        self.nodes = None
        self.busy = None

    def draw_node(self, x, y, text, r=NODE_R):
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="MistyRose2")
        self.canvas.create_text(x, y, text=text)

    def draw_graph(self):
        for n in self.nodes:
            for t in n.targets:
                self.canvas.create_line(n.vec.x, n.vec.y, t.vec.x, t.vec.y)
        for n in self.nodes:
            self.draw_node(n.vec.x, n.vec.y, n.text)

    def start_draw(self):
        self.canvas.delete("all")
        if self.busy:
            root.after_cancel(self.busy)
        random_layout(self.nodes)
        self.animate()

    def animate(self):
        self.canvas.delete("all")
        for _ in range(DELAY):
            force_layout(self.nodes)
        self.draw_graph()
        self.busy = root.after(5, self.animate)

    def switch_law(self):
        global USE_LOGARITHMIC_HOOKE
        USE_LOGARITHMIC_HOOKE = not USE_LOGARITHMIC_HOOKE


def random_layout(nodes):
    for n in nodes:
        n.vec.x = randint(NODE_R * 4, CANVAS_WIDTH - NODE_R * 4 - 1)
        n.vec.y = randint(NODE_R * 4, CANVAS_HEIGHT - NODE_R * 4 - 1)


def f_spring(u, v):
    delta = Vec(u.vec.x - v.vec.x, u.vec.y - v.vec.y)
    dist = max(math.sqrt(delta.x ** 2 + delta.y ** 2), 1e-6)  # To avoid division by zero
    if USE_LOGARITHMIC_HOOKE:
        force = (C1 * math.log(dist / C2)) * delta.x / dist, (C1 * math.log(dist / C2)) * delta.y / dist
    else:
        force = (C1 * (dist - C2)) * delta.x / dist, (C1 * (dist - C2)) * delta.y / dist
    return force


def f_ball(u, v):
    delta = Vec(u.vec.x - v.vec.x, u.vec.y - v.vec.y)
    dist = max(math.sqrt(delta.x ** 2 + delta.y ** 2), 1e-6)  # To avoid division by zero
    force = (C3 / (dist ** 2 + C4)) * delta.x / dist, (C3 / (dist ** 2 + C4)) * delta.y / dist
    return force


def force_layout(nodes):
    forces = {}
    for n in nodes:
        forces[n] = Vec(0, 0)

    # Compute spring forces
    for n in nodes:
        for target in n.targets:
            spring_force = f_spring(n, target)
            forces[n].x += spring_force[0]
            forces[n].y += spring_force[1]

    # Compute ball forces
    for n1 in nodes:
        for n2 in nodes:
            if n1 != n2:
                ball_force = f_ball(n1, n2)
                forces[n1].x += ball_force[0]
                forces[n1].y += ball_force[1]

    # Update node positions
    for n in nodes:
        n.vec.x += forces[n].x
        n.vec.y += forces[n].y

        # Ensure nodes stay within canvas boundaries
        n.vec.x = min(max(n.vec.x, NODE_R), CANVAS_WIDTH - NODE_R)
        n.vec.y = min(max(n.vec.y, NODE_R), CANVAS_HEIGHT - NODE_R)


g = Graph()
n1 = g.add("1")
n2 = g.add("2")
n3 = g.add("3")
n4 = g.add("4")
n5 = g.add("5")
n6 = g.add("6")
n7 = g.add("7")
n1.to(n2, n3, n4, n5)
n2.to(n5)
n3.to(n2, n4)
n6.to(n4, n1, n7)
n7.to(n5, n1)

root = Tk()
w = GUI(root)
w.nodes = g.nodes
root.mainloop()
