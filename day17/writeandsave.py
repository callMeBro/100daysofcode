# Write line to file
exmp2 = 'random.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")
    
# Read file to see if it worked 
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
    
###################################################################################  
    
    
# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    
# Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
    
###################################################################################  
    
    
# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

# Write the strings in the list to text file
with open('test.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)        
        
# Verify if writing to file is successfully executed
with open('test.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
    
###################################################################################  
 
    
# Overwrite content in file-- setting the code to w overwrite all existing data in the file 
with open('test.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('test.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
# Write new lines to file
with open('test.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
    
# Verify if the new lines are in the text file
with open('test.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
    
###################################################################################  
    
    # r+ : Reading and writing, Cannot truncate the file 
    # w+ : Writting annd reading truncates the file 
    # a+ :Appending and reading. Creates a new file, if none exist. 
    
# Append to file and read
with open('test1.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())
    
with open('test1.txt', 'a+') as testwritefile:
    
    # Prints the initial position of the file pointer using the tell() method. The tell() method returns the current position of the file pointer.
    print("Initial Location: {}".format(testwritefile.tell()))
    
    
    # read from current position of the file pointer 
    data = testwritefile.read()
    if not data:
        print('Read nothing')
    else:
        print(testwritefile.read())
    
    # Moves the file pointer to the beginning of the file using the seek() method with arguments (0, 0). 
    # The first argument (0) indicates the offset (position from the beginning) and the second argument 
    # (0) indicates the reference point (beginning of the file).
    testwritefile.seek(0, 0)
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    
    # read from the new position 
    data = testwritefile.read()
    if not data:
        print('Read nothing')
    else:
        print(data)
    
    # printing the final position 
    print("Location after read: {}".format(testwritefile.tell()))

# Overwrite file content and truncate
with open('test1.txt', 'r+') as testwritefile:
    testwritefile.seek(0, 0)
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0, 0)
    print(testwritefile.read())
    
    testwritefile.seek(0, 0)
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    # Uncomment the line below to truncate the file
    # testwritefile.truncate()
    testwritefile.seek(0, 0)
    print(testwritefile.read())
    
# Copy file to another
with open('test.txt', 'r') as readfile:
    with open('test1.txt', 'w') as writefile:
        for line in readfile:
            writefile.write(line)
                
# Verify if the copy is successful
with open('test1.txt', 'r') as testwritefile:
    print(testwritefile.read())
