import random


def print_title_and_guide() -> None:
    print("Trò chơi Búa Kéo Bao", end='\n\n')
    print("Chương trình sẽ chạy lặp lại liên tục.",
          "Hướng dẫn cách chơi:",
          "- Nhập R để chọn búa.",
          "- Nhập S để chọn kéo.",
          "- Nhập P để chọn bao.",
          "- Nhập Q để dừng chương trình.",
          sep='\n', end='\n\n')


def get_choices() -> tuple[str, str]:
    options = ('R', 'P', 'S')
    player_choice = input("Nhập lựa chọn (R/P/S): ").upper()
    if player_choice == 'Q': exit(0)
    elif player_choice not in options:
        print("Lựa chọn không hợp lệ.")
        player_choice = ''
    return player_choice, random.choice(options)


def compute_result(player_choice: str, computer_choice: str, ratio: dict[str, int]) -> None:
    if player_choice == 'R' and computer_choice == 'S'\
    or player_choice == 'P' and computer_choice == 'R'\
    or player_choice == 'S' and computer_choice == 'P':
        print("Bạn thắng!")
        ratio['player'] += 1
    elif player_choice != computer_choice:
        print("Máy thắng!")
        ratio['computer'] += 1
    else: print("Hòa.")


def run_game() -> None:
    ratio = {'player': 0, 'computer': 0}
    options = {'R': "Búa",'S': "Kéo",'P': "Bao"}
    while True:
        player_choice, computer_choice = get_choices()
        if not player_choice: continue
        print(f"Lựa chọn của máy: {options[computer_choice]}")
        print(f"Lựa chọn của bạn: {options[player_choice]}")
        compute_result(player_choice, computer_choice, ratio)
        print(f"Tỷ số hiện tại: {ratio['player']}-{ratio['computer']}", end='\n\n')


if __name__ == '__main__':
    print_title_and_guide()
    run_game()