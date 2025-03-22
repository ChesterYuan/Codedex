import datetime, bday_messages

today = datetime.date.today()

birthday_input = input("Enter your birthday date (YYYY-MM-DD): ")

year, month, day = map(int, birthday_input.split('-'))

next_birthday = datetime.date(year, month, day)

time_difference = next_birthday - today

if time_difference == 0:
    print(random.choice(bday_messages))
else:
    print(f"Your next birthday is in {time_difference.days} days.")
