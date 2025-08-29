# LungCancerDetection_CNN

<li>This project aims to detect lung cancer using a Convolutional Neural Network (CNN) model deployed with Flask.</li>
<li>It includes a Jupyter notebook (lung_cancer_detection.ipynb) for model training and a Flask app (app.py) for making predictions. Additionally, an HTML template (roshni.html) is provided for the web interface.</li>

## Model
<li>The model is trained using the notebook lung_cancer_detection.ipynb.</li>
<li>It uses a CNN architecture to classify CT scan images into two categories: Normal and Cancerous.</li>

## Flask App
<li>The Flask app (app.py) serves as the backend for making predictions.</li>
<li>It loads the trained model and preprocesses images uploaded by users for prediction.</li>
<li>Predictions are displayed on the web interface.</li>
  
## Web Interface
<li>The web interface (roshni.html) allows users to upload CT scan images and receive predictions for lung cancer.</li>
<li>It provides feedback on the prediction (Normal or Cancerous).</li>

## Usage
<li>Run the Flask app: python app.py</li>
<li>Access the web interface in your browser at http://localhost:5000</li>
<li>Make sure h5 path is correct in 'app.py'</li>
