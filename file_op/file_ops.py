
# r => read
# r+
# w => write
# w+
# a => append
# a+

#read : readline,readlines
fp = open("input.txt","r")
# content = fp.read()
# print(content)

# content = fp.read(100)
# #number of characters
# print(content)

#content = fp.readline()
content = fp.readlines()
# print(content)
# print(type(content))
# print(content[:5])

# for x in fp:
"""
Not working
"""
#     print(list(x))

# #write
# fp = open("input2.txt","w")
# fp.write("Write this line to a file 1")

# content = fp.read()
# print(content)

#can perform only one operation with r,w

# fp = open("input2.txt","w+")
# fp.write("second")

# content = fp.read()
# print(content)

# tell => current fp position
# seek(offset,position) => to change the fp position

# offset => number of char
# position => 0 => Start of the file
#             1 => current positon
#             2=> end of the file

# seek(15,0) => change the fp by 15 char from start of the file
# seek(0,2) => change fp by 0 char from end of the file
# seek(15,1) , seek(15,2)

fp = open("input2.txt","w+")
print(fp.tell())
fp.write("Sample text line 1")
print(fp.tell())
fp.seek(0,0)
print(fp.tell())
content = fp.read()
print(fp.tell())
print(content)

# r+ => read + write

fp = open("input.txt","r+")
content = fp.read()
print(content)

fp.write("\n\nSample line added using python script")
# difference between w+ and r+:
# w+ will not maintain the content but r+ maintain the content as well

#a
#a+
# r,r+,w,w+ => fp is at start
# a,a+ => at the end

fp = open("input.txt","a+")
# print(fp.tell())
# content = fp.read()
# print(content)

fp.write("\n\nabc")

# r => fp => start, file should already exist, read
# r+ => fp => start, file should already exist, read + write

# w => fp => start, create a new file, write
# w+ => fp => start, create a new file, write+ read

# a => fp => end , create a new file, wirte at the end
# a+ => fp => end , create a new file, wirte at the end