import os

source = 'C:/Users/user/Downloads/Python/Projects/Project 115/main.txt'
destination = 'C:/Users/user/Downloads/Python/Projects/Project 115/newfile.txt'

os.rename(source, destination)
print("File renamed from ", source, " to ", destination)

'''
Output ->

File renamed from  C:/Users/user/Downloads/Python/Projects/Project 115/main.txt  to  C:/Users/user/Downloads/Python/Projects/Project 115/newfile.txt
'''