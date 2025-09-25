def arithmetic_arranger(problems, show_answer = False):
  if len(problems) > 5 :
    print("Error: Too many problems.")
    return

  for problem in problems:
    list_problem = problem.split()
    operator = list_problem[1]
    operands = list_problem[::2]
    print(f"Operands: {operands}, Operator: {operator}")
    if operator != "+" and operator != "-":
      print("Error: Operator must be '+' or '-'.")
      return
    for operand in operands:
      if len(operand) > 4:
        print("Error: Numbers cannot be more than four digits.")
        return
      if operand.isdigit() == False:
        print("Error: Numbers must only contain digits.")
        return

arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])