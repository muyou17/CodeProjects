from collections.abc import Iterator
from itertools import cycle
from datetime import date, timedelta
from calendar import month, monthrange, weekday, weekheader


def schedule(worker: Iterator[str], year: int, month_number: int) -> str:
    """Lịch trực trong tháng."""

    # Di con trỏ của worker đến nhân viên trực cuối tháng trước
    current_day: date = date(year, 1, 1)
    # Tính số ngày từ đầu năm đến đầu tháng
    days_since_start: int = (date(year, month_number, 1) - current_day).days
    # Chạy từ đầu năm đến cuối tháng trước
    for day in range(days_since_start - 2):
        # Xét ngày tiếp theo
        current_day += timedelta(days=1)
        # Nếu không phải chủ nhật thì xét nhân viên tiếp theo
        if current_day.weekday() != 6:
            next(worker)

    # Lịch tháng
    month_calendar: str = month(year, month_number, 7)
    # Bỏ header để lấy các dòng ngày
    month_calendar = month_calendar[month_calendar.index("Sun") + 4:]
    # Duyệt qua từng ngày trong tháng
    for day in range(1, monthrange(year, month_number)[1] + 1):
        # Thêm tên nhân viên vào các ngày trong tuần
        if weekday(year, month_number, day) != 6:
            month_calendar = month_calendar.replace(str(day), f'{day} {next(worker)}', 1)
        # Nếu là chủ nhật thì không ai trực nên thêm N
        else:
            month_calendar = month_calendar.replace(str(day), f'{day} N', 1)

    # Nếu ngày đầu tiên của tháng không phải là thứ hai thì cần pad dòng đầu về đúng độ dài
    first_line: str = month_calendar[:month_calendar.index('\n')]
    if len(first_line) != 67:
        month_calendar = month_calendar.replace(first_line, first_line.rjust(65))

    # Thêm header vào lại và trả về lịch trực
    return weekheader(9) + '\n' + month_calendar


def main() -> None:
    # Các nhân viên
    worker: Iterator[str] = cycle('ABCDE')

    print("INPUT:")
    # Nhập năm
    year: int = int(input("Year: "))
    # Nhập tháng
    month_number: int = int(input("Month: "))

    print("\nOUTPUT:")
    # In lịch trực
    print(schedule(worker, year, month_number))


if __name__ == '__main__':
    main()