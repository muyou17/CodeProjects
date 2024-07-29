def readFile(p):
    try:
        f = open(p, 'r')
        return f.readlines()
    except:
        print("Không tìm được file", p)
        exit()

def extractEmail(lines:str):
    for line in lines:
        if line.lower().startswith("from"):
            s = line.split(":")[1].strip()
            print("Người gửi:", s)
        elif line.lower().startswith("to"):
            r = line.split(":")[1].strip()
            print("Người nhận:", r)
        elif line.lower().startswith("cc"):
            c = line.split(":")[1].strip()
            print("Người đồng nhận:", c)

def main():
    p = input("Tên file: ")
    lines = readFile(p)
    extractEmail(lines)

if __name__ == '__main__':
    main()