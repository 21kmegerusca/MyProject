"""
Сначала запускаем программу копирования, сохраняем интересующие нас контрукции
Затем отправляем игрока туда, где хотим создать копию конструкции,
и вводим в окне консоли название объекта.
Программа тут же создаст копию объекта.
Единожды сохранив конструкцию, вы можете загрузить ее в Minecraft в любой момент!
Для этого нужно лишь запустить программу и ввести имя конструкции,
указанное при ее сохранении.
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import shelve

def buildStructure(x, y, z, structure):
    xStart = x
    zStart = z
    for row in structure:
        for column in row:
            for block in column:
                mc.setBlock(x, y, z, block.id, block.data)
                z += 1
            x += 1
            z = zStart
        y += 1
        x = xStart
        
# Открываем файл и загружаем трехмерный список structure
structure = shelve.open("structuresFile.db")
structureName = input("Введите название конструкции: ")

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
buildStructure(x, y, z, structure[structureName])
