from test import multiple_choice_question, short_answer_question


def main() -> None:
    multiple_choice_question(
        "Câu 1: Hàm print dùng để làm gì?",
        "Gán giá trị cho hằng",
        "In giá trị ra bảng lệnh",
        "Gán giá trị cho biến",
        "Tính toán các phép toán cơ bản",
        'b',
        "Hàm print dùng để hiển thị giá trị ra bảng lệnh (console)."
    )
    multiple_choice_question(
        "Câu 2: Cú pháp đúng để gán giá trị 10 cho biến x là gì?",
        "x == 10",
        "x: 10",
        "x = 10",
        "int x = 10",
        'c',
        "Trong Python, cú pháp gán giá trị cho biến là tên_biến = giá_trị."
    )
    multiple_choice_question(
        "Câu 3: Điều gì sẽ xảy ra khi một biến đã có giá trị mà bị gán một giá trị khác?",
        "Biến sẽ giữ lại giá trị cũ",
        "Biến sẽ mang giá trị mới và giá trị cũ bị thay thế",
        "Sẽ xảy ra lỗi do ghi đè giá trị",
        "Không có gì xảy ra",
        'b',
        "Biến sẽ mang giá trị mới, không còn mang giá trị cũ nữa."
    )
    multiple_choice_question(
        "Câu 4: Tên biến nào sau đây là hợp lệ trong Python?",
        "2nd_variable",
        "variable_name",
        "!variable",
        "first variable",
        'b',
        "Tên biến không được bắt đầu bằng số hoặc ký tự đặc biệt và không chứa dấu cách."
    )
    multiple_choice_question(
        "Câu 5: Tên biến nào sau đây không hợp lệ trong Python?",
        "myVariable",
        "variable_1",
        "None",
        "number",
        'c',
        "Tên biến không được phép trùng với các từ khóa đặc biệt như None."
    )
    multiple_choice_question(
        "Câu 6: Tại sao chúng ta không nên đặt tên biến là các từ khóa đặc biệt như return, if, case?",
        "Vì sẽ khiến tên biến khó đọc hơn",
        "Vì sẽ xảy ra lỗi khi chạy chương trình",
        "Vì biến sẽ bị ghi đè",
        "Vì không có ý nghĩa khi đọc chương trình",
        'b',
        "Các từ khóa đặc biệt đã được Python sử dụng, việc dùng chúng làm tên biến sẽ gây ra lỗi cú pháp."
    )
    multiple_choice_question(
        "Câu 7: Hằng trong Python thường được biểu diễn dưới dạng nào?",
        "Viết bằng chữ in hoa",
        "Viết bằng chữ in thường",
        "Bắt đầu bằng số",
        "Bắt đầu bằng ký tự đặc biệt",
        'a',
        "Hằng trong Python thường được biểu diễn bằng cách đặt tên biến viết hoa."
    )
    multiple_choice_question(
        "Câu 8: Câu nào sau đây diễn tả đúng về hằng trong Python?",
        "Giá trị của hằng sẽ thay đổi bất kỳ lúc nào",
        "Giá trị của hằng không bao giờ được phép thay đổi",
        "Hằng có thể bắt đầu bằng số",
        "Hằng luôn được viết bằng chữ in thường",
        'b',
        "Hằng là những giá trị không bị thay đổi trong suốt quá trình chạy chương trình."
    )
    multiple_choice_question(
        "Câu 9: Đoạn mã sau có lỗi không? Nếu có, lỗi đó là gì?\nif = 10",
        "Không có lỗi",
        "Có lỗi vì if là từ khóa đặc biệt",
        "Có lỗi vì if có ký tự đặc biệt",
        "Có lỗi vì không có dấu chấm phẩy ở cuối dòng",
        'b',
        "if là từ khóa đặc biệt, không thể dùng làm tên biến."
    )
    multiple_choice_question(
        "Câu 10: Tên biến nào sau đây không vi phạm quy tắc giữa các lập trình viên?",
        "your_variable",
        "Variable_Name",
        "This_is_a_variable",
        "VariableExample",
        'a',
        "Tên biến nên được viết bằng chữ thường."
    )
    multiple_choice_question(
        "Câu 11: Trong Python, dấu = được gọi là gì?",
        "Dấu bằng",
        "Dấu so sánh",
        "Dấu gán giá trị",
        "Dấu tương đương",
        'c',
        "Dấu = trong Python được dùng để gán giá trị cho biến."
    )
    multiple_choice_question(
        "Câu 12: Biến x được gán giá trị 5 sau đó được gán tiếp giá trị 7.\n"
        "Giá trị của x hiện tại là bao nhiêu?",
        "5",
        "7",
        "12",
        "Không xác định",
        'b',
        "Giá trị của biến x sẽ bị ghi đè thành 7."
    )
    multiple_choice_question(
        "Câu 13: Lệnh print() sau đây sẽ in ra giá trị gì?\nx = 10\nprint(x)",
        "In ra x",
        "In ra x = 10",
        "Xảy ra lỗi",
        "In ra 10",
        'd',
        "Lệnh print(x) sẽ in ra giá trị của biến x, tức là 10."
    )
    short_answer_question(
        "Câu 14: Hãy gán giá trị 37 vào biến tên n.",
        "n = 37"
    )
    multiple_choice_question(
        "Câu 15: Lệnh print(x) sẽ hiển thị cái gì nếu biến x chưa được gán giá trị?",
        "Hiển thị None",
        "Hiển thị 0",
        "Hiển thị x",
        "Xảy ra lỗi",
        'd',
        "Nếu biến x chưa được gán giá trị thì lệnh print(x) sẽ báo lỗi."
    )
    short_answer_question(
        "Câu 16: Đoạn mã sau đây sẽ in giá trị gì ra bảng lệnh?\nn = 5\nprint(n)\nn = 11",
        "5"
    )
    multiple_choice_question(
        "Câu 17: Để đánh dấu một đối tượng là hằng trong Python, ta nên:",
        "Viết tên đối tượng in hoa",
        "Gán giá trị None cho đối tượng",
        "Không bao giờ gán lại giá trị cho đối tượng",
        "Không thể đánh dấu một đối tượng là hằng trong Python",
        'a',
        "Đối tượng có tên viết in hoa được quy ước là hằng trong Python."
    )
    multiple_choice_question(
        "Câu 18: Tên nào sau đây không đúng với quy tắc đặt tên đối tượng?",
        "number_of_students",
        "number1",
        "3rd_value",
        "TOTAL_COUNT",
        'c',
        "Tên đối tượng không được bắt đầu bằng số."
    )
    multiple_choice_question(
        "Câu 19: Tên đối tượng nên được đặt bằng ngôn ngữ nào?",
        "Tiếng Việt",
        "Tiếng Hàn",
        "Tiếng Trung",
        "Tiếng Anh",
        'd',
        "Tất cả tên đối tượng đều nên được đặt bằng tiếng Anh "
        "vì tiếng Anh là ngôn ngữ thông dụng nhất trong lập trình trên toàn thế giới."
    )
    multiple_choice_question(
        "Câu 20: Tên nào dưới đây là một tên biến tốt?",
        "student_count",
        "STUDENTCOUNT",
        "sc",
        "🧑‍🎓",
        'a',
        "student_count là một tên biến chi tiết, rõ ràng, dễ đọc và phù hợp với các quy ước."
    )
    print("Chúc mừng! Bạn đã hoàn thành toàn bộ câu hỏi của bài 1! 🥳")
    

if __name__ == '__main__':
    main()