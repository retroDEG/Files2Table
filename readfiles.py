#ngl this shit's gonna suck, i ony did pyhton for like 2 months in highschool like 8 years ago lmao. if i make this do anything like what i am hoping for i should go buy a lottery ticket. my coding is 45% luck, 50% stack overflow, and 5% skill... get fucked nerd(talking about myself) and good luck
import os

# choose directory
path = 'Testing Grounds'

#my own testing
filedir = os.listdir(path)
size = os.path.getsize('Testing Grounds/testfile_0.txt')
print(filedir)
print(str(size) + 'B')


#this portion referenced from https://www.geeksforgeeks.org/python-get-list-of-files-in-directory-with-size/
 
#ngl i don't have any clue what this does lmao, but i made it not filter out folders
fun = lambda x : os.path.isfile(os.path.join(path,x))
files_list = os.listdir(path)
 #this either lmao
size_of_file = [
    (f,os.stat(os.path.join(path, f)).st_size)
    for f in files_list
]
#i kinda know what this is doing though
for f,s in size_of_file:
    print("{} : {}MB".format(f, round(s/(1024*1024),3)))