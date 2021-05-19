from flask import Flask, render_template
import os

PEOPLE_FOLDER = os.path.join('static', 'images/')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'watermark.jpg')
    return render_template("index.html", user_image = full_filename)

if __name__=="__main__":
    app.run(port=4556, debug=True)