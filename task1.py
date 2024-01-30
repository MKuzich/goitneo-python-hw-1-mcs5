from datetime import datetime
from collections import defaultdict

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Bill Gates", "birthday": datetime(1955, 1, 29)},
    {"name": "Maxsssss Gates", "birthday": datetime(1955, 2, 3)},
    {"name": "Maxxx Gates", "birthday": datetime(1955, 1, 30)},
    {"name": "Max Gates", "birthday": datetime(1955, 2, 2)},
    {"name": "Maxsdsa Gates", "birthday": datetime(1955, 2, 4)},
    {"name": "Max Gates", "birthday": datetime(1955, 2, 4)},
    {"name": "BUG", "birthday": datetime(1955, 2, 6)}
]

def get_birthdays_per_week(users):
    today = datetime.now().date()
    birthdays = defaultdict(list)

    def sort_by_date(user):
        return user['birthday'].date()
    users.sort(key=sort_by_date)
    
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            if birthday_this_year.weekday() > 4: 
                if today.weekday() != 0:
                    birthdays['Monday'].append(name)
            else:
                birthdays[birthday_this_year.strftime('%A')].append(name)


    for key, val in birthdays.items():
        print(f'{key}: {", ".join(val)}')

get_birthdays_per_week(users)