from templates import *


def warning() -> None:
    input("Đây là file dùng để chứa các bài học, không thể chạy được. Vui lòng chạy file quiz.py để học.")


def lesson_1() -> None:
    print("Bài 1: Biến, Hằng và Hàm console.log\n\nTổng 30 câu hỏi.")
    multiple_choice_question(
        1, "Đâu là từ khóa để khai báo một hằng trong JavaScript?",
        "let", "var", "const", "Không cần từ khóa",
        'c',
        "Cú pháp để khai báo một hằng: const TÊN_HẰNG = GIÁ_TRỊ_CỦA_HẰNG."
    )
    multiple_choice_question(
        2, "Lệnh nào dùng để in giá trị ra bảng điều khiển (console)?",
        "console.out()", "console.print()", "console.show()", "console.log()",
        'd',
        "Hàm console.log() dùng để in giá trị ra màn hình console."
    )
    true_false_question(
        3, "Đối tượng khai báo bằng `const` có thể thay đổi giá trị sau khi được khởi tạo.",
        'f',
        "Biến `const` không thể thay đổi giá trị sau khi được khởi tạo."
    )
    multiple_choice_question(
        4, "Đâu là từ khóa để khai báo một biến có phạm vi trong khối?",
        "let", "var", "const", "Không cần từ khóa nào",
        'a',
        "Từ khóa `let` dùng để khai báo một biến với phạm vi giới hạn trong khối (block scope)."
    )
    checkbox_question(
        5, "Phát biểu nào sau đây đúng về `console.log()`?",
        "Có thể in ra số và chuỗi",
        "Có thể in ra giá trị thuộc các kiểu dữ liệu khác nhau",
        "Có thể in ra nhiều giá trị cùng lúc",
        "Không thể in ra đối tượng",
        {'a', 'b', 'c'},
        "`console.log` có thể in ra số, chuỗi, và nhiều giá trị cùng lúc. Nó cũng có thể in ra đối tượng."
    )
    multiple_choice_question(
        6, "Biến được khai báo bằng từ khóa `var` có phạm vi thế nào?",
        "Block scope", "Function scope", "Global scope", "Tất cả các phạm vi trên",
        'b',
        "Biến `var` chỉ có phạm vi trong hàm (function scope), không bị giới hạn bởi block scope."
    )
    true_false_question(
        7, "Biến khai báo bằng `let` không được phép khai báo lại trong cùng một phạm vi.",
        't',
        "Đúng, `let` không cho phép khai báo lại biến trong cùng một block scope."
    )
    checkbox_question(
        8, "Chọn tất cả các từ khóa có thể dùng để khai báo biến trong JavaScript:",
        "let", "const", "var", "final",
        {'a', 'c'},
        "`let` và `var` là các từ khóa hợp lệ để khai báo biến trong JavaScript."
    )
    true_false_question(
        9, "Phạm vi của `var` là toàn cục nếu được khai báo ngoài một hàm.",
        't',
        "Biến khai báo bằng `var` sẽ có phạm vi toàn cục (global scope) nếu khai báo ngoài một hàm."
    )
    checkbox_question(
        10, "Khi nào thì biến là biến toàn cục?",
        "Khai báo bên ngoài tất cả các hàm",
        "Khai báo bằng từ khóa `var` bên trong một khối",
        "Khai báo mà không có từ khóa đi kèm",
        "Khai báo với từ khóa `var` bên trong một hàm",
        {'a', 'c'},
        "Biến `var` là global khi khai báo bên ngoài tất cả các hàm hoặc khi khai báo không có từ khóa `var` hay `let`."
    )
    
    print("\nCòn 20 câu.")
    
    true_false_question(
        11, "Hàm `console.log` có thể in ra bất kỳ kiểu dữ liệu nào trong JavaScript.",
        't',
        "Hàm `console.log` có thể in ra bất kỳ kiểu dữ liệu nào như số, chuỗi, mảng,..."
    )
    true_false_question(
        12, "Biến khai báo bằng `let` có thể được truy cập bên ngoài khối không?",
        'f',
        "`let` có phạm vi giới hạn trong khối (block scope), nên không thể truy cập bên ngoài khối đó."
    )
    short_answer_question(
        13, "Hãy khai báo một biến toàn cục tên `myVar` có giá trị 5 trong JavaScript?",
        "myVar = 5",
        "Cú pháp đầy đủ: `myVar = 5;`."
    )
    checkbox_question(
        14, "Phát biểu nào sau đây đúng về hằng?",
        "Không thể gán lại giá trị cho hằng",
        "Có thể thay đổi giá trị của hằng",
        "Phạm vi của hằng là block scope",
        "Có thể khai báo lại hằng trong cùng phạm vi",
        {'a', 'c'},
        "Hằng không thể gán lại giá trị và có phạm vi trong khối."
    )
    multiple_choice_question(
        15, "Tên biến có thể bắt đầu bằng ký tự nào?",
        "Số", "Ký tự đặc biệt", "Chữ cái hoặc dấu gạch dưới", "Khoảng trắng",
        'c',
        "Tên biến phải bắt đầu bằng chữ cái hoặc dấu gạch dưới (_)."
    )
    true_false_question(
        16, "Tên biến có thể chứa dấu cách.",
        'f',
        "Tên biến không được chứa dấu cách."
    )
    multiple_choice_question(
        17, "Tên biến hợp lệ trong JavaScript là:",
        "123abc", "let", "_myVar", "biến",
        'c',
        "`_myVar` là tên biến hợp lệ trong JavaScript."
    )
    multiple_choice_question(
        18, "Trong cùng một phạm vi, có thể khai báo hai biến với cùng một tên không?",
        "Có", "Không", "Tùy vào kiểu khai báo", "Chỉ với biến toàn cục",
        'b',
        "Không thể khai báo hai biến với cùng một tên trong cùng một phạm vi."
    )
    true_false_question(
        19, "Tên hằng trong JavaScript nên viết bằng chữ in hoa với dấu gạch dưới giữa các từ.",
        't',
        "Đây là quy ước chung để phân biệt hằng và biến."
    )
    short_answer_question(
        20, "Tên biến hợp lệ có thể bao gồm các ký tự đặc biệt nào?",
        "_",
        "Tên biến hợp lệ chỉ có thể chứa dấu gạch dưới (_), không được chứa ký tự đặc biệt khác."
    )
    
    print("\nCòn 10 câu. Cố lên, sắp xong rồi!")
    
    multiple_choice_question(
        21, "Tên biến không được phép là:",
        "Tên lớp", "Tên hàm", "Từ khóa đặc biệt", "Dấu gạch dưới",
        'c',
        "Tên biến không được là các từ khóa đặc biệt của JavaScript như `let`, `const`, `if`,..."
    )
    true_false_question(
        22, "Có thể khai báo biến trong JavaScript mà không cần từ khóa `let`, `var`, hoặc `const`. (T/F)",
        't',
        "Đúng, có thể khai báo biến mà không cần từ khóa, nhưng biến đó sẽ tự động có phạm vi global."
    )
    checkbox_question(
        23, "Phát biểu nào đúng về biến toàn cục?",
        "Có thể truy cập từ bất kỳ đâu trong chương trình",
        "Có phạm vi chỉ trong hàm chứa nó",
        "Có thể trùng tên với biến cục bộ",
        "Không thể thay đổi giá trị sau khi khai báo",
        {'a', 'c'},
        "Biến toàn cục có thể truy cập từ bất kỳ đâu và có thể trùng tên với biến cục bộ."
    )
    short_answer_question(
        24, "Lệnh nào dùng để in chuỗi `Hello` ra màn hình console?",
        "console.log('Hello');",
        "Cú pháp đầy đủ: `console.log('Hello');`."
    )
    multiple_choice_question(
        25, "Tên biến `final` có hợp lệ không?",
        "Có", "Không", "Tùy thuộc vào ngữ cảnh", "Không có thông tin",
        'a',
        "`final` không phải là từ khóa đặc biệt trong JavaScript, nên nó là tên biến hợp lệ."
    )
    true_false_question(
        26, "Có thể khai báo lại biến toàn cục trong cùng một phạm vi không?",
        'f',
        "Không thể khai báo lại biến toàn cục trong cùng một phạm vi."
    )
    true_false_question(
        27, "Có thể khai báo biến bằng `let` và `const` trong cùng một phạm vi không?",
        'f',
        "Không thể khai báo cùng một biến bằng `let` và `const` trong cùng một phạm vi."
    )
    checkbox_question(
        28, "Đâu là dòng lệnh khai báo hằng tốt?",
        "const RED = `FF0000`",
        "const total_count = 27",
        "const LISTOFNUMBERS = [1, 2, 3]",
        "const N = 6",
        {'a'},
        "Một tên hằng tốt sẽ chi tiết, ngắn gọn, dễ hiểu, in hoa, ngăn cách các từ bởi dấu gạch dưới."
    )
    multiple_choice_question(
        29, "Nên đặt tên cho các biến, hằng, hàm, lớp,… bằng ngôn ngữ nào?",
        "Tiếng Việt", "Quốc tế ngữ", "Tiếng Anh", "Tiếng Nhật",
        'c',
        "Tiếng Anh là ngôn ngữ chung trong giới lập trình. Dù bạn đến từ nước nào hay làm việc tại đâu thì"
        "vẫn nên luôn luôn sử dụng tiếng Anh trong lập trình để mọi người đều có thể đoc được."
    )
    true_false_question(
        30, "Bình luận (phần chữ không được chạy bởi máy, chỉ để con người đọc)"
        "bắt buộc phải viết bằng tiếng Anh.",
        "f",
        "Tùy theo nơi làm việc mà ta nên chọn ngôn ngữ để bình luận"
        "cho phù hợp với những người sẽ đọc chương trình của chúng ta."
    )
    
    
if __name__ == '__main__':
    warning()