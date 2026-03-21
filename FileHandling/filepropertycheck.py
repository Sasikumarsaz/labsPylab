f = open("C:/Users/Sasik/Documents/file1test.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)   #f.closed: Returns a boolean value- False when file is currently open otherwise True.

f.close() # to close the file after performing the operations on it.
print("Is Closed?", f.closed)
