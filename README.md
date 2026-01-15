#  Solar Power Generation Prediction

##  Project Overview
This project focuses on predicting the **AC power output of a solar power plant** using machine learning techniques.  
The prediction is based on historical **solar generation data** and **weather sensor data**.  
The trained model is deployed as an interactive **Streamlit web application** for real-time predictions.

---

##  Objective
The main objective of this project is to build a reliable and accurate machine learning model that can estimate solar power generation based on environmental and operational parameters, helping in better energy planning and optimization.

---

##  Machine Learning Approach
- **Algorithm Used:** Random Forest Regressor  
- **Type:** Supervised Regression  
- **Target Variable:** AC Power  

###  Input Features
- Ambient Temperature  
- Module Temperature  
- Irradiation  
- DC Power  
- Daily Yield  

---
##  Project Structure
solar-power-generation-prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│ └── solar_rf_small.pkl
│
└── notebooks/
└── solar_power_gen_project.ipynb


---

##  Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Matplotlib & Seaborn  
- Git & GitHub  

---

##  How to Run the Project Locally

###  Install Dependencies
```bash
pip install -r requirements.txt
```
### Run the Streamlit App
```bash
python -m streamlit run app.py
```
The application will open automatically in your browser.

###  Deployment

Framework: Streamlit

Deployment Platform: Streamlit Community Cloud

Version Control: GitHub

###  Results

The Random Forest model provides accurate predictions for AC power output.

The web application allows users to input real-time values and get instant predictions.

The system performs well across different weather and operational conditions.


### Learning Outcomes

Hands-on experience with real-world solar power datasets

End-to-end machine learning pipeline development

Model deployment using Streamlit

GitHub project management and version control

