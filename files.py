#create a file or open it
#f = open("textfile.txt", "w+")

#open the file and append text to it
f = open("textfile.txt", "r")

#write into the file
#for i in range(10):
    #f.write("This is line " + str(i) + "\r\n")

#close the file when done
#f.close()

#open files and read contents
if f.mode == 'r':
    #contents = f.read()
#read line by line
    fl = f.readlines()
    for x in fl:
        print(x)
    #print(contents)