from datetime import datetime


def get_user_birth_year(current_year: int) -> int:
    while True:
        user_birth_year = input("Enter your year of birth: ")
        try:
            year_of_birth = int(user_birth_year)
            if not year_of_birth in range(1900, current_year + 1):
                raise ValueError
            return year_of_birth
        except ValueError:
            print("Invalid year!", end="\n\n")


def get_user_age_group(user_age: int) -> str:
    match [user_age >= age for age in (51, 36, 18, 7, 0)].index(True):
        case 0:
            return "Elderly"
        case 1:
            return "Middle-Aged"
        case 2:
            return "Young Adult"
        case 3:
            return "Adolescent"
        case 4:
            return "Child"


def years_until_elderly(age: int) -> int:
    return 51 - age if age < 51 else 0


def main() -> None:
    print("INPUT:")
    year_of_birth = get_user_birth_year(current_year := datetime.today().year)
    age_group = get_user_age_group(age := current_year - year_of_birth)

    print("\nOUTPUT:")
    print(f"Your birth year: {year_of_birth}",
          f"Your age: {age}",
          f"Your age group: {age_group}",
          f"Years until you become elderly: {years_until_elderly(age)}",
          sep="\n")


if __name__ == "__main__":
    main()