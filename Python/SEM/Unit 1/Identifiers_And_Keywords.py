#reserved words -> kewwords
#user defined names -> identifiers

# Define a function to check if a number is even
def is_even(number):  # 'is_even' is an identifier, 'def' is a keyword
    if number % 2 == 0:  # 'if' is a keyword
        return True  # 'return' is a keyword
    else:  # 'else' is a keyword
        return False

# Main program
num = 10  # 'num' is an identifier, '=' is an assignment operator
result = is_even(num)  # 'result' and 'is_even' are identifiers

# Print the result
if result:  # 'if' is a keyword
    print(f"{num} is even")  # 'print' is a function (identifier)
else:
    print(f"{num} is odd")  # 'else' is a keyword
