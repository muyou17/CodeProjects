def cntchar(line):
    cntdict = dict()
    for char in line:
        cntdict[char] = cntdict.get(char, 0) + 1
    return cntdict

def main():
    line = list(input("Enter a line: ").replace(' ', ''))
    print(cntchar(line))

if __name__ == '__main__':
    main()