import sys
import re


def process_quotes(line):
    inside_code_block = False
    processed_line = ""

    for char in line:
        if char == '`':
            inside_code_block = not inside_code_block

        if not inside_code_block and char == '"':
            processed_line += '“' if len(processed_line) % 2 == 0 else '”'
        else:
            processed_line += char

    return processed_line


def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    processed_lines = [process_quotes(line) for line in lines]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(processed_lines)


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = f"modified_{input_file}"

        process_file(input_file, output_file)
        print(f"Quotes processed and saved to {output_file}")
    else:
        print("Usage: python markdown_quotes_converter.py <input_file>")
        print("If no arguments provided, the program will process standard input.")

        input_lines = sys.stdin.readlines()
        processed_lines = [process_quotes(line) for line in input_lines]
        sys.stdout.writelines(processed_lines)


if __name__ == "__main__":
    main()
