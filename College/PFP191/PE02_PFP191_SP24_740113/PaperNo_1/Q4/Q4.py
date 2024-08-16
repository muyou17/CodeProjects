def printWordsNumbers(str: str) -> str:
    #Write your statements here
    array = [word.capitalize() for word in str.split()]
    date = ''.join(character for character in list(array[-1]) if character != '/')
    name = ''.join(word for word in array[:-1])
    return name + ':' + date
    #End your statements 
#end printWordsNumbers
#=====================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.==================
def main():
  print("TEST Q4 (3 marks):")
  str = input("Enter the string : ")
  print("OUTPUT:")
  s = printWordsNumbers(str)
  print(s)
#end main
#--------------------------------
if __name__ == "__main__":
  main()
#=========================================================================================
