import json
from datetime import datetime


def load_operations(file):
    """
    Читает json файл, преобразует в pyth список словарей
    :return pyth список словарей
    """
    with open(file, "r", encoding="utf-8") as f:
        operations_pyth = json.load(f)
        return operations_pyth


def sorted_operations(file):
    """
    Сортирует lstdir по дате выполнения операции, проверяет элемент на пустой ячейку
    :return: отсортированный список словарей
    """
    clear_list = []
    all_operat = load_operations(file)
    for operat in all_operat:
        if operat != {}:
            clear_list.append(operat)
            sorted_list = sorted(clear_list, key=lambda d: d["date"], reverse=True)
    return sorted_list


def new_time_format(file, num):
    """
    Принимает значение от ключа ["date"] преобразует строку в формат datetime, после преобразует его в нужный формат вывода
    :param num: номер элемента в спике словарей
    :return: время в формате datetime
    """
    time = datetime.strptime(sorted_operations(file)[num]["date"], "%Y-%m-%dT%H:%M:%S.%f")
    new_struct_time = time.strftime(("%d.%m.%Y"))
    return new_struct_time


def censored_sender(file, num):
    """
    Принимает значение по ключу ["from"], выполняет деление на "Счет" и на карту
    После делит строку на элементы в список, проверяет на количество элементов и соединяет в необходимый вид
    :param num: номер элемента в спике словарей
    :return: вид карты/счет, зацензуренный номер карты или счета отправителя
    """
    if "from" in sorted_operations(file)[num]:
        if "Счет" not in sorted_operations(file)[num]["from"]:
            a = sorted_operations(file)[num]['from'].split(" ")
            if len(a) > 2:
                card_inf = (a[0] + " " + a[1], a[2][:4] + " " + a[2][4:6] + "** **** " + a[2][12:len(a[2])], "->")
                card_inf = " ".join(card_inf)
                return card_inf
            else:
                card_inf = (a[0], a[1][:4] + " " + a[1][4:6] + "** **** " + a[1][12:len(a[1])], "->")
                card_inf = " ".join(card_inf)
                return card_inf
        else:
            a = sorted_operations(file)[num]['from'].split(" ")
            card_inf = (a[0], "**" + a[1][-4:len(a[1])], "->")
            card_inf = " ".join(card_inf)
            return card_inf
    else:
        return "На"


def cencored_addressee(file, num):
    """
    Принимает значение по ключу ["to"]
    После делит строку на элементы в список, проверяет на количество элементов и соединяет в необходимый вид
    :param num: номер элемента в спике словарей
    :return: вид карты/счет, зацензуренный номер карты или счета получателя
    """
    if "Счет" not in sorted_operations(file)[num]["to"]:
        a = sorted_operations(file)[num]['to'].split(" ")
        if len(a) > 2:
            card_inf = (a[0] + " " + a[1], a[2][:4] + " " + a[2][4:6] + "** **** " + a[2][12:len(a[2])])
            card_inf = " ".join(card_inf)
            return card_inf
        else:
            card_inf = (a[0], a[1][:4] + " " + a[1][4:6] + "** **** " + a[1][12:len(a[1])])
            card_inf = " ".join(card_inf)
            return card_inf
    else:
        a = sorted_operations(file)[num]['to'].split(" ")
        card_inf = (a[0], "**" + a[1][-4:len(a[1])])
        card_inf = " ".join(card_inf)
        return card_inf
