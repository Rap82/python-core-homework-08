#++++++++++++++  Тестові записи коду інформація для себе. ++++++++++

# # Якщо цікавить автоматичне створення, то можна зробити наступним чином, тільки коду буде більше

# from datetime import datetime, timedelta
# from collections import defaultdict

# # Визначаємо початкову дату
# start_date = datetime(2023, 1, 1)

# # Створюємо словник зі списками за замовчуванням
# template_dict = defaultdict(list)
# print(template_dict)

# # Додаємо ключі для кожного дня тижня для наступного тижня
# for i in range(7):
#     current_date = start_date + timedelta(days=i)
#     day_of_week = current_date.strftime('%A')  # Отримуємо назву дня тижня
#     template_dict[day_of_week]
#     print(template_dict)

# # Виводимо результат
# print(dict(template_dict))

# # Або використай datetime, dict comprehension
# start_date = datetime(2023, 1, 1)
# # Створюємо словник зі списками за замовчуванням за допомогою dict comprehension
# template_dict = {current_date.strftime('%A'): [] for current_date in (start_date + timedelta(days=i) for i in range(7))}

from datetime import datetime, timedelta, date


WEEKEND = ['Saturday', 'Sunday']


def range_from_12_26_to_01_01():

    start_date = datetime(year=date.today().year, month=12, day=26).date()

    template_dict = [current_date for current_date in (start_date + timedelta(days=i) for i in range(6))]

    return template_dict

def range_from_01_01_to_01_07():

    start_date = datetime(year=date.today().year, month=1, day=1).date()

    template_dict = [current_date for current_date in (start_date + timedelta(days=i) for i in range(7))]

    return template_dict

def sort_birthdate(users):

    future_вirthday_list = []

    current_date = date.today()
    
    for вirthday_dict in users:

        if вirthday_dict["birthday"].year == current_date.year:

            pass

        else :
            вirthday_dict["birthday"] = datetime(year=current_date.year, 
                                                 month=вirthday_dict["birthday"].month, 
                                                 day=вirthday_dict["birthday"].day).date()
        
        if current_date in range_from_12_26_to_01_01():  

            if вirthday_dict["birthday"] in range_from_01_01_to_01_07():
               
                вirthday_dict["birthday"] = datetime(year=(current_date.year + 1), 
                                                     month=вirthday_dict["birthday"].month, 
                                                     day=вirthday_dict["birthday"].day).date()
             
        if (current_date + timedelta(days=7)) > вirthday_dict["birthday"] >= current_date:
                
                future_вirthday_list.append(вirthday_dict)
   
    return future_вirthday_list

def format_birthdays(sort_birthdays):

    format_birthdays_list = []
    
    for birth in sort_birthdays:

        format_birthdays_dict = {}
        
        if birth["birthday"].strftime('%A') in WEEKEND:

            format_birthdays_dict[birth["birthday"].strftime('%A')] = birth["name"].split(' ')[0]

            format_birthdays_dict['Monday'] = format_birthdays_dict.pop(birth["birthday"].strftime('%A'))
            
        else :
      
            format_birthdays_dict[birth["birthday"].strftime('%A')] = birth["name"].split(' ')[0]
                   
        format_birthdays_list.append(format_birthdays_dict)
        
    return format_birthdays_list
  

def get_birthdays_per_week(users):

    list_mon = []

    list_tue = []

    list_wend = []

    list_thu = []

    list_fri = []

    birthdays_per_week_dict = {}

    if users == []: # Якщо список пустий відразу - повертаємо пустий словник {}
        
        return {}   # Тест 1 пройдено.
        
    elif sort_birthdate(users) == []: # Cписок пустий коли всі дні народження вже минули у цьому році

        return {}    # Тест 2 пройдено.
    
    sort_birthdays = sort_birthdate(users)

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
            

    if list_mon != []: 

        birthdays_per_week_dict['Monday'] = list_mon

    if list_tue != []:
        
        birthdays_per_week_dict['Tuesday'] = list_tue

    if list_wend != []:

        birthdays_per_week_dict['Wednesday'] = list_wend

    if list_thu != []: 
       
        birthdays_per_week_dict['Thursday'] = list_thu 

    if list_fri != []:

        birthdays_per_week_dict['Friday'] = list_fri
   
    users = birthdays_per_week_dict
    
    return users



users =[{'name': 'John', 'birthday': datetime(2023, 12, 30).date()}, 
        {'name': 'Doe', 'birthday': datetime(2022, 1, 1).date()}, 
        {'name': 'Alice', 'birthday': datetime(2020, 1, 29).date()},
        {"name": "Ylia Voda", "birthday": datetime(2017, 1, 6).date()},
        {"name": "Lesia Prad", "birthday": datetime(1999, 12, 31).date()},
        {"name": "Roman Koval", "birthday": datetime(2021, 1 , 6).date()}
        ]
# print(sort_birthdate(users))
print(get_birthdays_per_week(users))
# print(range_12_26_01_01 ()  )
current_date = date.today()
print (current_date)
print (iter(users))