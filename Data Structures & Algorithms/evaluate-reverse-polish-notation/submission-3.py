class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                second = stack[-1]
                stack.pop(-1)
                first = stack[-1]
                stack.pop(-1)
                result = None
                match i:
                    case "+":
                        result = first + second
                    case "-":
                        result = first - second
                    case "*":
                        result = first * second
                    case "/":
                        result = int(first / second)
                stack.append(result)
        return stack[0]

                
        