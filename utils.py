import json

def load_all():
    """
    функция загружает все данные
    """
    with open("data/data1.json", "r", encoding="utf-8") as file_all:
        return json.load(file_all)


def get_info_today(today):
    """
    функция выгружает данные за сегодняшний день
    """
    today_transp = []
    for i in load_all():
        if today == 6 or today == 7:
            if i["days"] == "ежедн." or i["days"] == "вых.":
                today_transp.append(i)
        elif 1 <= today <= 5:
            if i["days"] == "ежедн." or i["days"] == "раб.":
                today_transp.append(i)
    return today_transp


def info_by_numbers(number):
    """
    возвращает инвормация по номеру поезда или автобуса
    """
    train_number = []
    for i in load_all():
        if i["number"] == int(number):
            train_number.append(i)
    return train_number
