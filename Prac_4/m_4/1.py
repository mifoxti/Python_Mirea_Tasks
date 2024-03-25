class HTML:
    def __init__(self):
        self.code = []

    def p(self, text):
        self.code.append(f'<p>{text}</p>')

    def div(self):
        self.code.append('<div>')
        return self

    def body(self):
        self.code.append('<body>')
        return self

    def get_code(self):
        return '\n'.join(self.code)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.code.append('</div>')


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

print(html.get_code())

