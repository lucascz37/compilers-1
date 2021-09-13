from main import toInt


def convert_int_to_string(input: int):
    dict_list = {1: "1", 2: "2", 3: "3", 4: "4", 5:
                 "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0"}

    converted_string = ''

    break_condition = True
    rest_by = 1
    while break_condition:
        rest = (input % (rest_by * 10)) // rest_by
        if rest != None and input // rest_by > 0:
            converted_string = dict_list.get(rest) + converted_string
            rest_by *= 10
        else:
            break_condition = False

    return converted_string


def split(input: str):
    arr = []

    word = ""
    for letter in input:
        if letter != " ":
            word += letter
        else:
            arr.append(word)
            word = ""

    if len(word) > 0:
        arr.append(word)

    return arr


def convert_letter(input: str):
    new_string = ""

    for l in input:
        if l == 'a':
            new_string += 'o'
        elif l == 'A':
            new_string += 'O'
        else:
            new_string += l

    return new_string


def put_letter(input: str):
    new_string = ""

    phrase_len = len(input) - 1
    for index, l in enumerate(input):
        if l in ['o', 'O']:
            if index == phrase_len or input[index+1] == " ":
                new_string += l
                new_string += 's'
            else:
                new_string += l
        else:
            new_string += l

    return new_string


def increment_number_on_string(input: str):
    new_string = ""

    phrase_len = len(input)

    for index, l in enumerate(input):
        if index == len(new_string):
            if l.isdigit():
                number = l
                for n in range(index + 1, phrase_len):
                    next_number = input[n]
                    if next_number.isdigit():
                        number = number + next_number
                    else:
                        break
                new_string += convert_int_to_string(toInt(number) + 1)
            else:
                new_string += l

    return new_string


print(convert_int_to_string(12123124124))
print(split("Hello there Lucas"))
print(convert_letter("Hello there I would like a ice cream please"))
print(put_letter("Heollo this phrase finiosh with the letter o and O"))
print(increment_number_on_string(
    "Hello again for the 4° time in a row and some random number 123892138 and one in the mi235ddle"))
