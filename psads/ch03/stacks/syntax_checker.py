from Stack import Stack

def balanced_parens(expression):
    stack = Stack()
    for idx, token in enumerate(expression):
        if token == '(':
            stack.push(token)
            last_open_paren = idx
        if token == ')':
            try:
                stack.pop()
            except IndexError:
                msg = 'Found unmatched )' + '\n'
                msg += expression + '\n'
                msg += (' ' * idx) + '^'
                raise SyntaxError(msg)
        there_are_more_tokens = (idx != len(expression)-1)
        if stack.isEmpty() and there_are_more_tokens:
            msg = 'Matched parens, but there are extra tokens!\n'
            msg += expression + '\n'
            msg += (' ' * (idx + 1)) + '^'
            raise SyntaxError(msg)
    if not stack.isEmpty():
        msg = 'Found unmatched (' + '\n'
        msg += expression + '\n'
        msg += (' ' * last_open_paren) + '^'
        raise SyntaxError(msg)
    return True

