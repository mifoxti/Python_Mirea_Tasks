class Tag:
    def __init__(self, name):
        self.name = name
        self.children = []

    def __enter__(self):
        print(f'<{self.name}>')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'</{self.name}>')

    def __call__(self, *args, **kwargs):
        for content in args:
            print(f'<{self.name}>{content}</{self.name}>')


class HTML:
    def __enter__(self):
        print('<html>')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('</html>')

    def __getattr__(self, item):
        return Tag(item)


html = HTML()
with html.body() as body:
    with body.div() as div1:
        with div1.div() as div2:
            div2.p('Первая строка.')
            div2.p('Вторая строка.')
        with body.div() as div3:
            div3.p('Третья строка.')
