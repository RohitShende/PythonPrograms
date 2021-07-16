from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


# Accepting variables as url parameters


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/send_int/<int:post_id>')
def send_int(post_id):
    # show the post with the given id, the id is an integer
    return f'Received Int {post_id}'


@app.route('/send_float/<float:post_id>')
def send_float(post_id):
    # show the post with the given id, the id is a float
    return f'Received float {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


if __name__ == '__main__':
    app.run()
