#Write a Python function that checks whether a passed string is palindrome or not.

def checkpalindrome(mystring):
    #Reverse the string and store in a variable
    reversestring = mystring[::-1]
    print(reversestring)
    #Check if the original string matches the reversed one
    if(mystring == reversestring):
        print("That's a palindrome!")
    else:
        print("That's not a palindrome.")


#Enter a string and store in a variable
mystring = input("Enter the word ")
checkpalindrome(mystring)