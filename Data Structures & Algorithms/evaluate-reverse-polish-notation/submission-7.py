class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i == "+":
                a = stack.pop()
                b = stack.pop()
                c = b + a
                stack.append(c)
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                c = b - a
                stack.append(c)
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                c = int(b / a)
                stack.append(c)
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                c = b * a
                stack.append(c)
            else:
                stack.append(int(i))
            
            result = stack[-1]
        
        return result
        