from flask import request, Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def hello_world():
    return redirect(url_for('upload_file'))


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save("uploads/" + f.filename)
        return "File Upload Successful !", 200
    else:
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(port=8001)
