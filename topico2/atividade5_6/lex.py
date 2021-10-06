import ply.lex as lex

tokens = (
    "ATRIBUTION",
    "SEMICOL",
    "LPARENT",
    "RPARENT",
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE"
)

t_ATRIBUTION = r'\w+\s+(<-)\s+\w+'
t_SEMICOL = r"\;"
t_LPARENT = r"\("
t_RPARENT = r"\)"
t_PLUS = r".plus"
t_MINUS = r".minus"
t_TIMES = r".mult"
t_DIVIDE = r".div"


def t_NUMBER(t):
    r'[0-9]+(.[0-9]+)?'

    if "." in t.value:
        t.value = float(t.value)
        return t

    t.value = int(t.value)
    return t


t_ignore = ' \n\t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
