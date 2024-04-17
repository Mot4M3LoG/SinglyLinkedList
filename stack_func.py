def isempty(stack):
    if stack[0] is None:
        return True
    else:
        return False


def isfull(stack):
    if stack[19] is None:
        return False
    else:
        return True


def push(stack, x):
    global indexer
    if not isfull(stack):
        stack[indexer] = x
        indexer += 1
    else:
        print("stack is full.")


def pop(stack):
    global indexer
    if not isempty(stack):
        value = stack[indexer-1]
        stack[indexer-1] = None
        indexer -= 1
        return value
    else:
        print("stack is empty.")


def top(stack):
    global indexer
    if not isempty(stack):
        value = stack[indexer - 1]
        return value
    else:
        print("stack is empty.")
        return False


def converter(math_str, stack):
    global indexer
    string_holder = ''
    output = ''
    math_str = math_str + ' '
    for char in math_str:
        if char in {' '}:
            if string_holder == '-':  # priority for minus as operator
                stack_top = top(stack)
                if stack_top in {'/', '*'} or isempty(stack):  # if lower
                    # priority in stack, push current to stack
                    push(stack, string_holder)
                    string_holder = ''
                else:
                    while True:  # else, while the same priority,
                        # put into output, otherwise push into stack
                        stack_top = top(stack)
                        if stack_top in {'(', ')', '*', '/'} or isempty(stack):
                            push(stack, string_holder)
                            string_holder = ''
                            break
                        else:
                            output = output + str(pop(stack))
            else:
                output = output + str(string_holder)
                string_holder = ''
            if not output.endswith(' '):
                output = output + ' '
                continue

        elif char.isdigit() or char in {'.'}:
            string_holder = string_holder + str(char)

        elif char in {'+', '-', '/', '*', '('}:
            if char in {'('}:  # highest priority
                push(stack, char)
            elif char in {'+'}:  # second priority plus
                stack_top = top(stack)
                if stack_top in {'/', '*'} or isempty(stack):  # if lower
                    # priority in stack, push current to stack
                    push(stack, char)
                else:
                    while True:  # else, while the same priority,
                        # put into output, otherwise push into stack
                        stack_top = top(stack)
                        if stack_top in {'(', ')', '*', '/'} or isempty(stack):
                            push(stack, char)
                            break
                        else:
                            output = output + str(pop(stack))
            elif char in {'-'}:  # capture, to see if its operator or sign
                string_holder = string_holder + str(char)

            else:  # division or multiplication
                while True:
                    stack_top = top(stack)
                    if stack_top in {'(', ')'} or isempty(stack):
                        push(stack, char)
                        break
                    else:
                        output = output + str(pop(stack))

        elif char in {')'}:
            while True:
                if stack[indexer-1] == '(':
                    pop(stack)
                    break
                else:
                    tmp_holder = pop(stack)
                    output = output + str(tmp_holder) + ' '

    output = output + str(string_holder)
    string_holder = ''
    while not isempty(stack):
        if not output.endswith(' '):
            output = output + ' '
        tmp_holder = pop(stack)
        output = output + str(tmp_holder)
    output = output + str(string_holder)
    print("the expression rewritten looks like " + str(output))
    return output


def calculator(output, stack):
    global indexer
    is_wrong = False
    output = output + ' '
    indexer = 0
    str_holder = ''
    for char in output:
        if char.isdigit() or char in {'.'}:
            str_holder = str_holder + str(char)
        elif char in {' '}:
            if str_holder == '-':
                if indexer >= 2:
                    value_holder = 0
                    value_holder = value_holder - float(pop(stack))
                    value_holder = value_holder + float(pop(stack))
                    push(stack, value_holder)
                    str_holder = ''
                else:
                    is_wrong = True
                    break
            elif str_holder == '':
                pass
            else:
                push(stack, float(str_holder))
                str_holder = ''

        elif char in {'-'}:
            str_holder = str_holder + str(char)

        elif indexer >= 2:
            if char in {'+'}:
                value_holder = 0
                value_holder = value_holder + float(pop(stack))
                value_holder = value_holder + float(pop(stack))
                push(stack, value_holder)
            elif char in {'*'}:
                value_holder = 0
                value_holder = value_holder + float(pop(stack))
                value_holder = value_holder * float(pop(stack))
                push(stack, value_holder)
            elif char in {'/'}:
                value_holder2 = float(pop(stack))
                value_holder = (float(pop(stack))) / value_holder2
                push(stack, value_holder)
        else:
            is_wrong = True
            break
    if not is_wrong:
        outcome = pop(stack)
        print("the value of expression = " + str(outcome))
    else:
        print("expression is wrong.")


indexer = 0
if __name__ == '__main__':
    Stack = [None] * 20
    maths = input("enter your math: ")
    out = converter(maths, Stack)
    calculator(out, Stack)
