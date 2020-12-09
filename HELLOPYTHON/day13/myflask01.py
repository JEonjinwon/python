from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/myget")
def myget():
    temp = request.args.get('name', "전진원")
    temp1 = request.args.get('juso', "대전광역시")
    out=""
    out+=temp
    out+="-" 
    out+=temp1
    return out



if __name__=="__main__":
    app.run(host="127.0.0.1",port="7777") 