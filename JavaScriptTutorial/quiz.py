from lessons import lesson_1


def main() -> None:
    lessons = lesson_1,
    lesson_names = "Bài 1: Biến, Hằng và Hàm console.log",
    for lesson in lesson_names:
        print(lesson)
    while True:
        choice = input("\nChọn bài học (nhập số 1): ")
        try:
            if choice := int(choice) - 1 != 0:
                raise ValueError
            break
        except ValueError:
            print("Lỗi! Chỉ được nhập số 1.")
    lessons[choice]()


if __name__ == '__main__':
    main()