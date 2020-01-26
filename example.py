
file = open('test.txt', 'w')
x = int(input())
while(x != 0):
    file.write(str(x) + ' ')
    x = int(input())

file.close()