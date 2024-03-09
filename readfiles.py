#ngl this shit's gonna suck, i ony did pyhton for like 2 months in highschool like 8 years ago lmao. if i make this do anything like what i am hoping for i should go buy a lottery ticket. my coding is 45% luck, 50% stack overflow, and 5% skill... get fucked nerd(talking about myself) and good luck
import os

#open txt for writing files and sizes to
filelog = open("files.txt", "w")

# choose directory
path = 'Testing Grounds'

#first testing of this idea
#filedir = os.listdir(path)
#size = os.path.getsize('Testing Grounds/testfile_0.txt')
#print(filedir)
#print(str(size) + 'B')


#this portion referenced from https://www.geeksforgeeks.org/python-get-list-of-files-in-directory-with-size/
#ngl i don't have any clue what this does lmao, but i made it not filter out folders
fun = lambda x : os.path.isfile(os.path.join(path,x))
files_list = os.listdir(path)
 #this either lmao
size_of_file = [
    (f,os.stat(os.path.join(path, f)).st_size)
    for f in files_list
]
#write list of files in filedir to file close write mode
for f,s in size_of_file:
    filelog.write("{} : {}MB \n".format(f, round(s/(1024*1024),3)))
filelog.close()

#opens file in read mode
filelog = open("files.txt", "r")
#reads the lines
line = filelog.readlines()
#print [line number] of choice to console
print(line[2])
filelog.close()

#html output
filetable = open('file2table.txt', 'w')

filetable.write('<td>' + line[2] +'</td>')