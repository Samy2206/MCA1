
# f = open(filename,method)

# f = open("demo.txt","w")

#r -> read filenotexist
#w -> create new file override
#a  -> new file create do not ovverride
#r+  -> read and write / pointer at start 
#w+   -> write and read and ovveride the file data
#a+   ->  read and write without ovveride
#x    -< exclusive file already exist error


# name -> Name of opened file
# mode ->  Mode in which the file is opened
# closed ->  Returns boolean value indicates that file is closed or not
# readable()  ->  Retruns boolean value indicates that whether file is readable or not
# writable() ->  Returns boolean value indicates that whether file is writable or not.


#file methods
# f= open('demo.txt','w')
# print(f.name)
# print(f.mode)
# print(f.closed)
# print(f.readable())
# print(f.writable())

#write data to file
# f=open('demo.txt','w')
# f.writelines(['sam','shubham','sanjana'])           #iterable object as a parameter
# f.close()


#read data from file
# f = open('demo.txt','r')
# # data = f.read()           #read all the data from the files
# # data = f.read(10)           #to read n number of characters
# # data = f.readline()             #read one line at a time
# # data2 = f.readline()
# data = f.readlines()
# for i in data:
#     print(i)
# f.close()


#using with

# with open('demo.txt','r') as f:
#     print(f.read())
#     print(f.closed)
# print(f.closed)


import csv
f=open('demo1.csv','w',newline="")
w=csv.writer(f)
w.writerows([['sam',21,'fymca'],['shubham',22,'fymba'],['sanjana',20,'fymca']])
f.close()
f = open('demo1.csv','r')
r=csv.reader(f)

print(r)
for i in r:
    print(i)

