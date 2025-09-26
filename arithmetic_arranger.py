def arithmetic_arranger(problems, show_answer = False):
  result_list = []
  max_length = 0
  if len(problems) > 5 :
    return("Error: Too many problems.")

  for problem in problems:
    list_problem = problem.split()
    operands = list_problem[::2]
    operator = list_problem[1]

    if operator != "+" and operator != "-":
      return("Error: Operator must be '+' or '-'.")
    for operand in operands:
      if len(operand) > 4:
        return("Error: Numbers cannot be more than four digits.")
      if operand.isdigit() == False:
        return("Error: Numbers must only contain digits.")
    
    longitud_first_number = len(operands[0])
    longitud_second_number = len(operands[1])
    if longitud_first_number > longitud_second_number:
      max_length = longitud_first_number + 2
    else:
      max_length = longitud_second_number + 2
    dashes = "-" * max_length
    first_number_spaces = max_length - longitud_first_number
    second_number_spaces = max_length - 1 - longitud_second_number 
    result_list.append(" " * first_number_spaces + operands[0])
    result_list.append(operator + " " * second_number_spaces + operands[1])
    result_list.append(dashes)
    separator = "    "
 
    if show_answer == True:
      result = ""
      if operator == "+":
        result = str(int(operands[0]) + int(operands[1]))
      else:
        result = str(int(operands[0]) - int(operands[1]))
      result_number_spaces = max_length - len(result)
      result_list.append(" " * result_number_spaces + result)
      firts_row = separator.join(result_list[0::4])
      second_row = separator.join(result_list[1::4])
      third_row = separator.join(result_list[2::4]) 
      four_row = separator.join(result_list[3::4])
    else: 
      firts_row = separator.join(result_list[0::3])
      second_row = separator.join(result_list[1::3])
      third_row = separator.join(result_list[2::3])        
   
  
    
  if show_answer != True:
    return (f"{firts_row}\n{second_row}\n{third_row}")
  else:
    return (f"{firts_row}\n{second_row}\n{third_row}\n{four_row}")

print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))




  
   