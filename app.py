import streamlit as st
import pickle
import numpy as np

# Page Config
st.set_page_config(
    page_title="Medical Insurance Predictor",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Load model
with open("best_model (1).pkl", "rb") as file:
    model = pickle.load(file)

# Custom CSS for better UI
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            font-weight: 700;
            text-align: center;
            color: #2c3e50;
            margin-bottom: 5px;
        }
        .sub-text {
            text-align: center;
            color: #555;
            font-size: 17px;
            margin-bottom: 30px;
        }
        .result-box {
            padding: 20px;
            background-color: #e8f6ff;
            border-radius: 12px;
            border: 1px solid #b5daf1;
            text-align: center;
            margin-top: 20px;
        }
        .result-text {
            font-size: 26px;
            font-weight: 700;
            color: #2c3e50;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>🏥 Medical Insurance Charges Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-text'>Predict estimated insurance cost based on your age, BMI, and smoking habits.</div>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("📌 Input Details")
st.sidebar.write("Fill the details below:")

# Inputs
age = st.sidebar.number_input("🔹 Age", min_value=18, max_value=100, value=30)
bmi = st.sidebar.number_input("🔹 BMI", min_value=10.0, max_value=60.0, value=25.0)
smoker = st.sidebar.selectbox("🔹 Smoker", ["No", "Yes"])

# Encode Smoker
smoker_yes = 1 if smoker == "Yes" else 0

# Prepare Input
input_data = np.array([[age, bmi, smoker_yes]])

# Predict
st.write("### 📊 Prediction Section")
st.write("Click the button below to get your estimated medical insurance charges.")

if st.button("🔮 Predict Charges", use_container_width=True):
    prediction = model.predict(input_data)
    prediction_value = f"${prediction[0]:,.2f}"

    st.markdown(f"""
        <div class='result-box'>
            <div class='result-text'>💰 Estimated Charges: {prediction_value}</div>
        </div>
    """, unsafe_allow_html=True)
