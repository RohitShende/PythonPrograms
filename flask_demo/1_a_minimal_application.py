from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def hello_world():
    return "Hello, World 123 !!!"


@app.route("/welcome")
def welcome():
    return "<marquee> <h1> Welcome Rohit </h1> </marquee>"


if __name__ == '__main__':
    app.run()
