class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack to keep track of opening parentheses

        for c in s:  # Iterate through each character in the input string
            if c == "(":  # If the character is an opening parenthesis
                stack.append(")")  # Push the corresponding closing parenthesis onto the stack
            elif c == "{":  # If the character is an opening curly brace
                stack.append("}")  # Push the corresponding closing curly brace onto the stack
            elif c == "[":  # If the character is an opening square bracket
                stack.append("]")  # Push the corresponding closing square bracket onto the stack
            elif not stack or stack.pop() != c:
                # If the character is not an opening parenthesis, curly brace, or square bracket,
                # or if the stack is empty, or the top of the stack does not match the current character,
                # then the string is not valid
                return False

        # After iterating through the entire string, check if the stack is empty
        # If the stack is empty, it means all opening parentheses have matching closing parentheses
        return not stack
