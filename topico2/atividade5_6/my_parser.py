import ply.yacc as yacc
from lex import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)


def p_expression(p):
    """expression : math_expression SEMICOL"""
    p[0] = p[1]


def p_plus(p):
    """math_expression : math_expression PLUS LPARENT math_expression RPARENT"""
    p[0] = p[1] + p[4]


def p_minus(p):
    """math_expression : math_expression MINUS LPARENT math_expression RPARENT"""
    p[0] = p[1] - p[4]


def p_times(p):
    """math_expression : math_expression TIMES LPARENT math_expression RPARENT"""
    p[0] = p[1] * p[4]


def p_divide(p):
    """math_expression : math_expression DIVIDE LPARENT math_expression RPARENT"""
    p[0] = p[1] / p[4]


def p_math_expression(p):
    """math_expression : term"""
    p[0] = p[1]


def p_term(p):
    """term : NUMBER
    """
    p[0] = p[1]


def p_error(p):
    print(p)


parser = yacc.yacc()
