
from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # 🔴 Dummy prediction (replace with model later)
            predicted_breed = "Golden reteriver"

            return render_template(
                'output.html',
                breed=predicted_breed,
                image_path=filepath
            )

    return render_template('predict.html')


if __name__ == '__main__':
    app.run(debug=True)

