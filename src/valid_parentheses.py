from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    stack = MyStack()
    pairs = {')': '(', '}': '{', ']': '['}
    for char in string:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()
