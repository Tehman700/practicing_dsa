def reverse_parentheses(s):
    stack = [""]
    for ch in s:
        if ch == '(':
            stack.append("")             # start a fresh buffer for this bracket level
        elif ch == ')':
            inner = stack.pop()          # this is the content of the pair we just closed
            reversed_inner = inner[::-1] # reverse it, right here, right now
            stack[-1] += reversed_inner  # fold into the parent level and keep moving outward
        else:
            stack[-1] += ch

    return stack[0]
s = "(u(love)i)"
print(reverse_parentheses(s))   # iloveu
