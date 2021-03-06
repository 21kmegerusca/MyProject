from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import shelve

def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2

def copyStructure(x1, y1, z1, x2, y2, z2):
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)

    width = x2 -  x1
    height = y2 -  y1
    length = z2 -  z1
    structure = []
    print("Пожалуйста, подождите…")

    #Копируем конструкцию
    for row in range(height):
        structure.append([])
        for column in range(width):
            structure[row].append([])
            for depth in range(length):
                block = mc.getBlockWithData(x1 + column, y1 + row, z1 + depth)
                structure[row][column].append(block)
    return structure
s = ""
while s!="выход":
    # Получаем координаты первого угла
    input("Пройдите к первому углу и нажмите Enter в этом окне")
    pos1 = mc.player.getTilePos()
    x1 = pos1.x
    y1 = pos1.y
    z1 = pos1.z

    # Получаем координаты второго (противоположного) угла
    input("Подойдите к противоположному углу и нажмите Enter в этом окне")
    pos2 = mc.player.getTilePos()
    x2 = pos2.x
    y2 = pos2.y
    z2 = pos2.z

    structure = copyStructure(x1, y1, z1, x2, y2, z2)
    structureName = input("Как вы хотите назвать конструкцию? ") 

    #Сохраняем конструкцию в файл
    shelveFile = shelve.open("structuresFile.db")
    shelveFile[structureName] = structure
    shelveFile.close()
    s = input("если больше не хотите сохранять конструкции, напишите 'выход'")
