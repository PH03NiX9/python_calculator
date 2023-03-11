# Define a function for each arithmetic operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Define a function to evaluate expressions with parentheses
def evaluate(expression):
    # Convert the expression to a list of tokens
    tokens = []
    current_token = ''
    for char in expression:
        if char in '0123456789.':
            current_token += char
        else:
            if current_token != '':
                tokens.append(float(current_token))
                current_token = ''
            tokens.append(char)
    if current_token != '':
        tokens.append(float(current_token))

    # Evaluate the expression using the Shunting Yard algorithm
    output_queue = []
    operator_stack = []
    for token in tokens:
        if isinstance(token, float):
            output_queue.append(token)
        elif token in '+-*/':
            while operator_stack and operator_stack[-1] in '*/' and token in '+-':
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())

    # Evaluate the postfix expression
    operand_stack = []
    for token in output_queue:
        if isinstance(token, float):
            operand_stack.append(token)
        elif token in '+-*/':
            y = operand_stack.pop()
            x = operand_stack.pop()
            if token == '+':
                result = add(x, y)
            elif token == '-':
                result = subtract(x, y)
            elif token == '*':
                result = multiply(x, y)
            elif token == '/':
                result = divide(x, y)
            operand_stack.append(result)

    return operand_stack[0]

# Evaluate expressions until the user enters 'q'
while True:
    expression = input("Enter an expression (or 'q' to quit): ")
    if expression == 'q':
        break
    result = evaluate(expression)
    print(expression, "=", result)