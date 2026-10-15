class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
            
        stack = []
        operations = ["+", "-", "*", "/"]
        for i in range(len(tokens)):
            if tokens[i] in operations:
                result = self.eval(tokens[i], int(stack.pop()), int(stack.pop()))
                stack.append(result)
            else:
                stack.append(tokens[i])
        
        return stack.pop()

    def eval(self, operation, operand_2, operand_1):
        match operation:
            case "+":
                return operand_1 + operand_2
            case "-":
                return operand_1 - operand_2
            case "*":
                return operand_1 * operand_2
            case "/":
                return int(operand_1 / operand_2)