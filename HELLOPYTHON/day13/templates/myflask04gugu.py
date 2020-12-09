from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/gugu",methods=['POST','GET'])
def gugu():
    dan = request.form["dan"]
    
    return render_template('gugu.html',dan=dan)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="7777")