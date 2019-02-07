from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")

def hello():
    return render_template("index.html")

@app.route("/data_collect",methods=['POST'])

def data_collect():
    email = request.form["email"]
    password = request.form["pass"]
    print(email,password)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
