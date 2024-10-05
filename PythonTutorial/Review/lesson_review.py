def main() -> None:
    while review_questions:
        choice = input("Chọn bài (1-3): ")
        try:
            if 1 <= int(choice) <= 3: break
            else: raise ValueError
        except ValueError:
            print("Input không hợp lệ. Chỉ được phép nhập số nguyên từ 1 đến 3.", end='\n\n')
    eval(f'review_questions.lesson_{choice}()')
    input("Nhấn Enter để thoát chương trình.")


if __name__ == '__main__':
    try:
        import review_questions
    except ImportError:
        input("Lỗi! Không tìm được file review_questions.py.")
        exit(1)
    main()