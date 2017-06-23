from Stack import Stack


def balanced_parens(expression):
    """
    >>> balanced_parens('()')
    True

    >>> balanced_parens('(')
    False

    >>> balanced_parens(')')
    False

    >>> balanced_parens('(()(()(())))')
    True

    """
    stack = Stack()
    for char in expression:
        if char == '(':
            stack.push(char)
        if char == ')':
            try:
                stack.pop()
            except IndexError:
                return False
    return stack.isEmpty()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
