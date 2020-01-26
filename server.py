
from flask import Flask

app = Flask(__name__)

@app.route("/")
def showName():
    return "<div>Hellow world</div>"
    
if __name__ == '__main__':
    app.run()
