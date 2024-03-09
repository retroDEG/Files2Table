#honestly this one is working better lmao, might push to main file later
import os
from datetime import datetime

path = 'Testing Grounds'
filedir = os.listdir(path)


#for filename in os.listdir(path):
 #   s = os.path.join(path,st_size)
  #  f = os.path.join(path,filename)
   # print(os.path.basename(f,s))


test = open('testwrite.txt', 'w')

def get_file_info(directory):
    files = os.listdir(directory)
    for file in files:
        path = os.path.join(directory, file)
        splitext = os.path.splitext(path)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            sizekb = size/1024
            sizemb = sizekb/1024
            sizegb = sizemb/1024
            type = splitext[1]
            creation = os.path.getctime(path)
            time = datetime.fromtimestamp(creation).strftime('%m-%d-%y %H:%M:%S')
            test.write(f"{file}\n{type}\n{time}\n{size/1024}KB\n\n")
        else:
            test.write(f"{file}\nFolder\n{time}\n{size/1024}KB\n\n")
get_file_info(path)

test.close()
test = open('testwrite.txt', 'r')
lines = len(test.readlines())
print(lines)
test.close()
test = open('testwrite.txt', 'r')
readline = test.readlines()
print(readline[0:lines])
