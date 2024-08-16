import math
#-----------------------
def isPrime(n:int)->bool:
    # Write your statements here
    if n >= 2:
        pr = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                pr = False
                break
    else:
        pr = False
    return pr
    # End your statements
#end isPrime
#--------------------------
def countPrimes(li:list)->int:
    # Write your statements here
    c = int()
    for i in range(0, len(li)):
        if isPrime(li[i]):
            c += 1
    return c
    #End your statements
#end countPrimes
# DO NOT ADD NEW OR CHANGE STATEMENTS IN THIS FUNCTION
def inputList(li:list, n:int):
    for i in range(n):
        li.append(int(input(f"li[{i}]=")))
# end inputList
#========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
def main():
  print("TEST Q3 (2 marks):")
  li = list()
  n = int(input("Enter n = "))
  inputList(li, n)  
  print("OUTPUT:")
  result = countPrimes(li)
  print(f"{result}")
#end main
#------------------------------------
if __name__ == "__main__":
  main()
#============================================================
