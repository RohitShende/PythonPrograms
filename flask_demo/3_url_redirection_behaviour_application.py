from flask import Flask, redirect, url_for

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    # redirecting manually / forcefully
    return redirect(url_for('projects'))


@app.route('/projects/')
def projects():
    # will redirect if trailing slash is absent
    # works as a directory listing in file system
    return 'The project page'


@app.route('/about')
def about():
    # will throw an error if trailing slash is present
    # works as a file listing in file system
    return 'The about page'


if __name__ == '__main__':
    app.run()
