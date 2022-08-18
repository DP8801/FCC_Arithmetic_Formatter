def arithmetic_arranger(problems,boo=False):

  if len(problems) <= 5:
    
    left_op, op, right_op, justification = [],[],[],[]
    arranged_problems = ""
    valid_op = ["+", "-"]
    
    for i in problems:
      exp = i.split(" ")
      
      if exp[1] in valid_op:
        op.append(exp[1])                            #operator
      else:
        return "Error: Operator must be '+' or '-'."

      if exp[0].isdigit() and exp[2].isdigit():
        if len(exp[0])<=4 and len(exp[2])<=4:
          left_op.append(exp[0])                         #left operand
          right_op.append(exp[2])                        #right operand
        else:
          return "Error: Numbers cannot be more than four digits."
      else:
        return "Error: Numbers must only contain digits."
    
    for i in range(len(problems)):
      if len(left_op[i]) > len(right_op[i]):
        justification.append(len(left_op[i]) + 2)
      elif len(right_op[i]) > len(left_op[i]):
        justification.append(len(right_op[i]) + 2)
      else:
        justification.append(len(right_op[i]) + 2)
        
    for i in range(3):
  
      if i == 0:
        for j in range(len(problems)):
          if j!= len(problems) - 1:
            arranged_problems += "{}    ".format(left_op[j].rjust(justification[j]))
          else:
            arranged_problems += "{}\n".format(left_op[j].rjust(justification[j]))        
      elif i == 1:
        for j in range(len(problems)):
          if j!= len(problems) - 1:
            arranged_problems += "{}{}    ".format(op[j],right_op[j].rjust(justification[j]-1))
          else:
            arranged_problems += "{}{}\n".format(op[j],right_op[j].rjust(justification[j]-1))
            
      else:
        for j in range(len(problems)):
          if j != len(problems) - 1:
            arranged_problems += "".rjust(justification[j], "-") + "    "
          else:
            arranged_problems += "".rjust(justification[j], "-")
    try: 
      if boo == True:
        arranged_problems += "\n"
        for i in range(len(problems)):
          if op[i] == "+":
            result = str(int(left_op[i]) + int(right_op[i]))
            if i != len(problems) - 1:
              arranged_problems += result.rjust(justification[i]) + "    "
            else:
              arranged_problems += result.rjust(justification[i])
          else:
            result = str(int(left_op[i]) - int(right_op[i]))
            if i!= len(problems) - 1:
              arranged_problems += result.rjust(justification[i]) + "    "
            else:
              arranged_problems += result.rjust(justification[i])
    finally:
      return arranged_problems
  
  else:
    return "Error: Too many problems."
  # return arranged_problems