# --------------------------------
def findMaximum(a,b,c)->int:
    # Write your statements here
    if b > a:
        a, b = b, a
    if c > a:
        a, c = c, a
    return a
    # End your statements
# end findMaximum
# ===========DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============
def main():
    print("TEST Q1 (2 marks):")
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = int(input("Enter c : "))
    result = findMaximum(a,b,c)
    print("OUTPUT:")
    print(f"{result}")
# end main
# --------------------------------
if __name__ == "__main__":
    main()
# =========================================================================
