import os
import pickle
import pandas as pd
import io
from flask import Flask, render_template, request, Response

app = Flask(__name__, template_folder='templates')

# Initialize history to store session data
predictions_history = []

# Load the trained model
try:
    with open('churn_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html', history=predictions_history)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Get data from the form
        tenure = float(request.form.get('tenure', 0))
        monthly_charges = float(request.form.get('monthly_charges', 0))
        support_calls = float(request.form.get('support_calls', 0))

        # 2. Create DataFrame with EXACT matching names from your training script
        input_data = pd.DataFrame([[tenure, monthly_charges, support_calls]], 
                                  columns=['Tenure', 'Monthly_Charges', 'Support_Calls'])

        # 3. Make prediction
        prediction = model.predict(input_data)[0]
        result = "High Risk of Churn" if prediction == 1 else "Low Risk (Stay)"
        
        # 4. Save to history list
        predictions_history.append({
            'Tenure': tenure,
            'Monthly_Charges': monthly_charges,
            'Support_Calls': support_calls,
            'Prediction': result
        })
        
        return render_template('index.html', prediction_text=result, history=predictions_history)
    except Exception as e:
        return f"Application Error: {str(e)}. Check if model features match input columns."

@app.route('/download')
def download():
    if not predictions_history:
        return "No data available", 400
    
    df = pd.DataFrame(predictions_history)
    output = io.StringIO()
    df.to_csv(output, index=False)
    
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=churn_predictions.csv"}
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
