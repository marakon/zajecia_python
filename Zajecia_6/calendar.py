data = [
    ('January', range(1,32)),
    ('February', range(1,29)),
    ('March', range(1,32)),
    ('April', range(1,31)),
    ('May', range(1,32)),
    ('June', range(1,31)),
    ('July', range(1,32)),
    ('August', range(1,32)),
    ('September', range(1,31)),
    ('October', range(1,32)),
    ('November', range(1,31)),
    ('December', range(1,32)),
    ]

def print_calendar(data):
    start_day = 0
    for month, days in data:
        print('\n')
        print(month)
        print('{0:<4}'.format('')*start_day, end = '')
        start_day = print_week(days, start_day)

def print_week(days, start_day):
    for day in days:
        print('{0:<4}'.format(day), end = '')
        start_day += 1
        start_day = sunday_reset(start_day) if start_day == 7 else start_day
    return start_day

def sunday_reset(start_day):
    print()
    start_day = 0
    return start_day

print_calendar(data)
