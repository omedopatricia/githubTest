def sumlist(*inputnum):
    #Create variables for the sum, avaerage and count of the list
    sumn = 0
    avg = 0
    count = 0
    #convert the input to numbers
    inputnum = inputstring.split(",")
    #convert the numbers to a list
    listnums = list(map(float, inputnum))
    #count n
    n = len(listnums)
    #Add n and store in a sum variable
    sumn = sum(listnums)
    #Divide sum by count n and store in a variable avg
    avg = sumn/n
    print("The average is ",avg)


#input the numbers
inputstring = input("Please enter the numbers that you would like to add, separated by commas`")

#call the function
sumlist()
 