class Employee:
    def __init__(self, code: str, name: str, birth: int, salary: int, address: str) -> None:
        self.code = code
        self.name = name
        self.birth = birth
        self.age = lambda: 2024 - self.birth
        self.salary = salary
        self.income = lambda: self.salary * 12
        self.address = address

    def display(self) -> None:
        print("Mã nhân viên:", self.code,
              "\nTên:", self.name,
              "\nNăm sinh:", self.birth,
              "\nTuổi:", self.age(),
              "\nLương tháng:", self.salary,
              "\nThu nhập hàng năm:", self.income(),
              "\nĐịa chỉ:", self.address)

def main() -> None:
    data, employees = open("data.csv", 'r'), list()

    for line in data:
        code, name, birth, salary, address = line.split(',')
        employees.append(Employee(code, name, int(birth), int(salary), address))

    for employee in employees:
        Employee.display(employee)

if __name__ == '__main__':
    main()