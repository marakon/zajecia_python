day = 24 * 60
week = day * 7
seven_weeks = week * 7
print(str(seven_weeks) + '\n')

hours_per_week = int(input("How many hours per week?: "))
hour_to_know = 75
will_know = hour_to_know // hours_per_week
print("You will learn it within ", will_know ," weeks.")
