# Nhập vào module random để sử dụng
import random


# Tiêu đề
print("Trò chơi Búa Kéo Bao", end='\n\n')
    
# Hướng dẫn
print("Chương trình sẽ chạy lặp lại liên tục.",
      "Hướng dẫn cách chơi:",
      "- Nhập R để chọn búa.",
      "- Nhập S để chọn kéo.",
      "- Nhập P để chọn bao.",
      "- Nhập Q để dừng chương trình.",
      sep='\n', end='\n\n')
    
# dict chứa tỷ số
ratio = {'player': 0, 'computer': 0}
# dict chứa các lựa chọn
options = {'R': "Búa",'S': "Kéo",'P': "Bao"}
    
# Phần trò chơi chính, nằm trong khối lệnh while lặp vĩnh viễn
while True:
    # Lựa chọn của người chơi
    player_choice = input("Nhập lựa chọn (R/P/S): ").upper()
        
    # Kiểm tra xem lựa chọn có hợp lệ hay không
    if player_choice == 'Q':
        exit(0)
    elif player_choice not in options:
        print("Lựa chọn không hợp lệ.", end='\n\n')
        continue

    # Lựa chọn ngẫu nhiên của máy
    computer_choice = random.choice(tuple(options))
        
    # In ra các lựa chọn
    print(f"Lựa chọn của máy: {options[computer_choice]}")
    print(f"Lựa chọn của bạn: {options[player_choice]}")
        
    # Xử lý kết quả
    if player_choice == 'R' and computer_choice == 'S'\
    or player_choice == 'P' and computer_choice == 'R'\
    or player_choice == 'S' and computer_choice == 'P':
        print("Bạn thắng!")
        ratio['player'] += 1
    elif player_choice != computer_choice:
        print("Máy thắng!")
        ratio['computer'] += 1
    else: print("Hòa.")

    # In tỷ số hiện tại
    print(f"Tỷ số hiện tại: {ratio['player']}-{ratio['computer']}", end='\n\n')


if __name__ == '__main__':
    main()