# # Reading and Storing the Entire Content of a File
# # Using the read method, you can retrieve the complete content of a file
# # and store it as a string in a variable for further processing or display.
# # Step 1: Open the file you want to read
# with open("random.txt", 'r') as file:
    
#     # line1 = file.readline()  # Reads the first line
#     # line2 = file.readline()  # Reads the second line
    
#     # print(line1)  # Print the first line
#     # if 'tuesday' in line2:                #check if it contains a specific word 
#     #     print('tuesday is in line 2 ')
#     # else:
#     #     print("no tuesday in line 2")
        
        
#     #read characters from a specific position in the file  us seek() method 
    
#     # Step 2: Use the read method to read the entire content of the file
#     file_stuff = file.read()
    
#     # seeked = file.seek(10)
    
    
#     # Rewind the file pointer back to the beginning
#     file.seek(0)

#     # print(seeked)
#     characters = file.read(5)  # Read the next 5 characters
#     print(characters)
    
    
#     # Step 3: Now that the file content is stored in the variable 'file_stuff',
#     # you can manipulate or display it as needed.
    
    
#     # For example, let's print the content to the console:
#     # print(file_stuff)

# # Step 4: The 'with' statement automatically closes the file when it's done,
# # ensuring proper resource management and preventing resource leaks.

##########################################################################################################################################################################################################################################

# example1 = "random.txt"
# file1 = open(example1, "r")

# # Print the path of file
# print("Name: " + file1.name + "\n")
# # ------------------------------------ #

# # Print the mode of file, either 'r' or 'w'
# print("Mode: " + file1.mode)
# print("\n")
# # ------------------------------------ #

# # Read the file
# FileContent = file1.read()
# FileContent

# # ------------------------------------ #
# # Print the file with '\n' as a new line
# print(FileContent)

# # ------------------------------------ #

# # Type of file content
# print(type(FileContent))

# # ------------------------------------ #

# # Close file after finish
# file1.close()                   #This frees up resources and ensures consistency across different python versions



##########################################################################################################################################################################################################################################


# A BETTER WAY TO OPEN FILES

# example1 = "random.txt"
# file1 = open(example1, "r")

# # # ------------------------------------ #
 
# # Open file using with
# with open(example1, "r") as file1:
#     FileContent = file1.read()
#     print(FileContent)
# print("\n")
    

# # # ------------------------------------ #

# # Verify if the file is closed
# file1.closed

# # # ------------------------------------ #

# # See the content of file
# print(FileContent)
# print("\n")

# # # ------------------------------------ #

#     # Rewind the file pointer back to the beginning
# # Read first four characters
# with open(example1, "r") as file1:
#     print(file1.read(4))
# print("\n")
    
# # # ------------------------------------ #
    
#     # Read certain amount of characters
# with open(example1, "r") as file1:
#     print(file1.read(4))
#     print(file1.read(4))
#     print(file1.read(7))
#     print(file1.read(15))
# print("\n")


# # ------------------------------------ #
     
    # Read certain amount of characters
# with open(example1, "r") as file1:
#     print(file1.read(16))
#     print(file1.read(5))
#     print(file1.read(9))
    
# print("\n")
    
# # # ------------------------------------ #
# # Rewind the file pointer back to the beginning


#     # Read one line
# with open(example1, "r") as file1:
#     print("first line: " + file1.readline())
    
# # # ------------------------------------ #
    
# with open(example1, "r") as file1:
#     print(file1.readline(20)) # does not read past the end of line
#     print(file1.read(20)) # Returns the next 20 chars
    
# # # ------------------------------------ #
    
#     # Iterate through the lines
# with open(example1,"r") as file1:
#         i = 0;
#         for line in file1:
#             print("Iteration", str(i), ": ", line)
#             i = i + 1
            
        
# # ------------------------------------ #
#    # Read all lines and save as a list
# with open(example1, "r") as file1:
#     FileasList = file1.readlines()
    
# # # ------------------------------------ #
    
#     # Print the first line
# FileasList[0]

# # # ------------------------------------ #

# # Print the second line
# FileasList[1]

# # # ------------------------------------ #

# # Print the third line
# FileasList[2]

###################################################################################################################################################################################################################################################

# Writing to a file
# Create a new file Example2.txt for writing
with open('abcd.txt', 'w') as file1:
    file1.write("This is line A\n")
    file1.write("This is line B\n")
    file1.write("This is line C\n")
    file1.write("This is line D\n")
    # file1 is automatically closed when the 'with' block exits
    
# # # ------------------------------------ #
    
    
# # # ------------------------------------ #

    # Data to append to the existing file
new_data = "This is line E"
# Open an existing file Example2.txt for appending
with open('abcd.txt', 'a') as file1:
    file1.write(new_data + "\n")

# # # ------------------------------------ #
        # Open the source file for reading
with open('random.txt', 'r') as source_file:
    # Open the destination file for writing
    with open('destination.txt', 'w') as destination_file:
        # Read lines from the source file and copy them to the destination file
        for line in source_file:
            destination_file.write(line)
    # Destination file is automatically closed when the 'with' block exits
# Source file is automatically closed when the 'with' block exits

# # # ------------------------------------ #


    # file1 is automatically closed when the 'with' block exits
    
    # file1 is automatically closed when the 'with' block exits

#needs node js enviroment for pyodide.http
# from pyodide.http import pyfetch

# import pandas as pd

# filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"

# async def download(url, filename):

#     response = await pyfetch(url)

#     if response.status == 200:

#         with open(filename, "wb") as f:

#             f.write(await response.bytes())

# await download(filename, "example1.txt")

# print("done")
