from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1> Hello  World !! Welcome To Cyber Creed.... </h1>"

@app.route("/index")
def index():
    return  render_template('index.html')

# main driver function
if __name__ == "__main__":

    app.run()
