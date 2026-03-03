import os
import pickle
import pandas as pd
from flask import Flask, render_template, request

# Initialize Flask with the correct template folder
app = Flask(__name__, template_folder='templates')

# Load the trained model
with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    tenure = float(request.form['tenure'])
    monthly_charges = float(request.form['monthly_charges'])
    support_calls = float(request.form['support_calls'])

    # Create a DataFrame for the model
    input_data = pd.DataFrame([[tenure, monthly_charges, support_calls]], 
                              columns=['tenure', 'monthly_charges', 'support_calls'])

    # Make prediction
    prediction = model.predict(input_data)[0]
    
    result = "High Risk of Churn" if prediction == 1 else "Low Risk (Stay)"
    
    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    # Use the port Render provides or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
