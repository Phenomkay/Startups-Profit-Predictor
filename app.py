import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
 
state_mapping = {"New York": 0, "California": 1, "Florida": 2}
reverse_state_mapping = {v: k for k, v in state_mapping.items()}

st.set_page_config(page_title="Startup Profit Predictor", layout="centered")
st.title("Startup Profit Predictor")
st.markdown("### Predict the profitability of your startup based on spending in key areas")

st.sidebar.header("Enter Startup Details")
st.sidebar.markdown("Provide your startup's spending information below.")

rd_spend = st.sidebar.number_input("R&D Spend ($)", min_value=0, max_value=500000, step=1000)
admin_spend = st.sidebar.number_input("Administration Spend ($)", min_value=0, max_value=500000, step=1000)
marketing_spend = st.sidebar.number_input("Marketing Spend ($)", min_value=0, max_value=500000, step=1000)

state = st.sidebar.selectbox("State", options=list(state_mapping.keys()))
state_encoded = state_mapping[state]

# Predict Button
if st.sidebar.button("Predict Profit"):
    # Prepare input for prediction
    input_data = np.array([[rd_spend, admin_spend, marketing_spend, state_encoded]])
    profit_prediction = model.predict(input_data)[0]


    st.success(f"Estimated Profit for your startup in {state}: ${profit_prediction:,.2f}")


st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    .css-1d391kg {
        color: #bb86fc; /* Sidebar header color */
    }
    .stButton>button {
        background-color: #6200ee;
        color: white;
        font-weight: bold;
        font-size: 16px;
        padding: 8px 20px;
        border-radius: 8px;
    }
    .stAlert {
        border-radius: 8px;
        background-color: #333333;
        color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #bb86fc; /* Header text color */
    }
    </style>
    """, unsafe_allow_html=True
)

# Footer Information with Mobile Sidebar Instruction
st.markdown("---")
st.markdown(
    '<div class="mobile-instruction">📱 Instruction for Mobile Users: Tap the arrow at the top left to open the sidebar and enter your data for prediction.</div>',
    unsafe_allow_html=True
)