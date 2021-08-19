def verify_email(email):
    prefix = True
    domain = False
    post_domain = False
    post_domain_size = 0
    last_symbol = ""

    if email[0] in ['.', '-', '#']:
        return False

    for c in list(email[1:]):

        if prefix:

            if c.isalnum():
                last_symbol = ""
                continue
            elif c in ['.', '-', '_'] and c != last_symbol:
                last_symbol = c
            elif c == '@' and last_symbol == "":
                prefix = False
                domain = True
                continue
            else:
                print(c, 'is invalid')
                return False

        elif domain:
            if c == '.':
                domain = False
                post_domain = True
            elif c.isalnum() or c == '-':
                continue
            else:
                return False
        elif post_domain:
            if c.isalnum():
                post_domain_size += 1
            elif c == '.':
                return False

    if post_domain_size >= 2:
        return True
    else:
        return False


def toInt(string_value):
    value = 0
    length = len(string_value) - 1
    dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    for c in string_value:
        if c.isdigit():
            value += (10 ** length) * dict.get(c)
            length -= 1
        else:
            raise ValueError("{} is not a digit".format(c))

    return value


def verify_date(data):
    data = data.split("/")
    quant_dias = {"01": 31, "02": 0, "03": 31, "04": 30, "05": 31,
                  "06": 30, "07": 31, "08": 31, "09": 30, "10": 31, "11": 30, "12": 31}

    if len(data) == 3:
        for d in data:
            if len(d) == 2 and d.isdigit():
                pass
            else:
                return False
        if data[1] == '02':
            year = toInt(data[2])
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        quant_dias.update({"02": 29})
                    else:
                        quant_dias.update({"02": 28})
                else:
                    quant_dias.update({"02": 29})
            else:
                quant_dias.update({"02": 28})

        if toInt(data[0]) <= quant_dias.get(data[1]):
            return True
    else:
        return False
