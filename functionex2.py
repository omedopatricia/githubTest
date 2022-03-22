#Write a Python function that takes a list and returns a new list with only the unique elements of the first list.

def uniquelist(*randomstring):
    #convert the string to a list
    randomlist = list(randomstring)
    #convert the list to a set
    randomset = set(randomlist)
    print(randomset)


#input list of items from the user
randomstring= input("Please enter a random list of items separated by a comma: ")

uniquelist()


