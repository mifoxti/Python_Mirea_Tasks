import os
import argparse
import graphviz


def create_directory_tree(root_path):
    tree = graphviz.Digraph(comment='Directory Tree', format='png')
    add_node(tree, root_path)
    create_tree(tree, root_path)
    return tree


def create_tree(tree, current_path):
    if os.path.isdir(current_path):
        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)
            add_node(tree, item_path)
            create_tree(tree, item_path)


def add_node(tree, path):
    if os.path.isdir(path):
        tree.node(path, shape='folder', color='blue')
    else:
        tree.node(path, shape='file', color='green')


def main():
    parser = argparse.ArgumentParser(description='Generate directory tree in Graphviz format.')
    parser.add_argument('path', metavar='path', type=str, help='Root path for the directory tree')
    parser.add_argument('-o', '--output', metavar='output', type=str, default='directory_tree',
                        help='Output file name (without extension)')
    args = parser.parse_args()

    tree = create_directory_tree(args.path)
    output_file = args.output + '.png'
    tree.render(output_file, format='png', cleanup=True)

    print(f"Directory tree saved to {output_file}")


if __name__ == "__main__":
    main()
