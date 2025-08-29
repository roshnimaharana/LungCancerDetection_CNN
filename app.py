from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import os



app = Flask(__name__)  

cnn_model = load_model("lung_cancer_detection.h5")  # Ensure this file exists in the same folder

@app.route('/')
def index():
    return render_template("Roshni.html")  # index.html must be inside a 'templates' folder


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        # Save file temporarily
        file_path = 'temp_image.jpg'
        file.save(file_path)

        # Preprocess the image
        img = load_img(file_path, target_size=(256, 256))  # Match your model input size
        img_array = img_to_array(img) / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        result = cnn_model.predict(img_array)

        print("🔍 Prediction result:", result)
        print("🧪 Shape:", result.shape)

        # Map 4-class prediction to 2-class label
        predicted_index = np.argmax(result, axis=1)[0]

        if predicted_index in [0, 1]:
            prediction = "Cancer"
        elif predicted_index in [2, 3]:
            prediction = "Not Cancer"
        else:
            prediction = "Unknown"

        # Clean up
        os.remove(file_path)

        # Return result to frontend
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)