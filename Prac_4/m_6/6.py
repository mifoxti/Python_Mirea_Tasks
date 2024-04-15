import inspect


def get_doc(obj):
    """
    Получает docstring объекта.
    """
    doc = inspect.getdoc(obj)
    if doc is None:
        return ""
    return doc.strip()


def generate_md_doc(module_name):
    """
    Генерирует Markdown-документацию для модуля.
    """
    module = __import__(module_name)

    with open(f"{module_name}.md", "w") as f:
        f.write(f"# Модуль {module_name}\n\n")

        # Описание модуля
        doc = get_doc(module)
        if doc:
            f.write(doc + "\n\n")

        for name, obj in inspect.getmembers(module):
            # Пропускаем внутренние объекты
            if name.startswith("__"):
                continue

            # Классы
            if inspect.isclass(obj):
                f.write(f"## Класс {name}\n\n")

                doc = get_doc(obj)
                if doc:
                    f.write(doc + "\n\n")

                for meth_name, meth in inspect.getmembers(obj):
                    if not inspect.isfunction(meth):
                        continue

                    f.write(f"* **Метод** `{meth_name}{inspect.signature(meth)}`\n\n")

                    doc = get_doc(meth)
                    if doc:
                        f.write(doc + "\n\n")

            # Функции
            elif inspect.isfunction(obj):
                f.write(f"## Функция {name}\n\n")

                sig = inspect.signature(obj)
                f.write(f"Сигнатура: `{sig}`\n\n")

                doc = get_doc(obj)
                if doc:
                    f.write(doc + "\n\n")


if __name__ == "__main__":
    module_name = "m"
    generate_md_doc(module_name)

    print(f"Документация для модуля '{module_name}' успешно сгенерирована в файле '{module_name}.md'.")
