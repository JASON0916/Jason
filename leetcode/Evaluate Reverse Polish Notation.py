"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

__author__ = 'phoenix'


class Solution:
  def isOp(self, s):
    return s == "+" or \
           s == "-" or \
           s == "*" or \
           s == "/"


  def add( self, op1, op2 ):
    return op1 + op2

  def sub( self, op1, op2 ):
    return op1 - op2

  def mul( self, op1, op2 ):
    return op1 * op2

  def div( self, op1, op2 ):
    if op1 * op2 < 0:
        return -((-op1) / op2 )
    return op1 / op2

  #mapping from op to func
  operator = { "+": add, "-": sub, "*": mul, "/": div }

  def evalRPN( self, tokens ):
    nums = []
    for s in tokens:
      if self.isOp( s ):
        op2 = nums.pop()
        op1 = nums.pop()
        re = self.operator.get( s )(self, op1, op2 )
        nums.append( re )
      else:
        nums.append( int( s ) )
    return int(nums[ 0 ])


if __name__ == '__main__':
    o = Solution()
    print(o.evalRPN(["4", "13", "5", "/", "+"]))