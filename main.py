import utils
from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def startAction():
    #obj = utils.GetLength.GetLength("SornaRajaPrabhu")
    return sys.path
    #return str(obj.length())

if __name__ == '__main__':
    app.run()
