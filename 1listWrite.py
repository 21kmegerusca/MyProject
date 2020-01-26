from mcpi.minecraft import Minecraft 
mc = Minecraft.create() 
myFile = open("myFile.txt", "r") 

toDoList =  myFile.read().splitlines()
myFile.close()

for line in toDoList:
    mc.postToChat(line)
