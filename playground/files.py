f = open('demo.txt', mode='r')
# f.write('Hello from python!\n')
# f.close()

file_content = f.readlines()
f.close()
print(file_content)


with open('demo.txt', mode='r') as f:
    line = f.readline()
    while line:
        print(" - ", line)
        line = f.readline()


print(file_content)


for line in file_content:
    print(line[:-1])






