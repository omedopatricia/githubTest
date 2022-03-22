#Write a Python function to create and print a list where the values are square of numbers between 1 and 30
#create function with the list as the parameter
def squarelist():
    #create an empty list
    listi = []
    #add items to the list
    for i in range (1,31):
        listi.append(i)
    print(listi)

#call the function
squarelist()

