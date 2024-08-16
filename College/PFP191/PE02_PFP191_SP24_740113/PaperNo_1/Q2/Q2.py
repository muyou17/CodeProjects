import  math
#-----------------------------------------------------------------------------
def sum(n)->int:
    # Begin your statements here
    r = int()
    for i in range(0, n + 1):
        r += i ** 3
    return r
    # End your statements here
#end sum
#-----------------------------------------------------------------------------
#=============DO NOT ADD NEW OR CHANGE STATEMENTS IN THE MAIN FUNCTION========
def main():
    print('Test Q2 (3 marks)')
    n = int(input("Enter n = "))   
    print("OUTPUT:")
    s = sum(n)
    print(f'{s}')
# end main
#===========DO NOT ADD NEW OR CHANGE THIS STATEMENTS =========
if __name__ == '__main__':
    main()
#================================================================================

