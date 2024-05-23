with open('C:/python/Udemy-Course/File Handling In Python/Data.txt','r') as file:
    content_1 = file.readline()
    content_2 = file.readline()
    content = file.readlines()
print(content_1)
print(content_2)
print(content)
for line in content:
    print(line.strip())