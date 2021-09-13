import re


def function_1(input):
    return re.findall(r'\w+', input)


def function_2(input):
    return re.sub(r'a', 'o', input)


def function_3(input):
    return re.sub(r'(\w)\b', r'\1s', input)


def function_4(input):
    return re.sub(r'[0-9]+', lambda x: str(int(x.group()) + 1), input)


def function_5(input):
    return re.findall(r'[0-9]+\.[0-9]+', input)


def function_6(input):
    return re.findall(r'^<.+>$', input)


def function_7(input):
    return re.findall(r'\/\*.*\*\/', input)


def function_8(input):
    return re.sub(r'(\w+)\:\s(\w+)', r'\g<2>: \g<1>', input)

# 9 Não entendi a lógica de usar regex nessa questão

# 10 Não tem sentido usar regex para esse tipo de verificação https://stackoverflow.com/questions/546433/regular-expression-to-match-balanced-parentheses


def function_10(input):
    return len(re.findall(r'\(', input)) == len(re.findall(r'\)', input))


def function_11(input):
    return len(re.findall(r'a', input)) % 2 != 0


print(function_1("Hello World in another planet"))

print(function_2("replace the letter a by o"))

print(function_3("add s to words endings"))

print(function_4("add 1 to numb3rs 2819 23123"))

print(function_5("return decimal number 2.5 2.643 2.324 901238.123123 129308 1293082 120-33"))

# with open("test.html") as f:
#    for line in f:
#        print(function_6(line))

print(function_7("Teste comment /* helo mam */"))

print(function_8("Key1: 11224 \nKey2: 524 \nKey3: 5125 \nAbc: 51252"))

print(function_10("(helo(ashelkhs( iasodo( aslkdjasçkldj)asdasd ) asd) asdas)"))

print(function_11("number of the letter a is odd in this phrase I suposse alright? a"))
