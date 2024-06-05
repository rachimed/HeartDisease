# Heart Disease Detection Model with Flask API

This project includes a machine learning model for detecting heart disease and a Flask API for interacting with the model through a web interface.

## Model Overview:

The heart disease detection model is trained to predict the likelihood of an individual having heart disease based on various medical features. The features include age,
sex, chest pain type, resting blood pressure, cholesterol level, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise-induced
angina, oldpeak (ST depression induced by exercise relative to rest), and the slope of the peak exercise ST segment.

## Flask API:

The Flask API serves as the backend for the heart disease detection system. It provides a web interface for users to input their medical information and receive predictions
about their heart disease risk. The API handles HTTP requests and utilizes the trained machine learning model to make predictions in real-time.

### Routes:

- `/`: Home route, renders the main page of the web interface.
- `/form`: Route for the heart disease risk prediction form. Accepts POST requests with user input data and returns predictions.

### Usage:

To use the Flask API:

1. Ensure all dependencies are installed. You can install them using `pip install -r requirements.txt`.
2. Run the Flask application using `python app.py`.
3. Access the web interface by navigating to `http://localhost:8080` in your web browser.

## Directory Structure:

- `app.py`: Main Flask application file containing route definitions and API logic.
- `templates/`: Directory containing HTML templates for rendering web pages.
- `Models/`: Directory containing the heart disease detection model (Python script or pickle file).
- `requirements.txt`: Text file listing all dependencies required to run the Flask application.

## Usage Notes:

- Customize the HTML templates and route logic as needed.
