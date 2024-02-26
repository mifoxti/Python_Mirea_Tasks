# E101 indentation contains mixed spaces and tabs

def mixed_indentation():
    print("This line has both spaces and tabs.")
	print("Indented with a mix.")

# E111 indentation is not a multiple of four

def wrong_indentation():
  print("Indented with two spaces.")

# E112 expected an indented block

def missing_indented_block():
    pass

# E121 continuation line under-indented for hanging indent

long_variable_name = (
value1,
  value2,
)

# E122 continuation line missing indentation or outdented

long_variable_name = [
value1,
value2,
]

# E123 closing bracket does not match indentation of opening bracket's line

def mismatched_brackets():
    if condition:
    return True

# E201 whitespace after '('

function_call( argument)

# E202 whitespace before ')':

function_call(argument )

# E242 tab after ','

mass = [0,  1,  2]

# E301 expected 1 blank line, found 0:

def function_one():
    return 1

def function_two():
    return 2

# E302 expected 2 blank lines, found 0:

def function_one():
    return 1


def function_two():
    return 2

# E303 too many blank lines (3):

def function_with_extra_blank_lines():
    return 1



def another_function():
    return 2

#