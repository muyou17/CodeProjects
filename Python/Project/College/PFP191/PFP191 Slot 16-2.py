def out(s:str):
    acc, sep, email = s.partition('@')
    l = acc.partition(acc[-8])
    return l

def main():
    print("INPUT:")
    s = input()
    print("OUTPUT:")
    print(out(s))

if __name__ == '__main__':
    main()