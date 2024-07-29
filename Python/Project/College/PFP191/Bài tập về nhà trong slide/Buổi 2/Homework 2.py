print("INPUT:")
month: int = int(input("Month: "))

match month:
    case 2:
        days: int = 28
        year: int = int(input("Year: "))
        if not (not year % 400 or not year % 4 and year % 100):
            days += 1
    case 4 | 6 | 9 | 11:
        days: int = 30
    case _:
        days: int = 31

print("\nOUTPUT:")
print(days)