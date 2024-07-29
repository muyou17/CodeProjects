def data_read(p):
    l = {'name': [],
         'sid': [],
         'grade': []}
    with open(p, 'r') as f_in:
        for line in f_in:
            if not line.strip().startswith('#'):
                name, sid, grade = line.split(',')
                list['name'].append(name.strip())
                list['sid'].append(sid.strip())
                list['grade'].append(grade.strip())
    return l

def menu():
    print("Student Information Management Program")
    print("Func #1: Print student information list")
    print("Func #2: Find student information by name")
    print("Func #3: Delete student information by name")
    print("Func #4: Print student information with the highest score")
    print("Func #5: Sort student information by score")
    print("Func #6: Sort student information by student ID number")
    print("Func #7: Input new student information")
    print("Func #8: Edit student information")
    print("Func #9: Save student information into sinh_vien.txt")
    print("Func #10: Quit")
    o = int(input("Choose function: "))
    return o

def list_print():
    exit()

def main():
    m = menu()
    if m == 1:
        list_print()
    else:
        print("Please choose an option from 1 to 10 only!")
        main()

if __name__ == '__main__':
    main()