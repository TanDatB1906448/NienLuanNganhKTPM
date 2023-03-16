from flask import Blueprint, render_template, redirect, url_for, request, flash, send_from_directory, current_app
from werkzeug.utils import secure_filename
import os
from flowerR.FRModel.services import (predictAImage)

FGModel = Blueprint("FGModel", __name__)
UPLOADFOLER = os.path.dirname(__file__)

@FGModel.route("/recognize", methods = ['GET', 'POST'])
def uploadImage():
    try:
        if request.method == 'POST':
            image = request.files['img']
            if image.filename == "":
                return redirect(request.url)
            if image:
                imgName = secure_filename(image.filename)
                fileName = "image" + os.path.splitext(imgName)[1]
                image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], fileName))
                result = predictAImage(os.path.join(current_app.config['UPLOAD_FOLDER'], fileName))
                print(result)
                print(type(result))
                return render_template("recognize.html", fileURL = "..\\static\\uploads\\" + fileName)
    except: print("Except")
    return render_template("recognize.html")
