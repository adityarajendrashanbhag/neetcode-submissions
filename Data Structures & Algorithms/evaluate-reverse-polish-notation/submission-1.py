class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        arithmetic_notation = ["+", "-", "*", ""]
        
        for i in tokens:
            if i in "+":
                a = stack.pop()
                b = stack.pop()
                c = int(b) + int(a)
                stack.append(c)
            elif i in "-":
                a = stack.pop()
                b = stack.pop()
                c = int(b) - int(a)
                stack.append(c)
            elif i in "/":
                a = stack.pop()
                b = stack.pop()
                c = int(b) / int(a)
                stack.append(c)
            elif i in "*":
                a = stack.pop()
                b = stack.pop()
                c = int(b) * int(a)
                stack.append(c)
            else:
                stack.append(i)
            
            result = int(stack[-1])
        
        return result
        