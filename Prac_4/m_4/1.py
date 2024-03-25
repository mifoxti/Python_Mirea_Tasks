class Tag:
    def __init__(self, name):
        self.name = name
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __call__(self, *args, **kwargs):
        for arg in args:
            self.children.append(str(arg))

    def __str__(self):
        content = '\n'.join(self.children)
        return f'<{self.name}>\n{content}\n</{self.name}>'


class HTML:
    def __init__(self):
        self.root = None
        self.current_tag = None

    def __getattr__(self, name):
        if name not in self.__dict__:
            self.current_tag = Tag(name)
            if self.root is None:
                self.root = self.current_tag
            else:
                self.root.children.append(self.current_tag)
            return self.current_tag
        return self.__dict__[name]

    def get_code(self):
        return str(self.root)


# Пример использования
html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

print(html.get_code())
