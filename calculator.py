def calculator(x, y, operator):
    if operator == "+":
        print(f"The result of {x} {operator} {y} = {x + y}")
    if operator == "-":
        print(f"The result of {x} {operator} {y} = {x-y}")
    if operator == "*":
        print(f"The result of {x} {operator} {y} = {x*y}")
    if operator == "/":
        print(f"The result of {x} {operator} {y} = {x/y}")


calculator(54, 3, "/")