#
# author: F. Coppo
# description: python file management tutorial
#

"""
 FILE
"""
print("***************")
print("FILE")
print("***************")

# Read from file
print("***************")
print("Read from file")
print("***************")
fileName = "exampleFile.txt"
file = open(fileName, "r")

# print file obj infos
print("filename: %s" % file.name)
print("filemode: %s" % file.mode)

fileContent = file.read() # read the file
print(fileContent)
file.close()              # close the file

# Open file using with: is better practice because it automatically closes the file even if the code encounters an exception
print("File open and print using 'with'")
with open(fileName, "r") as file2:
	# ListFileContent = file2.readlines() # Read all lines and save as a list
	FileContent = file2.readline()		  # Read single lines
file2.closed
print(FileContent)

# Write to an existing file
print("***************")
print("Write to existing file")
print("***************")
Lines = ["This is line X\n", "This is line Y\n", "This is line Z\n"]
with open(fileName, 'a') as writefile: # 'w' create new file, 'a' is for append to existing file
    for line in Lines:
        writefile.write(line)

print("***************")
print("Copy file to another")
print("***************")
with open(fileName,'r') as readfile:
    with open("outputFile.txt",'w') as writefile:
          for line in readfile:
                writefile.write(line)
				
