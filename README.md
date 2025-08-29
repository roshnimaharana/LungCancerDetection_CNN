# LungCancerDetection_CNN

<li>This project aims to detect lung cancer using a Convolutional Neural Network (CNN) model deployed with Flask.</li>
<li>It includes a Jupyter notebook (lung_cancer_detection.ipynb) for model training and a Flask app (app.py) for making predictions. Additionally, an HTML template (roshni.html) is provided for the web interface.</li>




## About The Project

Lung Cancer is one of the leading life taking cancer worldwide. Early detection and treatment are crucial for patient recovery. Medical professionals use histopathological images of biopsied tissue from potentially infected areas of lungs for diagnosis. Most of the time, the diagnosis regarding the types of lung cancer are error-prone and time-consuming. Convolutional Neural networks can identify and classify lung cancer types with greater accuracy in a shorter period, which is crucial for determining patients' right treatment procedure and their survival rate. Adenocarcinoma, and squamous carcinoma cell,large cell and normal cell are considered in this research work. 




## Dataset

The dataset used in this project consists of lung cancer images categorized into four classes:
1. Normal
2. Adenocarcinoma
3. Large Cell Carcinoma
4. Squamous Cell Carcinoma

The dataset should be organized into training (`train`), validation (`valid`), and testing (`test`) folders with the following subfolders for each class:

- `train/`
  - `normal/`
  - `adenocarcinoma/`
  - `large_cell_carcinoma/`
  - `squamous_cell_carcinoma/`

- `valid/`
  - `normal/`
  - `adenocarcinoma/`
  - `large_cell_carcinoma/`
  - `squamous_cell_carcinoma/`

- `test/`
  - `normal/`
  - `adenocarcinoma/`
  - `large_cell_carcinoma/`
  - `squamous_cell_carcinoma/`





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




## Acknowledgements

We acknowledge and thank the contributors to the [Chest CT Scan Images Dataset](https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images) on Kaggle for providing the dataset used in this project.




## Usage

<li>Run the Flask app: python app.py</li>
<li>Access the web interface in your browser at http://localhost:5000</li>
<li>Make sure h5 path is correct in 'app.py'</li>


