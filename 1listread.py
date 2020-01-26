toDoList = "" 
toDoItem = input("Введите описание дела: ")

while toDoItem != "выход": 
    toDoList = toDoList + toDoItem + " \n"    
    toDoItem = input("Введите описание дела: ") #дела ввоодим на английском

myFile = open("myFile.txt", "w") 
myFile.write(toDoList) 
myFile.close()
