def is_true(s):
 
  stack = []
  mapping = {")": "(", "}": "{", "]": "["}  

  for char in s:
    if char in mapping:  
      if stack and stack[-1] == mapping[char]:
        stack.pop()
      else:
        return False 
    else:  
      stack.append(char)

  return not stack  


s = "()"
if is_true(s):
  print("True")
else:
  print("Not ")
