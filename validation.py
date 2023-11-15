import re
from datetime import datetime
from db import db


def validate_date(date):
    """
    Проверяет, является ли строка датой в одном из поддерживаемых форматов.

    Args:
        date (str): Строка, предположительно содержащая дату.

    Returns:
        datetime or None: Возвращает объект datetime, если строка соответствует
        хотя бы одному из форматов, иначе возвращает None.
    """
    date_formats = ['%d.%m.%Y', '%Y-%m-%d']
    for format in date_formats:
        try:
            return datetime.strptime(date, format)
        except ValueError:
            pass
    return None

def validate_phone(phone):
    """
    Проверяет, соответствует ли строка номеру телефона одного из поддерживаемых форматов.

    Args:
        phone (str): Строка, предположительно содержащая номер телефона.

    Returns:
        bool: True, если строка соответствует хотя бы одному из форматов, иначе False.
    """
    pattern1 = re.compile(r'^\+\d{11}$')
    pattern2 = re.compile(r'^\+\d{1,2}\s\d{3}\s\d{3}\s\d{2}\s\d{2}$')

    return pattern1.match(phone) is not None or pattern2.match(phone) is not None

def validate_email(email):
    """
    Проверяет, соответствует ли строка формату электронной почты.

    Args:
        email (str): Строка, предположительно содержащая адрес электронной почты.

    Returns:
        bool: True, если строка соответствует формату электронной почты, иначе False.
    """
    pattern = re.compile(r'^\S+@\S+\.\S+$')
    return pattern.match(email) is not None

def get_field_type(value):
    """
    Определяет тип поля (дата, телефон, электронная почта или текст) на основе значения.

    Args:
        value: Значение поля.

    Returns:
        str: Тип поля ("date", "phone", "email" или "text").
    """
    if validate_date(value):
        return "date"
    elif validate_phone(value):
        return "phone"
    elif validate_email(value):
        return "email"
    else:
        return "text"

def find_matching_template(data):
    """
    Находит подходящий шаблон на основе данных.

    Args:
        data (dict): Словарь данных для сопоставления с шаблонами.

    Returns:
        str or dict: Имя подходящего шаблона, если найден, или словарь с типами полей.
    """
    for template in db:
        template_fields = set(template.keys()) - {"name"}
        data_fields = set(data.keys())
        if template_fields.issubset(data_fields):
            matching = all(template[field] == get_field_type(data[field]) for field in template_fields)
            if matching:
                return template["name"]

    return {field: get_field_type(data[field]) for field in data}