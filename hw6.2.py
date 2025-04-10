secs_input = int(input("Enter a seconds amount from 0 to 8640000:"))

if 0 <= secs_input < 8640000:
    days, rest = divmod(secs_input, 24 * 60 * 60)
    hours, rest = divmod(rest, 60 * 60)
    mins, seconds = divmod(rest, 60)
    if days == 1:
        day_word = "day"
    elif 2 <= days % 10 <= 4 and not 12 <= days % 100 <= 14:
        day_word = "day"
    elif days % 10 == 1 and days % 100 != 11:
        day_word = "day"
    else:
        day_word = "days"
    time_string = f"{str(hours).zfill(2)}:{str(mins).zfill(2)}:{str(seconds).zfill(2)}"
    print(f"{days} {day_word}, {time_string}")
else:
    print("Error: number should be from 0 to 8640000")
