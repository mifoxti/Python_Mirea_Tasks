class SVG:
    def __init__(self):
        self.elements = []

    def line(self, x1, y1, x2, y2, color='black'):
        line_svg = f'<line x1="{x1:.6f}" y1="{y1:.6f}" x2="{x2:.6f}" y2="{y2:.6f}" stroke="{color}" />\n'
        self.elements.append(line_svg)

    def circle(self, cx, cy, r, color='black'):
        circle_svg = f'<circle cx="{cx:.6f}" cy="{cy:.6f}" r="{r:.6f}" fill="{color}" />\n'
        self.elements.append(circle_svg)

    def save(self, filename, width, height):
        with open(filename, 'w') as f:
            f.write(f'<svg version="1.1" width="{width:.6f}" height="{height:.6f}" xmlns="http://www.w3.org/2000/svg">\n')
            for element in self.elements:
                f.write(element)
            f.write('</svg>')
    
# Пример использования:
svg = SVG()
svg.line(10, 10, 60, 10, color='black')
svg.line(60, 10, 60, 60, color='black')
svg.line(60, 60, 10, 60, color='black')
svg.line(10, 60, 10, 10, color='black')

svg.circle(10, 10, r=5, color='red')
svg.circle(60, 10, r=5, color='red')
svg.circle(60, 60, r=5, color='red')
svg.circle(10, 60, r=5, color='red')

svg.save('pic.svg', 100, 100)
