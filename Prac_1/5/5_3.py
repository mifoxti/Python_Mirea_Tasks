import numpy as np
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def box(x, y, size):
    dx = np.maximum(np.abs(x) - size, 0)
    dy = np.maximum(np.abs(y) - size, 0)
    return np.sqrt(dx**2 + dy**2)

def circle(x, y, radius):
    return np.sqrt(x**2 + y**2) - radius

def difference(a, b):
    return np.maximum(a, -b)

def sdf_func(x, y):
    return difference(box(x, y, 0.4), circle(x, y, 0.3))

# Create tkinter window
root = tk.Tk()
root.title("SDF Visualization")

# Create a matplotlib figure
fig = Figure(figsize=(6, 6), dpi=100)
ax = fig.add_subplot(111)

# Generate data for visualization
x = np.linspace(-1, 1, 400)
y = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x, y)
result_sdf = sdf_func(X, Y)

# Plot the SDF on the matplotlib figure
contour = ax.contourf(X, Y, result_sdf, levels=20, cmap='viridis')
ax.set_title('SDF for Box - Circle (Difference)')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Create a tkinter canvas to embed the matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Add a colorbar
cbar = fig.colorbar(contour, ax=ax)
cbar.set_label('SDF Values')

# Run the tkinter main loop
tk.mainloop()
