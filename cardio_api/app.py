from flask import Flask, render_template, request,  url_for, redirect
import pickle
import pandas as pd
from Models.models import model
# instanciation off app Flask
app = Flask(__name__)


#! Routes
@app.route("/")
def home():


    return render_template('index.html')

#! Route formulaire

@app.route('/form', methods=["POST", "GET"])
def form():
    
    
    if request.method == 'POST':
        data = {}
        
        age= float(request.form['Age'])
        sex= float(request.form['Sex'])
        cp= float(request.form['ChestPainType'])
        rbp = float(request.form['RestingBP'])
        chol = float(request.form['Cholesterol'])
        fbs= float(request.form['FastingBS'])
        resecg= float(request.form['RestingECG'])
        maxhr= float(request.form['MaxHR'])
        exng = float(request.form['ExerciseAngina'])
        oldpeak = float(request.form['Oldpeak'])
        slp = float(request.form['ST_Slope'])
        
        data={
            'Age': age,
            'Sex': sex,
            'ChestPainType': cp,
            'RestingBP': rbp,
            'Cholesterol': chol,
            'FastingBS': fbs,
            'RestingECG': resecg,
            'MaxHR': maxhr,
            'ExerciseAngina': exng,
            'Oldpeak': oldpeak,
            'ST_Slope': slp
        }
        
        df = pd.DataFrame(data, index=[0])
        
        result = model.predict(df)
        
        print()
        
        return render_template('form.html', result=result, title="identification")
    else:
        return render_template('form.html', title="identification")

# Variables environement
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=8080)