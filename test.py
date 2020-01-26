# '\n'
file = open("test.tst", 'w') # "r" = чтение, "w" - запись
# a = int(x) x = '32' a = 32

x = input()
while(x!=""):
    file.write(x + '\n')
    x = input()

file.close()