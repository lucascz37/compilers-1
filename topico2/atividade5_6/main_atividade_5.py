from lex import lexer

codigo = """
    2.plus(2);
    3.plus(3);
    4.div(4);
    x <- 10;
"""

lexer.input(codigo)

while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
