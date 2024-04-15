import os

import matplotlib.pyplot as plt
import networkx as nx


def visualize_project_hierarchy(project_path):
    graph = nx.DiGraph()
    visited = set()

    def traverse_directory(directory):
        nonlocal graph
        nonlocal visited

        if directory in visited:
            return
        visited.add(directory)

        for item in os.listdir(directory):
            full_path = os.path.join(directory, item)

            if os.path.isdir(full_path):
                traverse_directory(full_path)
            elif item.endswith('.py'):
                module_name = os.path.relpath(full_path, project_path)
                module_name = module_name.replace(os.path.sep, '.')[:-3]
                graph.add_node(module_name)

    traverse_directory(project_path)

    for directory, _, files in os.walk(project_path):
        for filename in files:
            if filename.endswith('.py'):
                module_name = os.path.relpath(os.path.join(directory, filename), project_path)
                module_name = module_name.replace(os.path.sep, '.')[:-3]
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    for line in lines:
                        if 'import ' in line:
                            import_module = line.split('import ')[-1].split(',')[0].strip()
                            graph.add_edge(module_name, import_module)
                        elif 'from ' in line:
                            import_module = line.split('from ')[1].split('import')[0].strip()
                            graph.add_edge(module_name, import_module)

    return graph


def draw_graph(graph, output_file):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='skyblue', edge_color='gray',
            arrowsize=20)
    plt.savefig(output_file)
    plt.show()


# Пример использования
project_path = "D:\pyth_mirea"
output_file = "project_hierarchy.png"
graph = visualize_project_hierarchy(project_path)
draw_graph(graph, output_file)
print(f"Граф иерархии модулей проекта сохранен в файле {output_file}")
