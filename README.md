# Heart-Disease-Prediction
# ❤️ Heart Disease Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict the likelihood of heart disease using machine learning algorithms based on patient medical data. The goal is to assist in early detection and support healthcare decision-making.

---

## 🚀 Features

* Predict heart disease risk based on user inputs
* Trained multiple ML models (Logistic Regression, Decision Tree, Random Forest)
* Compared models using evaluation metrics
* Deployed using Streamlit for real-time predictions

---

## 📊 Dataset

* Source: Kaggle
* Contains medical attributes such as:

  * Age
  * Sex
  * Chest Pain Type
  * Blood Pressure
  * Cholesterol
  * Maximum Heart Rate
  * And more...

---

## 🧠 Machine Learning Workflow

### 1. Data Preprocessing

* Checked for missing values
* Feature selection
* Data scaling using StandardScaler

### 2. Model Building

* Logistic Regression
* Decision Tree
* Random Forest (Best Performing Model)

### 3. Model Evaluation

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

📌 **Note:** Recall was prioritized to minimize false negatives in medical prediction.

---

## 💻 Streamlit Web App

The project includes an interactive web application where users can:

* Enter patient details
* Get instant prediction
* View risk probability

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/Dk-Kushwaha12/heart-disease-prediction.git
```

2. Navigate to project folder:

```bash
cd heart-disease-prediction
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
heart-disease-prediction/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── heart.csv
├── main.ipynb
└── README.md
```

---

## 📈 Results

* Random Forest achieved the best performance
* High recall ensured better detection of heart disease cases

---

## 🔮 Future Improvements

* Hyperparameter tuning
* Deploy on cloud (AWS/Heroku)

---

## 👩‍💻 Author

Deepika Kushwaha

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
