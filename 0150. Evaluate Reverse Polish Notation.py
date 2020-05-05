from typing import List
import numpy as np

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []
        for t in tokens:
            if t == '+':
                right = number_stack.pop()
                left = number_stack.pop()
                ret = left + right
                number_stack.append(ret)
            elif t == '-':
                right = number_stack.pop()
                left = number_stack.pop()
                ret = left - right
                number_stack.append(ret)
            elif t == '*':
                right = number_stack.pop()
                left = number_stack.pop()
                ret = left * right
                number_stack.append(ret)
            elif t == '/':
                right = number_stack.pop()
                left = number_stack.pop()
                ret = abs(left) // abs(right)
                if left * right < 0:
                    ret *= -1
                number_stack.append(ret)
            else:
                number_stack.append(int(t))
            # print(number_stack)
        return number_stack[0]

if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ret = Solution().evalRPN(tokens)
    print(ret)
    nimei = np.floor(6 / (-132))
    print(nimei)