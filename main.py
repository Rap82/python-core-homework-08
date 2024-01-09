"""Імпортуємо з бібліотеки datetime функції date, datetime ,timedelta"""
from datetime import date, datetime ,timedelta


WEEKEND = ['Saturday', 'Sunday']


def range_from_12_26_to_01_01():
    """Функція що генерує і повертає згенерований список datetime обєктів у вкащаному діпазоні."""

    start_date = datetime(year=date.today().year, month=12, day=26).date()
    template_dict = [
        current_date for current_date in (start_date + timedelta(days=i) for i in range(6))
        ]
    return template_dict

def range_from_01_01_to_01_07():
    """Функція що генерує і повертає згенерований список datetime обєктів у вкащаному діпазоні."""
    start_date = datetime(year=date.today().year, month=1, day=1).date()

    template_dict = [
        current_date for current_date in (start_date + timedelta(days=i) for i in range(7))
        ]

    return template_dict

def sort_birthdate(employees_birthdays):
    """Перевіряє чи передані дні народження відповідають вимогам завдання \
    і повертає список тих з них які відповідають."""
    future_birthdays_list = []

    current_date = date.today()
    for birthday_dict in employees_birthdays:

        birthday_dict["birthday"] = datetime(year=current_date.year,
                                             month=birthday_dict["birthday"].month,
                                             day=birthday_dict["birthday"].day).date()
        if current_date in range_from_12_26_to_01_01():
            if birthday_dict["birthday"] in range_from_01_01_to_01_07():
                birthday_dict["birthday"] = datetime(year=(current_date.year + 1),
                                                     month=birthday_dict["birthday"].month,
                                                     day=birthday_dict["birthday"].day).date()
        if (current_date + timedelta(days=7)) > birthday_dict["birthday"] >= current_date:
            future_birthdays_list.append(birthday_dict)

    return future_birthdays_list

def format_birthdays(sort_birthdays):
    """Функція в якій форматуємо дані згідно вимог"""

    format_birthdays_list = []
    for birth in sort_birthdays:

        format_birthdays_dict = {}
        if birth["birthday"].strftime('%A') in WEEKEND:

            format_birthdays_dict['Monday'] = birth["name"].split(' ')[0]
        else :
            format_birthdays_dict[birth["birthday"].strftime('%A')] = birth["name"].split(' ')[0]
        format_birthdays_list.append(format_birthdays_dict)
    return format_birthdays_list

def get_birthdays_per_week(employees):
    """Функція в якій відформатовані дані сортуємо по потрібних днях \
     і повертаємо кінцевий результат"""
    empty_list = []
    list_mon = []

    list_tue = []

    list_wend = []

    list_thu = []

    list_fri = []

    birthdays_per_week_dict = {}

    if employees == []:
        return {}
    elif sort_birthdate(employees) == empty_list:
        return {}
    sort_birthdays = sort_birthdate(employees)

    list_birthdays_per_week = format_birthdays(sort_birthdays)

    for user in list_birthdays_per_week:
        match list(iter(user))[0]:

            case 'Monday':

                list_mon.append(user.get('Monday'))
            case 'Tuesday':
                list_tue.append(user.get('Tuesday'))
            case 'Wednesday':
                list_wend.append(user.get('Wednesday'))

            case 'Thursday':
                list_thu.append(user.get('Thursday'))
            case 'Friday':
                list_fri.append(user.get('Friday'))

    if list_mon != empty_list:
        birthdays_per_week_dict['Monday'] = list_mon

    if list_tue != empty_list:
        birthdays_per_week_dict['Tuesday'] = list_tue

    if list_wend != empty_list:

        birthdays_per_week_dict['Wednesday'] = list_wend

    if list_thu != empty_list:
        birthdays_per_week_dict['Thursday'] = list_thu
    if list_fri != empty_list:

        birthdays_per_week_dict['Friday'] = list_fri
    return birthdays_per_week_dict

# Цей запис був в початковому коді . Не міняв його .
if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
