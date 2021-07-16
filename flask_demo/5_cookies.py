from flask import Flask, render_template, request, make_response

app = Flask(__name__)
app.config['DEBUG'] = True


# Storing cookies:
@app.route('/')
def index():
    resp = make_response(render_template('base.html'))
    resp.set_cookie('username', 'Rohit_123')
    return resp


# Reading cookies:
@app.route('/access_cookie')
def access_cookie():
    username = request.cookies.get('username')
    print(username)
    return username
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.


if __name__ == '__main__':
    app.run()
