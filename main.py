from utils import GetLength
from flask import Flask

app = Flask(__name__)

@app.route('/')
def startAction():
    obj = GetLength.GetLength("SornaRajaPrabhu")
    return str(obj.length())

if __name__ == '__main__':
    app.run()
