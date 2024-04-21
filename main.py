import requests
from flask import Flask,request


app = Flask(__name__)


@app.route('/')
def home(): 
    url = request.args.get('url')
    if url == None :   
        return ' i am mr k . i gonna fuck you real soon '
    res = requests.get('https://moviekex.online:5001/fetch?url='+url).content
    return res


if __name__ == '__main__': 
    app.run()



