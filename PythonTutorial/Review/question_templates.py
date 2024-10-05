def warning() -> None:
    input("Đây là file chứa câu hỏi ôn tập, không thể chạy được. Vui lòng chạy file lesson_review.py để ôn bài.")


def multiple_choice_question(index: int, question: str,
                             a: str, b: str, c: str, d: str,
                             answer: str,
                             explanation: str = '') -> None:
    print(f"\nCâu hỏi trắc nghiệm\nCâu {index}: {question}\nA. {a}\nB. {b}\nC. {c}\nD. {d}")
    while True:
        if (response := input("Trả lời (A/B/C/D): ").lower()) == answer:
            print("Đúng!")
            break
        elif response in ('q', "quit"):
            exit(0)
        else:
            print("Sai! Hãy thử lại.")
    if explanation: print(explanation)


def true_false_question(index: int, question: str, answer: str, explanation: str = '') -> None:
    print(f"\nCâu hỏi đúng/sai\nCâu {index}: {question}")
    while True:
        if (response := input("Trả lời (T/F): ").lower()) == answer:
            print("Đúng!")
            break
        elif response in ('q', "quit"):
            exit(0)
        else:
            print("Sai! Hãy thử lại.")
    if explanation: print(explanation)


def short_answer_question(index: int, question: str, answer: str, explanation: str = '') -> None:
    print(f"\nCâu hỏi tự luận\nCâu {index}: {question}")
    while True:
        if (response := input("Trả lời: ").strip()) == answer:
            print("Đúng!")
            break
        elif response in ('q', "quit"):
            exit(0)
        else:
            print("Sai! Hãy thử lại.")
    if explanation: print(explanation)


def checkbox_question(index: int, question: str,
                      a: str, b: str, c: str, d: str,
                      answers: set[str], explanation: str = '') -> None:
    print(f"\nCâu hỏi nhiều đáp án\nSố đáp án đúng: {len(answers)}\n"
          f"\nCâu {index}: {question}\nA. {a}\nB. {b}\nC. {c}\nD. {d}")
    while True:
        if set(response := input("Trả lời (A/B/C/D): ").lower().split()) == answer:
            print("Đúng!")
            break
        elif response & {'q', "quit"}:
            exit(0)
        else:
            print("Sai! Hãy thử lại.")
    if explanation: print(explanation)


if __name__ == '__main__':
    warning()