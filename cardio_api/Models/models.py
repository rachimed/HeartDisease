import joblib

loaded_model = joblib.load("./Models/cardio_log_model.pkl")

class model():
    def predict(data):
        prediction = loaded_model.predict(data)
        
        print(loaded_model.predict_proba(data))
        if prediction == 0:
            return  0
        elif prediction == 1:
            return  1
        
        else:
            return 'Prediction inconnue'
        

    