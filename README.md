# 📊 ChurnGuard AI - Customer Retention Predictor

**Live Demo:** [ https://customer-churn-predictor-jlsu.onrender.com ]

ChurnGuard AI is a full-stack machine learning application designed to help businesses predict customer churn. By analyzing metrics like tenure, monthly charges, and support interactions, the tool provides real-time risk assessments to help teams improve retention.

## 🚀 Key Features
- **Real-Time Prediction:** Instant risk analysis for individual customers.
- **Bulk CSV Processing:** Upload entire spreadsheets to analyze hundreds of customers at once.
- **Dynamic Data Cleaning:** Robust backend logic that cleans and validates CSV headers automatically.
- **Data Export:** Session history can be exported back to CSV for business reporting.

## 🛠️ Tech Stack
- **Backend:** Python 3.14, Flask
- **Machine Learning:** Scikit-Learn (Random Forest Classifier), Pandas, NumPy
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Deployment:** Render (CI/CD via GitHub)

## 📂 How to use Bulk Upload
To use the bulk upload feature, your CSV should contain the following columns:
1. `Tenure` (Months)
2. `Monthly_Charges` (USD)
3. `Support_Calls` (Count in last 30 days)

*Note: The app is smart enough to handle extra columns or lowercase headers!*
