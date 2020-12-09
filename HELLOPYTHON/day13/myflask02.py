from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/mypost",methods=['POST'])
def mypost():
    name=request.form["name"]
    juso=request.form["juso"]
    
    out=""
    out+=name
    out+="-" 
    out+=juso
    return out



if __name__=="__main__":
    app.run(host="127.0.0.1",port="7777") 