from flask import Flask, render_template

app = Flask(__name__)

@app.route("/default")
def hello():
    my_list = [0,1,2,3,4,5]
    return render_template('default.html',myname="JEON",my_list=my_list)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="7777")