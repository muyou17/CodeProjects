def cntword(linelst):
    cntdict = dict()
    for word in linelst:
        cntdict[word] = cntdict.get(word, 0) + 1
    return cntdict

def main():
    line = input("Enter a line: ")
    linelst = line.split(sep=' ')
    print(cntword(linelst))

if __name__ == '__main__':
    main()