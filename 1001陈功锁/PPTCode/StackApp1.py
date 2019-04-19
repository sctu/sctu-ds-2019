from SStack import *

class ESStack(SStack):
    def depth(self):
        return len(self.elems)

#############################################
######## Paretheses checker #################

def check_pares(text):
    pares = "()[]{}"
    open_pares = "([{"
    opposite = {")":"(", "]":"[", "}":"{"}

    def paretheses(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in pares:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
    
    st = SStack()
    for pr, i in paretheses(text):
        if pr in open_pares: # push open pares into stack
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print("Unmatching is found at", i, "for", pr)
            return False
    print("All paretheses are correctly matched.")
    return True

################################################
####### Suffix expression evaluator ############

def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())

def suf_exp_evaluator(exp):
    """exp is a list of items representing a suffix expression.
    This function evaluates it and return its value.
    """
    operators = "+-*/" 
    st = ESStack()
    for x in exp:
        if not x in operators: 
            st.push(float(x))
            continue
        if st.depth() < 2: 
            raise SyntaxError("Short of operand(s).")
        a = st.pop() # second argument
        b = st.pop() # first argument
        if x == "+":
            c = b + a
        elif x == "-":
            c = b - a
        elif x == "*":
            c = b * a
        elif x == "/":
            if a == 0: raise ZeroDivisionError
            c = b / a
        else:
            pass # This branch is not possible
        st.push(c)
    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s).")
# end suf_exp_evaluator

def suffix_exp_calculator():
    """Repeatly ask for expression input until an 'end'."""
    while True:
        try:
            line = input("Suffix Expression: ")
            if line == "end":
                return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print("Error:", type(ex), ex.args)

def suffix_demo():
    print(suffix_exp_evaluator("1"))
    print(suffix_exp_evaluator("1 2 +"))
    print(suffix_exp_evaluator("1 3 + 2 *"))
    print(suffix_exp_evaluator("1 3 + 2 5 - *"))

#####################################################
##### Transform infix expression to suffix expression

priority = {"(":1, "+":3, "-":3, "*":5, "/":5}
infix_operators = "+-*/()"

def tokens(line):
    """ This function cannot deal with signed numbers,
    nor unary operators.
    """
    i, llen = 0, len(line)
    while i < llen:
        while line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:
            yield line[i]
            i += 1
            continue
        j = i + 1
        while (j < llen and not line[j].isspace() and 
               line[j] not in infix_operators):
            if ((line[j] == 'e' or line[j] == 'E') and
                j+1 < llen and line[j+1] == '-'):
                j += 1
            j += 1
        yield line[i:j]
        i = j

def trans_infix_suffix(line):
    st = SStack()
    llen = len(line)
    exp = []
    for x in tokens(line):
        if x not in infix_operators:
            exp.append(x)
        elif st.is_empty() or x == '(':
            st.push(x)
        elif x == ')':
            while not st.is_empty() and st.top() != "(":
                exp.append(st.pop())
            if st.is_empty():
                raise SyntaxError("Missing \'(\'.")
            st.pop() # discard left parethesis
        else: # consider all ops left-associative
            while (not st.is_empty() and 
                   priority[st.top()] >= priority[x]):
                exp.append(st.pop())
            st.push(x)
    while not st.is_empty():
        if st.top() == "(":
            raise SyntaxError("Extra \'(\' in expression.")
        exp.append(st.pop())
    return exp

def test_trans_infix_suffix(s):
    print(s)
    print(trans_infix_suffix(s))
    print("Value:", suf_exp_evaluator(trans_infix_suffix(s)))

def demo_trans():
    test_trans_infix_suffix("1.25")
    test_trans_infix_suffix("1 + 2")
    test_trans_infix_suffix("1 + 2 - 3")
    test_trans_infix_suffix("1 + 2 * 3")
    test_trans_infix_suffix("7. / 2 * 3")
    test_trans_infix_suffix("7.e-2/2*3")
    test_trans_infix_suffix("(1 + 2) * 3")
    test_trans_infix_suffix("1 + 2 * 3 - 5")
    test_trans_infix_suffix("13 + 2 * (3 - 5)")
    test_trans_infix_suffix("(1 + 2) * (3 - 5)")
    test_trans_infix_suffix("(1 + (2 * 3 - 5)) / .25")

if __name__ == "__main__":
    
##    check_pares("")
##    check_pares("()")
##    check_pares("([]{})")
##    check_pares("([]{}]")
##    check_pares("(abbvbb[hhh]jhg{lkii288}9000)000fhjsh")
##    check_pares("jkdsjckd(mfkk[fdjjfk],,,{kckjfc}jskdjkc]kkk")

##    suffix_exp_calculator()

    pass

