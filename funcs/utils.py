import json
from datetime import datetime


def load_operations():
    with open("operations.json", "r", encoding="utf-8") as file:
        operations_pyth = json.load(file)
        return operations_pyth


def sorted_operations():
    clear_list = []
    all_operat = load_operations()
    for operat in all_operat:
        if operat != {}:
            clear_list.append(operat)
            sorted_list = sorted(clear_list, key=lambda d: d["date"], reverse=True)
    return sorted_list


def new_time_format(num):
    time = datetime.strptime(sorted_operations()[num]["date"], "%Y-%m-%dT%H:%M:%S.%f")
    new_struct_time = time.strftime(("%d.%m.%Y"))
    return new_struct_time


def censored_sender(num):
    if "from" in sorted_operations()[num]:
        if "Счет" not in sorted_operations()[num]["from"]:
            a = sorted_operations()[num]['from'].split(" ")
            if len(a) > 2:
                card_inf = (a[0] + " " + a[1], a[2][:4] + " " + a[2][4:6] + "** **** " + a[2][12:len(a[2])], "->")
                card_inf = " ".join(card_inf)
                return card_inf
            else:
                card_inf = (a[0], a[1][:4] + " " + a[1][4:6] + "** **** " + a[1][12:len(a[1])], "->")
                card_inf = " ".join(card_inf)
                return card_inf
        else:
            a = sorted_operations()[num]['from'].split(" ")
            card_inf = (a[0], "**" + a[1][-4:len(a[1])], "->")
            card_inf = " ".join(card_inf)
            return card_inf
    else:
        return "На"


def cencored_addressee(num):
    if "Счет" not in sorted_operations()[num]["to"]:
        a = sorted_operations()[num]['to'].split(" ")
        if len(a) > 2:
            card_inf = (a[0] + " " + a[1], a[2][:4] + " " + a[2][4:6] + "** **** " + a[2][12:len(a[2])])
            card_inf = " ".join(card_inf)
            return card_inf
        else:
            card_inf = (a[0], a[1][:4] + " " + a[1][4:6] + "** **** " + a[1][12:len(a[1])])
            card_inf = " ".join(card_inf)
            return card_inf
    else:
        a = sorted_operations()[num]['to'].split(" ")
        card_inf = (a[0], "**" + a[1][-4:len(a[1])])
        card_inf = " ".join(card_inf)
        return card_inf
