#file=open("file.txt", "r")
#contents=file.read()
#print(contents)
#file.close()

with open("file.txt", "r") as file:
    file_text=file.readlines
print('print easier way: ', file_text)