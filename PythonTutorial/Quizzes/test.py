def multiple_choice_question(question: str,
                             a: str, b: str, c: str, d: str,
                             answer: str,
                             explanation: str = '') -> None:
    print(f"{question}\nA. {a}\nB. {b}\nC. {c}\nD. {d}")
    while not (input("Trả lời: ").lower() == answer):
        print("Sai!")
    print("Đúng!")
    print(explanation, end='\n\n') if explanation else print()


def short_answer_question(question: str, answer: str) -> None:
    print("Câu hỏi tự luận", question, sep='\n')
    while not (input("Trả lời: ") == answer):
        print("Sai!")
    print("Đúng!", end='\n\n')