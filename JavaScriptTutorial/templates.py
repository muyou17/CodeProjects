def warning() -> None:
    input("Đây là file dùng để chứa các mẫu câu hỏi, không thể chạy được. Vui lòng chạy file quiz.py để học.")


def multiple_choice_question(index: int, question: str,
                             a: str, b: str, c: str, d: str,
                             answer: str,
                             explanation: str = '') -> None:
    print(f"\nCâu hỏi trắc nghiệm\nCâu {index}: {question}\nA. {a}\nB. {b}\nC. {c}\nD. {d}")
    while not (input("Trả lời (A/B/C/D): ").lower() == answer):
        print("Sai! Hãy thử lại.")
    print("Đúng!")
    if explanation: print(explanation)


def true_false_question(index: int, question: str, answer: str, explanation: str = '') -> None:
    print(f"\nCâu hỏi đúng/sai\nCâu {index}: {question}")
    while not (input("Trả lời (T/F): ").lower() == answer):
        print("Sai! Hãy thử lại.")
    print("Đúng!")
    if explanation: print(explanation)


def short_answer_question(index: int, question: str, answer: str, explanation: str = '') -> None:
    print(f"\nCâu hỏi tự luận\nCâu {index}: {question}")
    while not (input("Trả lời: ").strip().lower() == answer.strip().lower()):
        print("Sai! Hãy thử lại.")
    print("Đúng!")
    if explanation: print(explanation)


def checkbox_question(index: int, question: str,
                      a: str, b: str, c: str, d: str,
                      answers: set[str], explanation: str = '') -> None:
    print(f"Câu hỏi nhiều đáp án\nCâu {index}: {question}\nA. {a}\nB. {b}\nC. {c}\nD. {d}")
    while True:
        response = input("Trả lời (A/B/C/D ngăn bởi dấu cách): ").lower().split()
        if set(response) == answers:
            print("Đúng!")
            break
        print("Sai! Hãy thử lại.")
    if explanation: print(explanation)


if __name__ == '__main__':
    warning()