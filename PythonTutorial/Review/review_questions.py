try:
    import question_templates
except ImportError:
    input("Lỗi! Không tìm được file question_templates.py")
    exit(1)


def warning() -> None:
    input("Đây là file chứa mẫu câu hỏi, không thể chạy được. Vui lòng chạy file lesson_review.py để ôn bài.")


def lesson_1() -> None:
    print("\nBài 1: Biến, Hằng và Hàm Print\nTổng 55 câu hỏi.")
    question_templates.multiple_choice_question(
        1, "Hàm print dùng để làm gì?",
        "Gán giá trị cho hằng",
        "In giá trị ra bảng lệnh",
        "Gán giá trị cho biến",
        "Tính toán các phép toán cơ bản",
        'b',
        "Hàm print dùng để hiển thị giá trị ra bảng lệnh (console)."
    )
    question_templates.multiple_choice_question(
        2, "Trong Python, dấu = được gọi là gì?",
        "Dấu bằng",
        "Dấu so sánh",
        "Dấu gán giá trị",
        "Dấu tương đương",
        'c',
        "Dấu = trong Python được dùng để gán giá trị cho biến."
    )
    question_templates.multiple_choice_question(
        3, "Cú pháp đúng để gán giá trị 10 cho biến x là gì?",
        "x == 10",
        "x: 10",
        "x = 10",
        "int x = 10",
        'c',
        "Trong Python, cú pháp gán giá trị cho biến là tên_biến = giá_trị."
    )
    question_templates.multiple_choice_question(
        4, "Điều gì sẽ xảy ra khi một biến đã có giá trị mà bị gán một giá trị khác?",
        "Biến sẽ giữ lại giá trị cũ",
        "Biến sẽ mang giá trị mới và giá trị cũ bị thay thế",
        "Sẽ xảy ra lỗi do ghi đè giá trị",
        "Không có gì xảy ra",
        'b',
        "Biến sẽ mang giá trị mới, không còn mang giá trị cũ nữa."
    )
    question_templates.multiple_choice_question(
        5, "Tên biến nào sau đây là hợp lệ trong Python?",
        "2nd_variable",
        "variable_name",
        "!variable",
        "first variable",
        'b',
        "Tên biến không được bắt đầu bằng số hoặc ký tự đặc biệt và không chứa dấu cách."
    )
    question_templates.true_false_question(
        6, "Trong Python, các biến phải được gán giá trị trước khi sử dụng.",
        "t",
        "Biến cần được gán giá trị trước khi sử dụng."
    )
    question_templates.multiple_choice_question(
        7, "Tên biến nào sau đây không hợp lệ trong Python?",
        "myVariable",
        "variable_1",
        "None",
        "number",
        'c',
        "Tên biến không được phép trùng với các từ khóa đặc biệt như None."
    )
    question_templates.multiple_choice_question(
        8, "Tại sao chúng ta không nên đặt tên biến là các từ khóa đặc biệt như return, if, class?",
        "Vì sẽ khiến tên biến khó đọc hơn",
        "Vì sẽ xảy ra lỗi khi chạy chương trình",
        "Vì biến sẽ bị ghi đè",
        "Vì không có ý nghĩa khi đọc chương trình",
        'b',
        "Các từ khóa đặc biệt đã được Python sử dụng, việc dùng chúng làm tên biến sẽ gây ra lỗi cú pháp."
    )
    question_templates.multiple_choice_question(
        9, "Hằng trong Python thường được biểu diễn dưới dạng nào?",
        "Viết bằng chữ in hoa",
        "Viết bằng chữ in thường",
        "Bắt đầu bằng số",
        "Bắt đầu bằng ký tự đặc biệt",
        'a',
        "Hằng trong Python thường được biểu diễn bằng cách đặt tên biến viết hoa."
    )
    question_templates.multiple_choice_question(
        10, "Câu nào sau đây diễn tả đúng về hằng trong Python?",
        "Giá trị của hằng sẽ thay đổi bất kỳ lúc nào",
        "Giá trị của hằng không bao giờ được phép thay đổi",
        "Hằng có thể bắt đầu bằng số",
        "Hằng luôn được viết bằng chữ in thường",
        'b',
        "Hằng là những giá trị không bị thay đổi trong suốt quá trình chạy chương trình."
    )
    question_templates.multiple_choice_question(
        11, "Đoạn mã sau có lỗi không? Nếu có, lỗi đó là gì?\nif = 10",
        "Không có lỗi",
        "Có lỗi vì if là từ khóa đặc biệt",
        "Có lỗi vì if có ký tự đặc biệt",
        "Có lỗi vì không có dấu chấm phẩy ở cuối dòng",
        'b',
        "if là từ khóa đặc biệt, không thể dùng làm tên biến."
    )
    question_templates.multiple_choice_question(
        12, "Tên biến nào sau đây không vi phạm quy ước?",
        "your_variable",
        "Variable_Name",
        "This_is_a_variable",
        "VariableExample",
        'a',
        "Tên biến nên được viết bằng chữ thường và sử dụng dấu gạch dưới để ngăn cách các từ."
    )
    question_templates.multiple_choice_question(
        13, "Biến x được gán giá trị 5 sau đó được gán tiếp giá trị 7. Giá trị của x hiện tại là bao nhiêu?",
        "5",
        "7",
        "12",
        "Không xác định",
        'b',
        "Giá trị của biến x sẽ bị ghi đè thành 7."
    )
    question_templates.multiple_choice_question(
        14, "Lệnh print() sau đây sẽ in ra giá trị gì?\nx = 10\nprint(x)",
        "In ra x",
        "In ra x = 10",
        "Xảy ra lỗi",
        "In ra 10",
        'd',
        "Lệnh print(x) sẽ in ra giá trị của biến x, tức là 10."
    )
    question_templates.short_answer_question(
        15, "Hãy gán giá trị 37 vào biến tên n.",
        "n = 37"
    )
    print("\nXong 15 câu đầu, còn lại 40 câu.")
    question_templates.multiple_choice_question(
        16, "Lệnh print(x) sẽ hiển thị cái gì nếu biến x chưa được gán giá trị?",
        "Hiển thị None",
        "Hiển thị 0",
        "Hiển thị x",
        "Xảy ra lỗi",
        'd',
        "Nếu biến x chưa được gán giá trị thì lệnh print(x) sẽ báo lỗi NameError."
    )
    question_templates.short_answer_question(
        17, "Đoạn mã sau đây sẽ in giá trị gì ra bảng lệnh?\nn = 5\nprint(n)\nn = 11",
        "5",
        "Giá trị 5 được in ra vì lệnh print(n) được thực hiện trước khi n được gán lại giá trị 11."
    )
    question_templates.multiple_choice_question(
        18, "Để đánh dấu một đối tượng là hằng trong Python, ta nên:",
        "Viết tên đối tượng in hoa",
        "Gán giá trị None cho đối tượng",
        "Không bao giờ gán lại giá trị cho đối tượng",
        "Không thể đánh dấu một đối tượng là hằng trong Python",
        'a',
        "Đối tượng có tên viết in hoa được quy ước là hằng trong Python."
    )
    question_templates.multiple_choice_question(
        19, "Tên nào sau đây không đúng với quy tắc đặt tên đối tượng?",
        "number_of_students",
        "number1",
        "3rd_value",
        "TOTAL_COUNT",
        'c',
        "Tên đối tượng không được bắt đầu bằng số."
    )
    question_templates.multiple_choice_question(
        20, "Tên biến nên được đặt bằng ngôn ngữ nào?",
        "Tiếng Việt",
        "Tiếng Hàn",
        "Tiếng Trung",
        "Tiếng Anh",
        'd',
        "Tất cả tên biến đều nên được đặt bằng tiếng Anh "
        "vì tiếng Anh là ngôn ngữ chung trong lập trình trên toàn thế giới."
    )
    question_templates.true_false_question(
        21, "Python phân biệt chữ hoa và chữ thường trong tên biến.",
        "t",
        "Python phân biệt chữ hoa và chữ thường, vì vậy 'myVariable' và 'myvariable' được coi là hai biến khác nhau."
    )
    question_templates.short_answer_question(
        22, "Điền vào chỗ trống ký hiệu để gán giá trị 'Hello' cho biến greeting: greeting _ 'Hello'",
        "=",
        "Dấu '=' được sử dụng để gán giá trị cho biến trong Python."
    )
    question_templates.multiple_choice_question(
        23, "Khi nào nên sử dụng tên biến viết hoa trong Python?",
        "Cho tất cả các biến",
        "Cho các hằng",
        "Cho các hàm",
        "Cho các lớp",
        'b',
        "Tên biến viết hoa thường được sử dụng cho các hằng trong Python."
    )
    question_templates.true_false_question(
        24, "Từ khóa sep dùng để thay đổi giá trị được in ra vào cuối lệnh print().",
        "f",
        "Từ khóa sep dùng để thay đổi giá trị ngăn cách các giá trị khi in."
    )
    question_templates.true_false_question(
        25, "Trong Python, ta có thể thay đổi giá trị của một biến sau khi đã gán giá trị cho nó.",
        "t",
        "Python cho phép gán lại giá trị cho biến bất cứ lúc nào."
    )
    print("\nCòn 30 câu nữa.")
    question_templates.short_answer_question(
        26, "Viết lệnh để in ra giá trị của biến name.",
        "print(name)",
        "Hàm print() được sử dụng để hiển thị giá trị của biến."
    )
    question_templates.multiple_choice_question(
        27, "Đâu là cách tốt nhất để đặt tên cho một biến chứa số lượng học sinh?",
        "x",
        "a",
        "number_of_students",
        "NUMBER_OF_STUDENTS",
        'c',
        "number_of_students là tên biến mô tả rõ ràng mục đích của biến và tuân theo quy ước đặt tên trong Python."
    )
    question_templates.checkbox_question(
        28, "Chọn tất cả các câu đúng về biến trong Python:",
        "Biến phải được gán giá trị trước khi sử dụng",
        "Biến có thể thay đổi kiểu dữ liệu",
        "Tên biến không được bắt đầu bằng số",
        "Biến không thể bị thay đổi giá trị",
        {'a', 'b'},
        "Trong Python, biến có thể thay đổi giá trị, kiểu dữ liệu và tên biến không được bắt đầu bằng số."
    )
    question_templates.true_false_question(
        29, "Python yêu cầu khai báo kiểu dữ liệu khi tạo biến.",
        "f",
        "Python không yêu cầu khai báo kiểu dữ liệu khi tạo biến, tuy nhiên ta có thể khai báo nếu muốn."
    )
    question_templates.short_answer_question(
        30, "Viết lệnh để gán giá trị 42 cho biến answer:",
        "answer = 42"
    )
    question_templates.multiple_choice_question(
        31, "Trong Python, biến nào sau đây được coi là hằng số?",
        "total_sum",
        "MAXIMUM_VALUE",
        "userInput",
        "final_result",
        'b',
        "Theo quy ước, hằng số trong Python thường được đặt tên bằng chữ in hoa."
    )
    question_templates.true_false_question(
        32, "Python cho phép sử dụng dấu cách trong tên biến.",
        "f",
        "Python không cho phép sử dụng dấu cách trong tên biến. Thay vào đó, ta có thể sử dụng dấu gạch dưới."
    )
    question_templates.multiple_choice_question(
        33, "Đâu là cách đúng để gán giá trị cho nhiều biến cùng lúc trong Python?",
        "int a, b, c",
        "a, b, c = 0",
        "a = b = c = 0",
        "del a, b, c",
        'b',
        "Trong Python, ta có thể gán cùng một giá trị cho nhiều biến bằng cách tạo một chuỗi các dấu gán."
    )
    question_templates.true_false_question(
        34, "Trong Python, ta có thể sử dụng dấu gạch dưới (_) làm ký tự đầu tiên trong tên biến.",
        "t",
        "Python cho phép sử dụng dấu gạch dưới làm ký tự đầu tiên trong tên biến."
    )
    question_templates.checkbox_question(
        35, "Chọn tất cả các quy tắc đặt tên biến đúng trong Python:",
        "Tên biến có thể bắt đầu bằng chữ cái hoặc dấu gạch dưới",
        "Tên biến có thể chứa chữ cái, số và dấu gạch dưới",
        "Tên biến có thể trùng với các từ khóa của Python",
        "Tên biến phân biệt chữ hoa và chữ thường",
        {'a', 'b', 'd'},
        "Tên biến trong Python có thể bắt đầu bằng chữ cái hoặc "
        "dấu gạch dưới, chứa chữ cái, số và dấu gạch dưới, và phân biệt chữ hoa chữ thường."
    )
    print("Sắp xong rồi, còn 20 câu.")
    question_templates.true_false_question(
        36, "Với hàm print, ta có thể in ra nhiều giá trị cùng lúc bằng cách ngăn cách chúng bởi dấu phẩy.",
        "t",
        "Ta có thể in nhiều giá trị cùng lúc theo cú pháp: print(giá_trị_1, giá_trị_2,…, giá_trị_n)"
    )
    question_templates.true_false_question(
        37, "Nhiều tên biến khác nhau có thể chỉ đến cùng một đối tượng.",
        't',
        "Python cho phép dùng nhiều tên khác nhau để chỉ đến cùng một điểm trong bộ nhớ."
    )
    question_templates.checkbox_question(
        38, "Những điều nào sau đây đúng về biến trong Python?",
        "Tên biến nên được viết hoa",
        "Biến có thể được gán lại giá trị là chính nó",
        "Có thể gán giá trị cho nhiều biến trên cùng một dòng",
        "Các biến khác nhau phải chỉ đến các đối tượng khác nhau",
        {'b', 'c'},
        "Tên biến nên được viết thường, có thể sử dụng chính nó để gán lại giá trị, "
        "có thể gán cùng giá trị cho nhiều biến trên một dòng và các biến có cùng giá trị có thể "
        "(nhưng không nhất thiết phải) chỉ đến cùng một đối tượng."
    )
    question_templates.checkbox_question(
        39, "Điều nào sau đây đúng về hàm print?",
        "print() chỉ in được 1 giá trị cùng lúc",
        "Có thể thay đổi giá trị cuối cùng mà print() in ra thông qua từ khóa end",
        "Không thể cho tên biến vào hàm print",
        "Có thể thay đổi giá trị ngăn cách các đối tượng thông qua từ khóa sep",
        {'b', 'd'},
        "print() có thể in nhiều giá trị cùng lúc, thay đổi giá trị ngăn cách bằng từ khóa sep, "
        "thay đổi giá trị kết thúc bằng từ khóa end, có thể nhập giá trị trực tiếp hay dùng tên biến."
    )
    question_templates.multiple_choice_question(
        40, "Giá trị kết thúc (end) mặc định của hàm print là gì?",
        "Không có giá trị (None)",
        "Dấu cách (' ')",
        r"Ký tự xuống dòng ('\n')",
        "Ký tự trống ('')",
        'c',
        r"Giá trị mặc định để kết thúc hàm print là ký tự xuống dòng ('\n')"
    )
    question_templates.multiple_choice_question(
        41, "Trong Python, từ khóa nào được sử dụng để xóa một biến?",
        "remove",
        "delete",
        "del",
        "clear",
        'c',
        "Từ khóa del được sử dụng để xóa một biến trong Python."
    )
    question_templates.multiple_choice_question(
        42, "Khi sử dụng hàm print(), làm thế nào để thay đổi ký tự ngăn cách giữa các giá trị?",
        "Sử dụng tham số 'separator'",
        "Sử dụng tham số 'sep'",
        "Sử dụng tham số 'split'",
        "Sử dụng tham số 'join'",
        'b',
        "Tham số 'sep' trong hàm print() được sử dụng để thay đổi ký tự ngăn cách giữa các giá trị."
    )
    question_templates.true_false_question(
        43, "Trong Python, mọi giá trị đều là đối tượng.",
        "t",
        "Trong Python, mọi dữ liệu, bao gồm giá trị, hàm, lớp,… đều là các đối tượng."
    )
    question_templates.multiple_choice_question(
        44, "Hàm nào được sử dụng để lấy ID của một đối tượng trong Python?",
        "object_id()",
        "get_id()",
        "id()",
        "identity()",
        'c',
        "Hàm id() được sử dụng để lấy ID duy nhất của một đối tượng trong Python."
    )
    question_templates.short_answer_question(
        45, "Viết lệnh để in ra ID của biến x.",
        "print(id(x))",
        "Sử dụng hàm id() và truyền biến x vào để lấy ID của nó, sau đó sử dụng print() để hiển thị."
    )
    print("\nCố lên! Chỉ còn 10 câu nữa thôi!")
    question_templates.short_answer_question(
        46, "Viết lệnh để xóa biến quz ra khỏi chương trình.",
        "del quz",
        "Từ khóa del dùng để xóa biến ra khỏi chương trình."
    )
    question_templates.true_false_question(
        47, "Trong Python, các biến có cùng giá trị luôn trỏ đến cùng một đối tượng trong bộ nhớ.",
        "f",
        "Không phải lúc nào các biến có cùng giá trị cũng trỏ đến cùng một đối tượng trong bộ nhớ. "
        "Điều này phụ thuộc vào kiểu dữ liệu và cách Python quản lý bộ nhớ."
    )
    question_templates.true_false_question(
        48, "Trong Python, ta có thể sử dụng số làm ký tự đầu tiên trong tên biến.",
        "f",
        "Tên biến trong Python không thể bắt đầu bằng số, nhưng có thể chứa số ở các vị trí khác."
    )
    question_templates.true_false_question(
        49, "Nhiều biến khác nhau có thể chỉ đến cùng một đối tượng.",
        "t",
        "Python có thể cho các biến có giá trị giống nhau chỉ đến cùng đối tượng để tiết kiệm bộ nhớ."
    )
    question_templates.multiple_choice_question(
        50, "Đâu là cách tốt nhất để đặt tên cho một hằng?",
        "camelCase",
        "snake_case",
        "PascalCase",
        "UPPERCASE_WITH_UNDERSCORES",
        'd',
        "Quy ước đặt tên cho hằng số trong Python là sử dụng chữ in hoa và dấu gạch dưới để ngăn cách các từ."
    )
    question_templates.short_answer_question(
        51, "Viết lệnh để gán giá trị 3.14 cho một hằng số PI.",
        "PI = 3.14"
    )
    question_templates.multiple_choice_question(
        52, "Điều gì xảy ra khi bạn gán giá trị cho nhiều biến cùng một lúc, như foo = bar = baz = 1?",
        "Chỉ biến đầu tiên được gán giá trị",
        "Tất cả các biến đều được gán giá trị",
        "Python báo lỗi cú pháp (SyntaxError)",
        "Chỉ biến cuối cùng được gán giá trị",
        'b',
        "Khi gán giá trị cho nhiều biến cùng một lúc như vậy, tất cả các biến đều được gán cùng một giá trị."
    )
    question_templates.multiple_choice_question(
        53, "Trong Python, điều gì xảy ra khi bạn cố gắng truy cập một biến đã bị xóa bằng lệnh del?",
        "Python trả về giá trị None",
        "Python tự động tạo lại biến với giá trị mặc định",
        "Python báo lỗi tên biến (NameError)",
        "Python bỏ qua lệnh đó và tiếp tục thực thi",
        'c',
        "Khi cố gắng truy cập một biến đã bị xóa, xảy ra NameError."
    )
    question_templates.true_false_question(
        54, "Trong Python, các biến được tạo ra khi chúng được gán giá trị lần đầu tiên.",
        "t",
        "Trong Python, biến được tạo ra và cấp phát bộ nhớ khi nó được gán giá trị lần đầu tiên."
    )
    question_templates.checkbox_question(
        55, "Những điều nào là đúng khi nói về đối tượng trong Python?",
        "Các biến khác nhau là những đối tượng khác nhau",
        "Có thể dùng id() để kiểm tra danh tính của đối tượng",
        "Nếu hai giá trị có cùng một ID thì hai giá trị đó có thể là hai đối tượng khác nhau",
        "Hai giá trị giống nhau luôn luôn có ID giống nhau",
        {'b', 'd'},
        "Một đối tượng có thể được chỉ đến bởi nhiều biến.\n"
        "Hàm id hiển thị tham chiếu của đối tượng.\n"
        "Hai giá trị có ID giống nhau thì chúng là một đối tượng.\n"
        "Một đối tượng chỉ có một ID."
    )
    print("\nChúc mừng! Bạn đã hoàn thành toàn bộ câu hỏi ôn tập của bài 1! 🥳", end='\n\n')


if __name__ == '__main__':
    warning()