import os
import argparse


def list_files(path='.', show_hidden=False, long_format=False):
    files = os.listdir(path)

    if not show_hidden:
        files = [f for f in files if not f.startswith('.')]

    files.sort()

    if long_format:
        for file in files:
            file_path = os.path.join(path, file)
            stat_info = os.stat(file_path)
            print(f"{file}\tSize: {stat_info.st_size} bytes\tModified: {stat_info.st_mtime}")
    else:
        print('\n'.join(files))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analog of the 'ls' command in Python.")
    parser.add_argument('path', nargs='?', default='.', help='Path to the directory')
    parser.add_argument('-a', '--all', action='store_true', help='Show hidden files')
    parser.add_argument('-l', '--long', action='store_true', help='Use a long listing format')

    args = parser.parse_args()
    list_files(path=args.path, show_hidden=args.all, long_format=args.long)
