
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from flask import Flask

app = Flask(__name__)

@app.route("/")
def showName():
    pos = mc.player.getTilePos()
    return "Player position: x: "+str(pos.x)+" y: "+str(pos.y) +" z: "+str(pos.z)

if __name__ == '__main__':
    app.run()
