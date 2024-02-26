import tkinter as tk
import math

def draw_pacman(canvas, size, angle):
    canvas.create_arc(0, 0, size, size, start=angle, extent=360-angle*2, style=tk.PIESLICE, fill='yellow', outline='black')

def draw_eye(canvas, size):
    eye_size = size // 15
    eye_x = size // 1.8
    eye_y = size // 3
    canvas.create_oval(eye_x - eye_size, eye_y - eye_size, eye_x + eye_size, eye_y + eye_size, fill='black')

def main():
    root = tk.Tk()
    root.title("Pac-Man")

    canvas_size = 200
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg='black')
    canvas.pack()

    pacman_angle = 30  # Уменьшенный угол рта

    draw_pacman(canvas, canvas_size, pacman_angle)
    draw_eye(canvas, canvas_size)

    root.mainloop()

if __name__ == "__main__":
    main()