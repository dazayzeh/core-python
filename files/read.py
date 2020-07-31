# run write.py first so the newfile.txt will be created
# otherwise you'll get FileNotFoundError

file = open('newfile.txt', mode='rt', encoding='utf-8')

print(file.read(14))  # reads 12 chars
print(file.read())  # continue reading the rest of the print(file
print(f'empty string {file.read()}')  # should return now an empty string meaning end of print(file
print(file.seek(0))  # points again to the beginning  of the print(file

print(file.readline())  # read until the end of a line
print(file.readline())  # reads the next line
print(file.readline())  # reads the third line
print(f'empty string {file.readline()}') # now returns an empty string
print(file.seek(0))  # points to the beginning of the file

f_list = file.readlines()  # best practice as it reads all the lines into a list
file.close()

print(f_list)
