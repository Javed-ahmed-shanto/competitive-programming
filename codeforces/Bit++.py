def execute_program(program):
    x = 0
    for statement in program:
        if "++" in statement:
            x += 1
        elif "--" in statement:
            x -= 1
    return x

if __name__ == "__main__":
    n = int(input().strip())  # Number of statements
    program = [input().strip() for _ in range(n)]  # Read the program
    final_value = execute_program(program)
    print(final_value)
