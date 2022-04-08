'''
COURSE: FreeCodeCamp's Scientific Computing With Python
CHALLENGE: Arithemtic Formatter

## DESCRIPTION

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.
Example

Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

Output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----


Function Call:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

Output:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474

## RULES

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

    Situations that will return an error:
        If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
        The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
        Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
        Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.

    If the user supplied the correct format of problems, the conversion you return will follow these rules:
        There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
        Numbers should be right-aligned.
        There should be four spaces between each problem.
        There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
  
  ## SOLUTION: https://replit.com/@DaniloBilanoski/boilerplate-arithmetic-formatter#arithmetic_arranger.py

'''

def arithmetic_arranger(arithmetic_problems, solutions=False):
 
  if len(arithmetic_problems) > 5:
    return ("Error: Too many problems.")

  first_line = list()
  second_line = list()
  third_line = list()
  fourth_line = list()
  sorted_problems = list()

  problems = tuple(arithmetic_problems)

  for p in problems:
    num1, operator, num2 = p.split()

    if num1.isdigit() == False or num2.isdigit() == False:
      return ("Error: Numbers must only contain digits.")
    
    if operator not in (["+", "-"]):
      return ("Error: Operator must be '+' or '-'.")
    
    if len(num1) > 4 or len(num2) > 4:
      return ("Error: Numbers cannot be more than four digits.")
    
    line_lenght = max(len(num1),len(num2))

    first_line.append(num1.rjust(line_lenght + 2) + "    ")
    second_line.append(f"{operator} {num2.rjust(line_lenght)}    ")
    third_line.append("-"*(line_lenght+2) + "    ")
    fourth_line.append(str(eval(num1 + operator + num2)).rjust(line_lenght + 2) + "    ")
  
  if solutions == True:
    sorted_problems = f"{''.join(first_line).rstrip()}\n{''.join(second_line).rstrip()}\n{''.join(third_line).rstrip()}\n{''.join(fourth_line).rstrip()}"
  else:
    sorted_problems = f"{''.join(first_line).rstrip()}\n{''.join(second_line).rstrip()}\n{''.join(third_line).rstrip()}"
  
  return sorted_problems

print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
