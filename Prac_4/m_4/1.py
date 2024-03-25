class Tag:
    def __init__(self, name):
        self.name = name
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __call__(self, *args, **kwargs):
        child = Tag(*args, **kwargs)
        self.children.append(child)
        return child

    def get_code(self, indent=0):
        code = ' ' * indent + f'<{self.name}>\n'
        for child in self.children:
            code += child.get_code(indent + 4)
        code += ' ' * indent + f'</{self.name}>\n'
        return code

    # Метод для добавления содержимого в тег
    def content(self, content):
        self.children.append(content)
        return self


class HTML(Tag):
    def __init__(self):
        super().__init__('html')

    def body(self):
        return Body()

    def get_code(self):
        code = '<!DOCTYPE html>\n'
        code += super().get_code()
        return code

    # Метод для создания тега <div>
    def div(self):
        return Div()


class Body(HTML):
    def __init__(self):
        super().__init__('body')


class Div(HTML):
    def __init__(self):
        super().__init__('div')

    def p(self, content):
        return self.content(P(content))


class P(HTML):
    def __init__(self, content):
        super().__init__('p')
        self.content(content)


if __name__ == '__main__':
    html = HTML()
    with html.body() as body:
        with html.div() as div1:
            with div1.div() as div2:
                div2.p('Первая строка.')
                div2.p('Вторая строка.')
            with div1.div() as div3:
                div3.p('Третья строка.')

    print(html.get_code())
