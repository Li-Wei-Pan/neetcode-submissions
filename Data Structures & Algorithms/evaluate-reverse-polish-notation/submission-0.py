class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack to store values if encounter operators then perform calculation
        num_list = []
        operators = ['+', "-", "*", "/"]
        for i in tokens:
            if i not in operators:
                num_list.append(int(i))
            else:
                b = num_list.pop()
                a = num_list.pop()
                if i == '+':
                    num_list.append(a + b)
                elif i == '-':
                    num_list.append(a - b)
                elif i == '*':
                    num_list.append(a * b)
                else:
                    num_list.append(int(a / b))  # truncate toward zero
        return num_list[0]
        print(num_list)