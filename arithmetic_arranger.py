def arithmetic_arranger(problems, show_answers=False):
    #Review the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    #Initialise lists
    operands_left = []
    operators = []
    operands_right = []
    answers = []

    # Parse each problem and check for errors
    for problem in problems:
        operands = problem.split()
        operand_left = operands[0]
        operator = operands[1]
        operand_right = operands[2]

        # Check operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check operands
        if not operand_left.isdigit() or not operand_right.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand_left) > 4 or len(operand_right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Compute answer if requested
        if show_answers:
            if operator == "+":
                answer = int(operand_left) + int(operand_right)
            else:
                answer = int(operand_left) - int(operand_right)
            answers.append(str(answer))

        # Store operands and operator
        operands_left.append(operand_left)
        operators.append(operator)
        operands_right.append(operand_right)

    # Compute maximum length of operands and answer
    max_length = max([len(operand) for operand in operands_left + operands_right + answers])

    # Initialize list to store formatted lines
    lines = []

    # Format each problem and answer
    for i in range(len(problems)):
        # Pad left operand and answer with spaces
        operand_left = operands_left[i].rjust(max_length)
        answer = answers[i].rjust(max_length) if show_answers else ""

        # Pad right operand with spaces and concatenate parts into a single line
        operand_right = operands_right[i].rjust(max_length)
        line = operand_left + " " + operators[i] + " " + operand_right + "    " + answer
        lines.append(line)

    # Concatenate lines into a single string and add horizontal lines if requested
    arranged_problems = "\n".join(lines)
    if show_answers:
        horizontal_lines = ["-" * max_length for i in range(len(problems))]
        arranged_problems += "\n" + "    ".join(horizontal_lines) + "    "

    return arranged_problems

print("Welcome to the Arithmetic Arranger")
problems = input("Insert your problems split by commas, Example: 500 + 56, 840 - 10: ")
problem_list = problems.split(",")

resultado = arithmetic_arranger(problem_list, True)

print(resultado)