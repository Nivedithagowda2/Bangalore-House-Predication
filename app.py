import streamlit as st
import pickle
import numpy as np

# -----------------------------------
# Load Model
# -----------------------------------
with open("bangalore_home_price_model.pkl", "rb") as f:
    data = pickle.load(f)

model = data["model"]
columns = data["columns"]

# -----------------------------------
# Sidebar Navigation
# -----------------------------------
st.sidebar.title("🏡 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "ℹ About"])

# -----------------------------------
# HOME PAGE (Prediction)
# -----------------------------------
if page == "🏠 Home":
    st.title("🏡 Bangalore House Price Prediction App")
    st.write("Enter details to estimate house price (in Lakhs).")

    # ------- User Inputs -------
    sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, value=1000)
    bath = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
    bhk = st.number_input("BHK", min_value=1, max_value=10, value=2)
    location = st.selectbox("Select Location", columns[3:])

    # ------- Prediction Function -------
    def predict_price(sqft, bath, bhk, location):
        x = np.zeros(len(columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk

        if location in columns:
            idx = columns.index(location)
            x[idx] = 1

        return model.predict([x])[0]

    # ------- Prediction History -------
    if "history" not in st.session_state:
        st.session_state.history = []

    # ------- Predict Button -------
    if st.button("Predict Price"):
        price = round(predict_price(sqft, bath, bhk, location), 2)
        st.success(f"🏷 Estimated Price: ₹ {price} Lakhs")

        st.session_state.history.append({
            "Total Sqft": sqft,
            "Bathrooms": bath,
            "BHK": bhk,
            "Location": location,
            "Predicted Price (Lakhs)": price
        })

    # ------- Show History -------
    if st.session_state.history:
        st.markdown("## 📝 Prediction History")
        st.table(st.session_state.history)


# -----------------------------------
# ABOUT PAGE
# -----------------------------------
if page == "ℹ About":
    st.title("ℹ About This Project")
    st.write("""
    ### 🏡 Bangalore House Price Prediction App
    This application predicts **house prices in Bangalore** based on:
    - Total Square Feet  
    - Number of Bathrooms  
    - Number of BHK  
    - Location (One-Hot Encoding)

    ### 🧠 Machine Learning Model
    The model is trained using:
    - Python  
    - Pandas  
    - NumPy  
    - Scikit-Learn (Ridge Regression)  
    - One-Hot Encoded categorical features  

    ### 📦 Dataset
    The dataset contains:
    - 243 location features  
    - Cleaned & processed price per sqft  
    - Final engineered dataframe used for training  

    ### 🎯 Goal
    This project helps users quickly estimate the **approximate market price of a house** in Bangalore.

    ### 👩🏻‍💻 Developer
    **Niveditha Gowda**  
    Data Science Enthusiast  
    Passionate about ML & real-world applications.

    ### 🚀 Future Enhancements
    - Add map-based price visualization  
    - Deep learning models  
    - API + mobile app  
    """)

    st.success("Thank you for using the app! 😊")

