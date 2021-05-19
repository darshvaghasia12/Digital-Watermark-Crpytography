import os
import time
import cv2
from flask import Flask,render_template,request

app=Flask(__name__)

APP_ROOT=os.path.dirname(os.path.abspath(__file__))
target1 = os.path.join('static',APP_ROOT, 'images/')
app.config['UPLOAD_FOLDER'] = target1
@app.route("/")
def index():
    return render_template("watermark.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT,'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("Original Image"):
        print(file)
        filename= file.filename
        destination="/".join ([target,filename])
        print(destination)
        file.save(destination)
    return render_template("complete.html")

@app.route("/owner", methods=['POST'])
def ownership():
    os.system('python owernership_share_generator.py')
    print(target1)
    return render_template("ownership.html")

@app.route("/upload_StolenImages", methods=['POST'])
def upload_StolenImages():
    target1 = os.path.join(APP_ROOT, 'images/stolen_images')
    print(target1)

    if not os.path.isdir(target1):
        os.mkdir(target1)

    for file in request.files.getlist("Stolen Image"):
        print(file)
        filename = file.filename
        destination = "/".join([target1, filename])
        print(destination)
        file.save(destination)
    return render_template("copyrightcheck.html")

@app.route("/copyrightcheck", methods=['POST'])
def copyrightcheck():
    os.system('python master_share_generator_1.py')
    return render_template("watermark_generator.html")

@app.route("/generate_watermark", methods=['POST'])
def generate_watermark():
    target2 = os.path.join(APP_ROOT, 'images/regenerated_watermarks')
    print(target2)

    if not os.path.isdir(target2):
        os.mkdir(target2)

    os.system('python watermark_generator.py')
    return render_template("Accuracy.html")

@app.route("/Accuracy", methods=['POST'])
def Accuracy():
    template = cv2.imread('images\watermark.jpg', 0)
    res1=[]
    for k in range(0, 4):
        img_gray = cv2.imread('images\\regenerated_watermarks\\watermark_img_' + str(k) + '.jpg', 0)
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        res1.append(res)
    return render_template('DispAccuracy.html', res=res1[:])



if __name__=="__main__":
    app.run(port=4555, debug=True)