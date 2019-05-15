hours_per_week = int(input("How many hours per week?: "))

def count_weeks(hours_per_week):
    hour_to_know = 75
    will_know = hour_to_know // hours_per_week
    return will_know

print("You will learn it within ", count_weeks(hours_per_week) ," weeks.")



