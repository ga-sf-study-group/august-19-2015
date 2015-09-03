import sys
from string import rfind
import pdb

if __name__ == '__main__':
  if len(sys.argv) > 1:
    maps = {'(': ')', '{': '}', '[': ']'}
    s = sys.argv[1]
    stack = []
    for k in s:
      if k in maps.keys():
        stack.append(k)
      elif k in maps.values():
        if len(stack) == 0 or maps[stack.pop()] != k:
          print 'not valid paranthesis'
          exit(0)
    if len(stack) == 0:
      print 'valid paranthesis'
    else:
      print 'not valid paranthesis'
  else:
    print 'input an expression'
    print 'run the program as:'
    print 'python valid_paranthesis.py "[](){}}"'
