
from flask import Flask, render_template
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flast_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'golden-lubis'
app.config['UPLOAD_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File filed should not be empty')
        ]
    )
    submit = SubmitField('Upload')


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    return render_template('photo_it.html')


if __name__ == "__main__":
    app.run(debug=True)