def out(s:str):
    l = s.split(':')
    return ' '.join(l[0].split()).title() + ' ' + l[1].strip()

def main():
    print("INPUT:")
    s = input()
    print("OUTPUT:")
    print(out(s))

if __name__ == '__main__':
    main()