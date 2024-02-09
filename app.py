
from flask import Flask, render_template, send_from_directory, url_for, redirect

from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'golden-lubis'
# app.config['UPLOAD_PHOTOS_DEST'] = 'uploads'

# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

# class UploadForm(FlaskForm):
#     photo = FileField(
#         validators=[
#             FileAllowed(photos, 'Only images are allowed'),
#             FileRequired('File filed should not be empty')
#         ]
#     )
#     submit = SubmitField('Upload')

@app.route('/')
def home():
    return render_template('mathGPT.html')

@app.route('/mathGPT.html')
def math():
    return redirect(url_for("home"))

@app.route('/photo_it')
def photo_it():
    return render_template('photo_it.html')

@app.route('/photo_it.html')
def photo_html():
    return redirect("photo_it")



# @app.route('/uploads/<filename>')
# # def get_file(filename):
# #     return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)


# @app.route('/', methods=['GET', 'POST'])
# def upload_image():
    # form = UploadForm()
    # if form.validate_on_submit():
    #     filename = photos.save(form.photo.data)
    #     file_url = url_for('get_file', filename=filename)
    # else:
    #     file_url = None
    # return render_template('photo_it.html', form=form, file_url=file_url)


if __name__ == "__main__":
    app.run()